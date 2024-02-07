VENV := env
PYTHON := $(VENV)/bin/python

setup:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

requirements: requirements.txt
	$(VENV)/bin/pip freeze > requirements.txt

create_and_load_bdd: bdd.db
	$(PYTHON) scripts/load_all.py

dataset: aggreated_data.csv
	$(PYTHON) scripts/get_data.py

embeddings: embeddings.pkl
	$(PYTHON) scripts/get_embeddings.py

api_data: api/data/main.py
	cd api/data && uvicorn main:app --reload

api_model: api/model/main.py
	cd api/model && uvicorn main:app --reload

