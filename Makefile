VENV := env
PYTHON := $(VENV)/bin/python

setup: requirements.txt
    python3 -m venv $(VENV)
    $(VENV)/bin/pip install -r requirements.txt

update_requirements: requirements.txt
	$(VENV)/bin/pip freeze > requirements.txt

create_and_load_bdd: scripts/load_all.py
	$(PYTHON) -m scripts/load_all.py

run_api: api/data/main.py
	cd api/data && uvicorn main:app --reload