import arxiv
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def main():
    arxiv_client = arxiv.Client()
    arxiv_search = arxiv.Search(
        query='quantum',
        max_results=10,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = {
        "title": [],
        "authors": [],
        "abstract": []
    }

    for result in arxiv_client.results(arxiv_search):
        results['title'].append(result.title)
        results['authors'].append(", ".join([str(a) for a in result.authors]))
        results['abstract'].append(result.summary)

    df = pd.DataFrame.from_dict(results)


if __name__ == '__main__':
    main()
