import os
import re
import arxiv
import pandas as pd
import numpy as np

ROOT_DIR = os.getcwd()
PDF_DIR = os.path.join(ROOT_DIR, 'pdfs')
SAMPLE_PATH = os.path.join(ROOT_DIR, 'files', 'pkl', 'sample.pkl')


def main():
    df = pd.read_pickle(SAMPLE_PATH)
    arxiv_ids = df['arxiv_id'].to_list()
    
    list_names = []
    for idx in arxiv_ids:
        if isinstance(idx, str):
            if '/' in idx:
                list_names.append(re.sub('/', '_', idx))
            else:
                list_names.append(idx)
        else:
            list_names.append(np.nan)
    
    client = arxiv.Client()
    for name, ids in zip(list_names, arxiv_ids):
        if name != np.nan:
            fn = os.path.join(PDF_DIR, f"{name}.pdf")
            if not os.path.exists(fn):
                try:
                    paper = next(client.results(arxiv.Search(id_list=[ids])))
                    paper.download_pdf(dirpath=PDF_DIR, filename=f"{name}.pdf")
                    print(f"{fn} done")
                except Exception as e:
                    print(e)
                    continue


if __name__ == "__main__":
    main()