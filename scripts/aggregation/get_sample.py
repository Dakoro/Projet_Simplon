import re
import os
import nltk
import pickle
import pandas as pd
from nltk.corpus import stopwords

nltk.download('stopwords')

STW = stopwords.words('english')


def process(text: str):
    text = [re.sub(r'[^\w\s]', ' ', s) for s in text.split()]
    text = [s.strip().lower() for s in text if s.strip().lower() not in STW]
    return " ".join(text)


def main():
    path = os.path.join(os.getcwd(), "files", "pkl", "aggreated_data.pkl")
    df = pd.read_pickle(path).sample(n=10000, random_state=42)
    df['abstract'] = df['abstract'].apply(process)
    
    sample_fp = os.path.join(os.getcwd(), "files", "pkl", "sample.pkl")
    test_fp = os.path.join(os.getcwd(), "files", "pkl", "test_data.pkl")
    df_test = df.sample(n=2000, random_state=42)

    df.to_pickle(sample_fp, protocol=pickle.HIGHEST_PROTOCOL)
    df_test.to_pickle(test_fp, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    main()
