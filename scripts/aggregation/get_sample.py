import pandas as pd
import re
from nltk.corpus import stopwords
from dotenv import load_dotenv
load_dotenv()

STW = stopwords.words('english')


def process(text: str):
    text = [re.sub(r'[^\w\s]', ' ', s) for s in text.split()]
    text = [s.strip().lower() for s in text if s.strip().lower() not in STW]
    return " ".join(text)


def main():
    path = '/home/dakoro/Projet_Simplon/aggreated_data.csv'
    df = pd.read_csv(path).sample(n=10000, random_state=42)
    df['abstract'] = df['abstract'].apply(process)
    df.to_csv('sample.csv', index=False)


if __name__ == "__main__":
    main()
