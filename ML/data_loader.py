import json
import random


def fetch_data():
    with open('training.json') as training_f:
        training = json.load(training_f)
    with open('validation.json') as valid_f:
        validation = json.load(valid_f)
    # If needed you can shrink the training and validation data to speed up somethings but this isn't always safe to do by setting k < 16000
    #k = 100
    #random.shuffle(training)
    #random.shuffle(validation)
    #training, validation = training[:k], validation[:(k // 10)]
    tra = []
    val = []
    for elt in training:
        tra.append((elt["text"].split(), int(elt["stars"]-1)))
    for elt in validation:
        val.append((elt["text"].split(), int(elt["stars"]-1)))
    return tra, val
