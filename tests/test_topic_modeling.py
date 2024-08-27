import os

ROOT_DIR = os.getcwd()

def test_model_exists():
    bertopic_path = os.path.join(ROOT_DIR, 'models', 'bertopic')
    assert os.path.exists(bertopic_path)
    
    fns = os.listdir(bertopic_path)
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