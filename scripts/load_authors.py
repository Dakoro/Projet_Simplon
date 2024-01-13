import os
import logging as log
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from utils import load_arxiv_dataset, load_nips_dataset, format_arxiv_dataset

load_dotenv()

BDD_URI = os.getenv('BDD_URI')
ENGINE_URI = f'sqlite:///{BDD_URI}'


def get_result_count_optimized(df: pd.DataFrame):
    # Flatten the 'authors' lists into a single Series
    authors_series = df['authors'].explode()

    # Count the occurrences of each author
    result_count = authors_series.value_counts().to_dict()

    return result_count


def format_df_final(df: pd.DataFrame) -> pd.DataFrame:
    df['name'] = df['name'].str.lower()
    df_final = df.groupby('name').sum().reset_index()
    df_final = df_final.rename(columns={'count': 'article_count'})
    return df_final


def insert_bdd(df: pd.DataFrame):
    engine = create_engine(ENGINE_URI, echo=True)
    try:
        df.to_sql("Author", engine, if_exists='append', index=False)
    except Exception as e:
        log.warning('failed')
        print(e)


def main():

    df_nips = load_nips_dataset()

    df_nips_auth = df_nips.groupby('name').count().reset_index().rename(
        columns={"title": "count"}).drop(
            columns=['year'])

    df_arxiv = format_arxiv_dataset(load_arxiv_dataset())
    # authors = [author for ls in df_arxiv['authors'] for author in ls]
    article_count = get_result_count_optimized(df_arxiv)

    df_count = pd.DataFrame.from_dict(
        article_count, orient='index', columns=['count']).reset_index().rename(
        columns={"index": "name"})

    df_concat = pd.concat([df_nips_auth, df_count], axis=0)

    final_df = format_df_final(df_concat)
    insert_bdd(final_df)


if __name__ == '__main__':
    main()
