VENV := env
PYTHON := $(VENV)/bin/python

setup:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

requirements: requirements.txt
	$(VENV)/bin/pip freeze > requirements.txt

bdd: bdd.db
	$(PYTHON) scripts/bdd/load_all.py

dataset: aggreated_data.csv
	$(PYTHON) scripts/aggregation/get_data.py

sample: sample.csv
	$(PYTHON) scripts/aggregation/get_sample.py

embeddings: embeddings.pkl
	$(PYTHON) scripts/get_embeddings.py

topic_modeling:
	$(PYTHON) scripts/experiments/topic_modeling.py

clustering:
	$(PYTHON) scripts/experiments/clustering.py

api_data: 
	cd api/data && uvicorn main:app --reload --port 8080

api_model: 
	cd api/model && uvicorn main:app --reload --port 8081

mlflow:
	mlflow server --port 8082

run_app:
	cd arxiv_app && ../$(PYTHON) manage.py runserver