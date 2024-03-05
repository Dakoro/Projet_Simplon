import re
import string
import os
import pandas as pd
from bs4 import BeautifulSoup
from bs4.element import Tag


def rm_new_line(text: str) -> str:
    res = re.sub(r'[^\w\s]', '', text)
    return " ".join(res.split()[:-2])


def parse_title(title_tag: Tag) -> str:
    tag_split = title_tag.string.split()
    title = ' '.join(tag_split[1:])
    return title


def extract_year(year_string: str):
    pattern = "\d\d\d\d"
    return re.findall(pattern, year_string)[-1]


def main():
    path = os.path.join(os.getcwd(), "data_source/doc_scraping.html")
    with open(path, 'r', encoding='utf-8') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, features="html.parser")
    title = soup.find('title')
    arxiv_id = title.text.split()[0][1:-1]

    abstract_tag = soup.find("div", {"class": "ltx_abstract"})
    abstract = abstract_tag.find("p").string

    date_tag = soup.find("div", {"id": "watermark-tr"})
    year = extract_year(date_tag.string)

    author_tag = soup.find("span", {"class": "ltx_personname"})
    author = rm_new_line(author_tag.text)

    df = pd.DataFrame({
        "arxiv_id": [arxiv_id],
        "title": [parse_title(title)],
        "year": [year],
        "author": [author],
        "abstract": [abstract]
    })
    print(df)


if __name__ == '__main__':
    main()
