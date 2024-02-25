import arxiv
import pandas as pd


def main():
    arxiv_client = arxiv.Client()
    arxiv_search = arxiv.Search(
        query='quantum',
        max_results=10,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = {
        "arxiv_id": [],
        "title": [],
        "year": [],
        "authors": [],
        "categories": [],
        "abstract": []
    }

    for result in arxiv_client.results(arxiv_search):
        results['arxiv_id'].append(result.entry_id.split('/')[-1])
        results['title'].append(result.title)
        results['year'].append(result.published)
        results['authors'].append(", ".join([str(a) for a in result.authors]))
        results["categories"].append(result.primary_category)
        results['abstract'].append(result.summary)

    df = pd.DataFrame.from_dict(results)
    df.to_csv('arxiv_api.csv')


if __name__ == '__main__':
    main()
