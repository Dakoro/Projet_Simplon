FROM python:3.10-slim-bullseye

COPY ../arxiv_app /arxiv_app
COPY ../Makefile /
COPY ../scripts/nltk_download.py nltk_download.py
COPY .env /
RUN apt-get update -y 
RUN apt-get install gcc build-essential -y

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r arxiv_app/requirements.txt
RUN python nltk_download.py

EXPOSE 8000

CMD ["make", "run_app"]