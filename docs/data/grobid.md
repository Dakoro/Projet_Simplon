## Parsing des pdfs avec grobid
[grobid docs](https://grobid.readthedocs.io/en/latest/Introduction/)
GROBID is a tool for parsing pdf. It uses a CRF model and a Deep Leaning model, these two models
were trained on academic papers. 
warning: the base image is heavy (18G) be carfule with docker

### Run grobid container
```sh
make grobid-container
```

### Download PDFs
```sh
make get-pdfs
```

### Process PDFs
```sh
make pdf-processing
```