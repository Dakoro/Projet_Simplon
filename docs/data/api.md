## API data
API that allow acces to arxiv paper

### Source code
Source code is stored in the api/model folder
- database.py : Create a the data base instance
- desp.py : dependency injection file (handle protected route with jwt token)
- gunicorn.conf.py
- main.py: main fastapi file
- models.py: containt user model
- requirements.txt: api requirements
- schemas.py: pydantic schema
- test_api.py: pytest file

### Install dependencies
```sh
pip install -r api/data/requirements.txt
```

### Launch api
```sh
make api_data
```

### Test api
```sh
make test-api-data
```