import pandas as pd
from dotenv import load_dotenv
load_dotenv()


def main():
    path = '/home/dakoro/Projet_Simplon/aggreated_data.csv'
    df = pd.read_csv(path).sample(n=10000, random_state=42)
    df.to_csv('sample.csv')


if __name__ == "__main__":
    main()
