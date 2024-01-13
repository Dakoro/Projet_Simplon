import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from utils import load_arxiv_dataset, format_arxiv_dataset, load_nips_dataset
load_dotenv()

BDD_URI = os.getenv('BDD_URI')
ENGINE_URI = f'sqlite:///{BDD_URI}'


def main():
    engine = create_engine(ENGINE_URI, echo=True)
    queries = [
        'SELECT id, name FROM Author;',
        'SELECT id, title FROM Paper;'
    ]

    with engine.connect() as conn:
        result_0 = conn.execute(text(queries[0]))
        result_1 = conn.execute(text(queries[1]))
        authors = result_0.all()
        papers = result_1.all()

    df_authors = pd.DataFrame({
        'author_id': [v[0] for v in authors],
        'name': [v[1] for v in authors]
    })

    df_papers = pd.DataFrame({
        'paper_id': [v[0] for v in papers],
        'title': [v[1] for v in papers]
    })

    df_arxiv = load_arxiv_dataset()
    df_arxiv = format_arxiv_dataset(df_arxiv)
    df_arxiv = df_arxiv[['authors', 'title']].explode(column='authors')
    df_arxiv = df_arxiv.rename(columns={"authors": "name"})
    df_arxiv['name'] = df_arxiv['name'].str.lower()

    df_nips = load_nips_dataset()
    df_nips = df_nips[['name', 'title']]
    df_nips['name'] = df_nips['name'].str.lower()
    df_concat = pd.concat([df_arxiv, df_nips]).drop_duplicates()

    df_paper_merge = df_papers.merge(df_concat, on='title')
    df_final = df_paper_merge.merge(
        df_authors,
        on='name')[['paper_id', 'author_id']]

    df_final.to_sql('Author_Paper', engine, if_exists='append', index=False)


if __name__ == '__main__':
    main()
