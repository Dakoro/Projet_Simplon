## API Model
Api that allow acces to machine learning functionnality:
- clustering 
- topic modeling 
- rag

### Source code
Source code is stored in the api/model folder
- database.py : Create a the data base instance
- desp.py : dependency injection file (handle protected route with jwt token)
- gunicorn.conf.py
- main.py: main fastapi file
- models.py: containt user model
- requirements.txt: api requirements
- schemas.py: pydantic schema
- test_api_model.py: test with pytest

### Install dependencies
```sh
pip install -r api/model/requirements.txt
```

### Launch api
```sh
make api_model
```

### Test api
```sh
make test-api
```

### Pull image
```sh
docker pull ghcr.io/dakoro/projet_simplon/api_model:latest
```