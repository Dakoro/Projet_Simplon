VENV := env
PYTHON := sudo $(VENV)/bin/python

setup:
	sudo python3 -m venv $(VENV)
	sudo $(VENV)/bin/pip install -r requirements.txt

requirements: requirements.txt
	sudo $(VENV)/bin/pip freeze > requirements.txt

bdd: bdd.db
	$(PYTHON) scripts/bdd/load_all.py

dataset:
	$(PYTHON) scripts/aggregation/get_data.py

sample:
	$(PYTHON) scripts/aggregation/get_sample.py

embeddings: embeddings.pkl
	$(PYTHON) scripts/get_embeddings.py

topic_modeling:
	$(PYTHON) scripts/experiments/topic_modeling.py

clustering:
	$(PYTHON) scripts/experiments/clustering.py

api_data: 
	cd api/data && uvicorn main:app --reload --port 8081

api_model: 
	cd api/model && uvicorn main:app --reload --port 8082

mlflow:
	mlflow server --port 8083

run_app:
	cd arxiv_app && ../$(PYTHON) manage.py runserver