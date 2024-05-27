import os
import re
import pathlib
import pickle
import pandas as pd
import networkx as nx
import nx2vos
from dataclasses import dataclass
from collections import Counter
from nltk import ngrams
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT_DIR = pathlib.Path(os.getcwd()).parent
DOCS_DIR = os.path.join(ROOT_DIR, 'pdfs', 'chunks')
STW = stopwords.words('english') + ['that', 'this', 'with', 'only']

def load_docs(path):
    list_docs = sorted(
        [os.path.join(DOCS_DIR, fn) for fn in os.listdir(DOCS_DIR) if fn.endswith('.pkl')],
        key=lambda x: int(re.sub('\D', '', x)))
    def open_doc(path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
    docs = []
    for fp in list_docs:
        data = open_doc(fp)
        docs += data
    return docs


@dataclass
class Coocurrences():
    sentences: list[str]
    top_nwords: int
    
    def _make_vocab(self):
        counter = Counter()
        for sentence in self.sentences:
            bigram = [' '.join(tup) for tup in ngrams(sentence.split(), 2)]
            trigram = [' '.join(tup) for tup in ngrams(sentence.split(), 3)]
            tokens = sentence.split() + bigram + trigram
            counter += Counter(tokens)
        words = counter.most_common(self.top_nwords)
        return [word for word, _ in words]
    
    def make_cooc_matrix(self, ngrams_tuple, max_features):
        vec = TfidfVectorizer(
            ngram_range=ngrams_tuple,
            stop_words='english',
            max_features=max_features, 
            vocabulary=self._make_vocab())
        X = vec.fit_transform(self.sentences)
        Xc = X.T * X
        names = vec.get_feature_names_out()
        df_cooc = pd.DataFrame(data=Xc.toarray(), columns=names, index=names)
        return df_cooc


def clean_text(text: str):
    text = re.sub('\n', '', text).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'http[s]?://\S+', '', text)
    tokens = [tok for tok in text.split() if tok.strip() not in STW]
    tokens = [tok for tok in tokens if len(tok) > 3]
    return " ".join(tokens)


def make_ssn(fn):
    docs = load_docs(DOCS_DIR)
    text = []
    for d in docs:
        arxiv_id = d.metadata['file_path'].split('/')[-1]
        arxiv_id = re.sub('.pdf', '', arxiv_id)
        if arxiv_id == fn:
            text.append(d)
    sentences = [clean_text(t.page_content) for t in text]
    df_cooc = Coocurrences(sentences, 1000).make_cooc_matrix((1,3), 10000)
    graph = nx.from_pandas_adjacency(df_cooc)
    graph_path = f'/home/dakoro/Github/Projet_Simplon/arxiv_app/media/graph_{fn}.json'
    nx2vos.write_vos_json(graph, graph_path)
    
    