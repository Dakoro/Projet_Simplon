import os
import mlflow
import pickle
import pandas as pd
from bertopic import BERTopic
from dotenv import load_dotenv
from umap import UMAP
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from gensim import corpora
from gensim.models.coherencemodel import CoherenceModel
from utils import load_embeddings
from bertopic.representation import (
    KeyBERTInspired,
    MaximalMarginalRelevance,
    OpenAI,
    PartOfSpeech
)

load_dotenv()
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
mlflow.set_experiment("Topic Modeling")


def get_umap(list_params: list[dict]):
    umap_model_list = []
    for params in list_params:
        umap_model = UMAP(
            n_components=params['n_components'],
            n_neighbors=params['n_neighbors'],
            metric=params['metric'],
            random_state=42
        )
        umap_model_list.append(umap_model)
    return umap_model_list


def get_hdbscan(params_list: list[dict]):
    hdbscan_model_list = []
    for params in params_list:
        hdbscan_model = HDBSCAN(
            min_cluster_size=params['min_cluster_size'],
            min_samples=params['min_samples'],
            cluster_selection_method=params['cluster_selection_method'],
            prediction_data=True
        )
        hdbscan_model_list.append(hdbscan_model)
    return hdbscan_model_list


def train_bertopic(
        docs,
        embeddings,
        years,
        embeddings_model,
        vectorizer_model,
        umap_model,
        hdbscan_model,
        representation_model,
        umap_params,
        hdbscan_params,
        run_name):
    with mlflow.start_run(run_name=run_name):
        mlflow.log_params(umap_params)
        mlflow.log_params(hdbscan_params)
        model = BERTopic(
            embedding_model=embeddings_model,
            vectorizer_model=vectorizer_model,
            umap_model=umap_model,
            hdbscan_model=hdbscan_model,
            representation_model=representation_model,
            top_n_words=10,
            verbose=True)
        topics, probs = model.fit_transform(documents=docs,
                                            embeddings=embeddings)
        # reduce_topics = model.reduce_outliers(docs,
        # topics,
        # strategy='embeddings',
        # embeddings=embeddings)
        # model.update_topics(docs,
        #                     topics=reduce_topics,
        #                     representation_model=representation_model,
        #                     vectorizer_model=vectorizer_model)
        coherence = get_coherence(model, topics, vectorizer_model, docs)
        mlflow.log_metric("coherence", coherence)
        topic_over_time = model.topics_over_time(docs, years, topics)
        return (model, topics, topic_over_time, probs, coherence)


def get_coherence(model, topics, vectorizer_model, docs):
    vectorizer = vectorizer_model
    analyzer = vectorizer.build_analyzer()
    _ = vectorizer.get_feature_names_out()
    tokens = [analyzer(doc) for doc in docs]
    dictionary = corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    topic_words = [[words for words, _ in model.get_topic(topic)]
                   for topic in range(len(set(topics))-1)]
    coherence_model = CoherenceModel(topics=topic_words,
                                     texts=tokens,
                                     corpus=corpus,
                                     dictionary=dictionary,
                                     coherence='c_v')
    coherence = coherence_model.get_coherence()
    return coherence


def get_best_model(coherence_list, list_topics):
    for coherence, topic in zip(coherence_list, list_topics):
        if coherence == max(coherence_list):
            return topic


def main():
    df = pd.read_csv('sample.csv')
    embeddings_model = SentenceTransformer('BAAI/bge-large-en-v1.5')
    docs = df['abstract'].to_list()
    embeddings = load_embeddings()
    years = df['year'].to_list()
    umap_params_1 = {
        "n_neighbors": 25,
        "n_components": 9,
        "metric": 'cosine'
    }

    umap_params_2 = {
        "n_neighbors": 10,
        "n_components": 5,
        "metric": 'cosine'
    }

    hdbscan_params_1 = {
        "min_cluster_size": 100,
        "min_samples": 30,
        "cluster_selection_method": "leaf"
    }

    hdbscan_params_2 = {
        "min_cluster_size": 200,
        "min_samples": 50,
        "cluster_selection_method": "leaf"
    }

    hdbscan_params_list = [hdbscan_params_1, hdbscan_params_2]
    umap_params_list = [umap_params_1, umap_params_2]

    vectorizer_model = CountVectorizer(stop_words="english", min_df=2,
                                       ngram_range=(1, 2))
    umap_model_list = get_umap(umap_params_list)
    hdbscan_model_list = get_hdbscan(hdbscan_params_list)

    # KeyBERT
    keybert_model = KeyBERTInspired()

    # Part-of-Speech
    pos_model = PartOfSpeech("en_core_web_sm")

    # MMR
    mmr_model = MaximalMarginalRelevance(diversity=0.3)

    OPENAI_API_KEY = os.getenv('OPENAI_KEY')

    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = """
    I have a topic that contains the following documents:
    [DOCUMENTS]
    The topic is described by the following keywords: [KEYWORDS]

    Based on the information above, extract a short but highly descriptive
    topic label of at most 5 words. Make sure it is in the following format:
    topic: <topic label>
    """
    openai_model = OpenAI(client=client,
                          model="gpt-3.5-turbo",
                          exponential_backoff=True,
                          chat=True,
                          prompt=prompt,
                          temperature=0)

    # All representation models
    representation_model = {
        "KeyBERT": keybert_model,
        "OpenAI": openai_model,  # Uncomment if you will use OpenAI
        "MMR": mmr_model,
        "POS": pos_model
    }

    list_topics = []
    for i in range(2):
        for j in range(2):
            tuple_topics = train_bertopic(
                docs,
                embeddings,
                years,
                embeddings_model=embeddings_model,
                vectorizer_model=vectorizer_model,
                umap_model=umap_model_list[i],
                hdbscan_model=hdbscan_model_list[j],
                representation_model=representation_model,
                umap_params=umap_params_list[i],
                hdbscan_params=hdbscan_params_list[j],
                run_name=f'bertopic_run_{i}{j}'
            )
            list_topics.append(tuple_topics)
    coherence_list = [topic[-1] for topic in list_topics]
    best_model = get_best_model(coherence_list, list_topics)[0]
    bertopic_fp = os.path.join(os.getcwd(), 'models', 'bertopic')
    best_model.save(bertopic_fp,
                    serialization="safetensors",
                    save_ctfidf=True,
                    save_embedding_model=embeddings_model)


if __name__ == "__main__":
    main()
