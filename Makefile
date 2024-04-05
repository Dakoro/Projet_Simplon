
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
	cd api/model && uvicorn main:app --reload --port 8082

mlflow:
	mlflow server --port 8083

run_app:
	cd arxiv_app && python manage.py runserver

qdrant:
	docker run -p 6333:6333 -p 6334:6334 \
	-v $(pwd)/qdrant_storage:/qdrant/storage:z \
	qdrant/qdrant