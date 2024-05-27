### API Model
Api that allow acces to machine learning functionnality:
- clustering 
- topic modeling 
- rag

## Source code
Source code is stored in the api/model folder
- database.py : Create a the data base instance
- desp.py : dependency injection file (handle protected route with jwt token)
- gunicorn.conf.py
- main.py: main fastapi file
- models.py: containt user model
- requirements.txt: api requirements
- schemas.py: pydantic schema
- test_api_model.py: test with pytest