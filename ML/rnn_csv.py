import numpy as np
import torch
import torch.nn as nn
from torch.nn import init
import torch.optim as optim
import math
import random
import os
from torch.autograd import Variable
import time
from tqdm import tqdm
from data_loader import fetch_data
import spacy
import os
import pickle
import csv

unk = '<UNK>'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

class RNN(nn.Module):
    def __init__(self, input_dim, h, output_size, n_layers, device):  # Add relevant parameters
        super(RNN, self).__init__()
        self.device = device
        self.h = h
        self.n_layers = n_layers
        self.activation = nn.ReLU()
        self.fc = nn.Linear(h, output_size)
        self.rnn = nn.RNN(input_dim, h, n_layers,
                          nonlinearity='relu')
        # Ensure parameters are initialized to small values, see PyTorch documentation for guidance
        self.softmax = nn.LogSoftmax(dim=1)
        # These two combined are the same as the crossentropyloss() function
        self.loss = nn.NLLLoss()

    def compute_Loss(self, predicted_vector, gold_label):
        return self.loss(predicted_vector, gold_label)

    def forward(self, inputs):
        out, hidden = self.rnn(inputs)
        out = self.fc(out[-1].view(1, -1))
        output = self.softmax(out)
        return output, hidden


def convert_to_vector_representation(data):
    spacy.prefer_gpu()
    nlp = spacy.load("en_core_web_lg")
    vectors = []
    for document, star in tqdm(data):
        #document = nlp(document)
        document_vectors = []
        for i in document:
            i = nlp(i)
            document_vectors.append(i.vector)
        vectors.append((torch.tensor(document_vectors), star))
    return vectors


CACHED = True


def main(hidden_dim, number_of_epochs):  # Add relevant parameters
    index_global = 0
    is_cuda = torch.cuda.is_available()
    if is_cuda:
        device = torch.device("cuda")
        print("GPU is available")
    else:
        device = torch.device("cpu")
        print("GPU not available, CPU used")

    print("Fetching data")
    # X_data is a list of pairs (document, y); y in {0,1,2,3,4}
    train_data, valid_data = fetch_data()
    print("Data fetched")
    #train_data = convert_to_vector_representation(train_data)
    #valid_data = convert_to_vector_representation(valid_data)
    if CACHED:
        train_data = pickle.load(open("train_data.pkl", "rb"))
        valid_data = pickle.load(open("valid_data.pkl", "rb"))
    else:
        train_data = convert_to_vector_representation(train_data)
        valid_data = convert_to_vector_representation(valid_data)
        pickle.dump(train_data, open("train_data.pkl", "wb"))
        pickle.dump(valid_data, open("valid_data.pkl", "wb"))

    print("Vectorized data")

    # Create RNN
    model = RNN(input_dim=300, h=hidden_dim,
                output_size=5, n_layers=1, device=device)
    model.to(device)
    optimizer = optim.SGD(model.parameters(), lr=0.005, momentum=0.9)
    for epoch in range(number_of_epochs):
        model.train()
        optimizer.zero_grad()
        loss = None
        correct = 0
        total = 0
        start_time = time.time()
        print("Training started for epoch {}".format(epoch + 1))
        random.shuffle(train_data)
        minibatch_size = 16
        N = len(train_data)
        for minibatch_index in tqdm(range(N // minibatch_size)):
            optimizer.zero_grad()
            loss = None
            for example_index in range(minibatch_size):
                input_vector, gold_label = train_data[minibatch_index *
                                                      minibatch_size + example_index]
                input_vector = input_vector.to(device)
                predicted_vector, hidden = model(input_vector.unsqueeze(1))
                predicted_label = torch.argmax(predicted_vector)
                correct += int(predicted_label == gold_label)
                total += 1
                example_loss = model.compute_Loss(
                    predicted_vector.view(1, -1), torch.tensor([gold_label]))
                if loss is None:
                    loss = example_loss
                else:
                    loss += example_loss
            loss = loss / minibatch_size
            if (loss.item() > 100):
                print ("Stopping: Model might be Overfitting")
                os._exit(1)
            loss.backward()
            #nn.utils.clip_grad_norm_(model.parameters(),0.5)
            optimizer.step()
        print("Training completed for epoch {}".format(epoch + 1))
        print("Training accuracy for epoch {}: {}".format(
            epoch + 1, correct / total))
        print("Training time for this epoch: {}".format(time.time() - start_time))
        model.eval()
        loss = None
        correct = 0
        total = 0
        start_time = time.time()
        print("Validation started for epoch {}".format(epoch + 1))
        #random.shuffle(valid_data)
        minibatch_size = 16
        N = len(valid_data)
        with open('rnn.csv', 'a') as csvFile:
            row = ["index", "epoch", "gold_label", "predicted_label"]
            writer = csv.writer(csvFile)
            writer.writerow(row)
            for minibatch_index in tqdm(range(N // minibatch_size)):
                optimizer.zero_grad()
                loss = None
                for example_index in range(minibatch_size):
                    input_vector, gold_label = valid_data[minibatch_index *
                                                          minibatch_size + example_index]
                    input_vector = input_vector.to(device)
                    predicted_vector, hidden = model(input_vector.unsqueeze(1))
                    predicted_label = torch.argmax(predicted_vector)

                    row = [index_global, epoch + 1, gold_label, predicted_label]
                    writer = csv.writer(csvFile)
                    writer.writerow(row)


                    index_global = index_global + 1

                    correct += int(predicted_label == gold_label)
                    total += 1
                    example_loss = model.compute_Loss(
                        predicted_vector.view(1, -1), torch.tensor([gold_label]))
                    if loss is None:
                        loss = example_loss
                    else:
                        loss += example_loss
                loss = loss / minibatch_size
        csvFile.close()
        print("Validation completed for epoch {}".format(epoch + 1))
        print("Validation accuracy for epoch {}: {}".format(
            epoch + 1, correct / total))
        print("Validation time for this epoch: {}".format(
            time.time() - start_time))
