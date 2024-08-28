import os
import bertopic
from sentence_transformers import SentenceTransformer


ROOT_DIR = os.getcwd()
BERTOPIC_MODEL = os.path.join(ROOT_DIR, 'models', 'bertopic')
EMB_MODEL = SentenceTransformer('BAAI/bge-large-en-v1.5')


def test_model_exists():
    assert os.path.exists(BERTOPIC_MODEL)
    
    fns = os.listdir(BERTOPIC_MODEL)
    assert len(fns) == 5
    
    expected_fns = [
        "ctfidf_config.json",
        "ctfidf.safetensors",
        "topic_embeddings.safetensors",
        "topics.json",
        "config.json",
    ]
    
    for fn in expected_fns:
        assert fn in fns


def test_inference():
    model = bertopic.BERTopic().load(BERTOPIC_MODEL, embedding_model=EMB_MODEL)
    assert isinstance(model, bertopic.BERTopic)
    abstract = """
    Assessing seismic hazards and thereby designing earthquake-resilient structures or 
    evaluating structural damage that has been incurred after an earthquake are important 
    objectives in earthquake engineering. Both tasks require critical evaluation of strong 
    groundAssessing seismic hazards and thereby designing earthquake-resilient structures or 
    evaluating structural damage that has been incurred after an earthquake are important 
    objectives in earthquake engineering. Both tasks require critical evaluation of strong 
    ground motion records, and the knowledge of site conditions at the earthquake stations plays 
    a major role in achieving the aforementioned objectives. Site conditions are generally 
    represented by the time-averaged shear wave velocity in the upper 30 meters of the geological 
    materials (Vs30). Several strong motion stations lack Vs30 measurements resulting in 
    potentially inaccurate assessment of seismic hazards and evaluation of ground motion 
    records. In this study, we present a deep learning-based approach for predicting Vs30 at 
    strong motion station locations using three-channel earthquake records. For this purpose, 
    Convolutional Neural Networks (CNNs) with dilated and causal convolutional layers are used 
    to extract deep features from accelerometer records collected from over 700 stations located 
    in Turkey. In order to overcome the limited availability of labeled data, 
    we propose a two-phase training approach. In the first phase, a CNN is trained to 
    estimate the epicenters, for which ground truth is available for all records. 
    After the CNN is trained, the pre-trained encoder is fine-tuned based on the Vs30 ground truth. 
    The performance of the proposed method is compared with machine learning models that utilize 
    hand-crafted features. The results demonstrate that the deep convolutional encoder based 
    Vs30 prediction model outperforms the machine learning models that rely on hand-crafted features. 
    motion records, and the knowledge of site conditions at the earthquake stations plays a 
    major role in achieving the aforementioned objectives. Site conditions are generally represented 
    by the time-averaged shear wave velocity in the upper 30 meters of the geological materials 
    (Vs30). Several strong motion stations lack Vs30 measurements resulting in potentially inaccurate 
    assessment of seismic hazards and evaluation of ground motion records. In this study, 
    we present a deep learning-based approach for predicting Vs30 at strong motion station 
    locations using three-channel earthquake records. For this purpose, 
    Convolutional Neural Networks (CNNs) with dilated and causal convolutional layers are 
    used to extract deep features from accelerometer records collected from over 700 stations 
    located in Turkey. In order to overcome the limited availability of labeled data, 
    we propose a two-phase training approach. In the first phase, a CNN is trained to estimate 
    the epicenters, for which ground truth is available for all records. After the CNN is trained, 
    the pre-trained encoder is fine-tuned based on the Vs30 ground truth. 
    The performance of the proposed method is compared with machine learning models that utilize 
    hand-crafted features. The results demonstrate that the deep convolutional encoder based 
    Vs30 prediction model outperforms the machine learning models that rely on hand-crafted features.
    """
    
    topic, _ = model.transform([abstract])
    result = model.get_topic(topic=topic[0], full=True)
    
    keys = [
        "KeyBERT",
        "MMR",
        "Main",
        "OpenAI",
        "POS"
    ]
    for key in result.keys():
        assert key in keys
    
    assert result['OpenAI'][0][0] == 'Multi-Label Zero Shot Learning'
