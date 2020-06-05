install:
	pip uninstall -y -r <(pip freeze)
	pip install -r requirements.txt

install3: #just in case
	pip3 uninstall -y -r <(pip freeze)
	pip3 install -r requirements.txt

collect:
	python3 collect_data.py

prepare:
	python3 prepare_data.py csv

run:
	python3 prepare_data.py
	python3 trials.py
	#python3 order_schedule.py (make sure clfs are ./SVM_Models/)
 	#python3 order_executor.py