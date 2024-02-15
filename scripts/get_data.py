import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

BDD_URI = os.getenv('BDD_URI')
ENGINE_URI = f'sqlite:///{BDD_URI}'


def main():
    engine = create_engine(ENGINE_URI, echo=True)
    query = """
    SELECT
        paper_id,
        name,
        article_count,
        year,
        title,
        categories,
        abstract
    FROM Author_Paper as ap
        JOIN Author as a ON ap.author_id = a.id
        JOIN Paper as p ON ap.paper_id = p.id;
    """

    data_df = {}
    cols = [
        "paper_id",
        "name",
        "article_count",
        "year",
        "title",
        "categories",
        "abstract"
    ]

    with engine.connect() as conn:
        result = conn.execute(text(query))
        data = result.all()
    for i, col in zip(range(len(data[0])), cols):
        list_row = [row[i] for row in data]
        data_df[col] = list_row

    df = pd.DataFrame.from_dict(data_df)
    df.to_csv('aggreated_data.csv', index=False)


if __name__ == '__main__':
    main()
