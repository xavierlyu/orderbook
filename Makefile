venv: #works for mac only, if Windows, check venv.pdf 
	python3 -m pip install -U pip
	virtualenv -p python3 venv
	source venv/bin/activate
	pip install -r requirements.txt
	#for jupyter notebook just in case
	python3 -m ipykernel install --user --name=venv

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