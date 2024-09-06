### Install dependencies
```sh
pip install -r arxiv_app/requirements.txt
```

### Launch app 
```sh
make run_app
```

### Tests
Mlflow and api_model must be running
```sh
make test-app
```

### Pull image
```sh
docker pull ghcr.io/dakoro/projet_simplon/app:latest
```