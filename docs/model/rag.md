## RAG

### EMBEDDING MODEL
- [BGE](https://huggingface.co/BAAI/bge-large-en-v1.5/tree/main)

### LLM
- Openai api with langchain
```sh
pip install langchain openai --upgrade
```

### Qdrant with lanchain
```sh
pip install langchain qdrant_client --upgrade
```

### Qdrant container
```sh
make local-qdrant
```

### Load qdrant
```sh
make load-qdrant
```