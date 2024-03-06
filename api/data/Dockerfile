# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /


COPY api/data .
COPY bdd.db .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV BDD_URI=./bdd.db

EXPOSE 3100

CMD ["gunicorn", "main:app"]