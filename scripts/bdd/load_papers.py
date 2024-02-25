import os
import logging as log
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from utils import (
    load_arxiv_papers,
    format_arxiv_papers,
    load_nips_papers,
    request_arxiv,
    get_scraping,
    get_mongo,
    )

load_dotenv()

BDD_URI = os.getenv('BDD_URI')
ENGINE_URI = f'sqlite:///{BDD_URI}'


def main():
    log.basicConfig(
        filename='logs/load_bdd.log',
        encoding='utf-8',
        level=log.DEBUG)

    df_arxiv = load_arxiv_papers()
    df_arxiv_formated = format_arxiv_papers(df_arxiv)

    df_nips = load_nips_papers()
    df_nips_wna = df_nips[df_nips['abstract'] != 'Abstract Missing']

    df_arxiv_api = request_arxiv()
    df_scraping = get_scraping()
    df_mongo = get_mongo()

    dfs = [
        df_arxiv_formated,
        df_nips_wna,
        df_arxiv_api,
        df_scraping,
        df_mongo
    ]

    df_concat = pd.concat(dfs)
    df_concat = df_concat.drop_duplicates('title')

    engine = create_engine(ENGINE_URI, echo=True)
    with engine.connect() as conn:
        try:
            df_concat.to_sql('Paper', conn, if_exists='append', index=False)
            log.info('Paper table loaded')
        except Exception as err:
            log.debug(err)
            log.warning('Loading Failed')
            log.error(err)


if __name__ == '__main__':
    main()
