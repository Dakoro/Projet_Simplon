import re
from bs4 import BeautifulSoup
from bs4.element import Tag


def rm_new_line(text: str) -> str:
    return re.sub('\n', " ", text)


def parse_title(title_tag: Tag) -> str:
    tag_split = title_tag.string.split()
    title = ' '.join(tag_split[1:])
    return title


def extract_year(year_string: str):
    pattern = re.compile('\d\d\d\d')
    return pattern.findall(year_string)[0]


def main():
    path = '/home/dakoro/project_complement/data_source/[1910.06709] A Simple Proof of the Quadratic Formula.html'
    with open(path, 'r', encoding='utf-8') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, features="html.parser")
    title = soup.find('title')

    abstract_tag = soup.find_all("p", {"id": "id3.id1"})[0]
    abstract = abstract_tag.string

    date_tag = soup.find("div", class_="ltx_dates")
    year = extract_year(date_tag.string)

    author_tag = soup.find("span", class_="ltx_personname")

    data = {
        "title": parse_title(title),
        "year": year,
        "author": rm_new_line(author_tag.string),
        "abstract": abstract
    }

    print(data)


if __name__ == '__main__':
    main()
