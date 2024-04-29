
requirements: requirements.txt
	pip freeze > requirements.txt

bdd:
	python scripts/bdd/load_all.py

dataset:
	python scripts/aggregation/get_data.py

sample:
	python scripts/aggregation/get_sample.py

embeddings:
	python scripts/aggregation/get_embeddings.py

topic_modeling:
	pip install scipy==1.12.0
	python scripts/experiments/topic_modeling.py
	pip install scipy

clustering:
	python scripts/experiments/clustering.py

api_data: 
	cd api/data && uvicorn main:app --reload --port 8081

api_model: 
	cd api/model && uvicorn main:app --reload --host 0.0.0.0 --port 8082

api_model_container:
	cd api/model && gunicorn main:app --timeout 60

test-api:
	cd api/model && pytest -s

local-api-container:
	docker compose -f .local/docker-compose.yml up

test-api-container:
	docker compose -f .ci/docker-compose.yml up -d

mlflow-server:
	mlflow server \
    --backend-store-uri sqlite:///mlflow/mlruns.db \
	--default-artifact-root mlflow/mlruns \
    --host 0.0.0.0 \
    -p 8083

run_app:
	cd arxiv_app && python manage.py runserver

prune-docker:
	docker system prune --all --volumes