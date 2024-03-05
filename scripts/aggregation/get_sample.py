import pandas as pd
import re
import os
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

STW = stopwords.words('english')


def process(text: str):
    text = [re.sub(r'[^\w\s]', ' ', s) for s in text.split()]
    text = [s.strip().lower() for s in text if s.strip().lower() not in STW]
    return " ".join(text)


def main():
    path = os.path.join(os.getcwd(), "files", "csv", "aggreated_data.csv")
    df = pd.read_csv(path).sample(n=10000, random_state=42)
    df['abstract'] = df['abstract'].apply(process)
    sample_fp = os.path.join(os.getcwd(), "files", "csv", "sample.csv")
    df.to_csv(sample_fp, index=False)


if __name__ == "__main__":
    main()
