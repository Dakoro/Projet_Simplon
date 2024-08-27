import os
import re
# import cv2
import pathlib
import pickle
# import base64
# import fitz
import numpy as np
from nltk.corpus import stopwords

ROOT_DIR = pathlib.Path(os.getcwd()).parent
DOCS_DIR = os.path.join(ROOT_DIR, 'pdfs', 'chunks')
STW = stopwords.words('english') + ['that', 'this', 'with', 'only']

def load_docs(path):
    list_docs = sorted(
        [os.path.join(DOCS_DIR, fn) for fn in os.listdir(DOCS_DIR) if fn.endswith('.pkl')],
        key=lambda x: int(re.sub('\D', '', x)))
    def open_doc(path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
    docs = []
    for fp in list_docs:
        data = open_doc(fp)
        docs += data
    return docs


def clean_text(text: str):
    text = re.sub('\n', '', text).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'http[s]?://\S+', '', text)
    tokens = [tok for tok in text.split() if tok.strip() not in STW]
    tokens = [tok for tok in tokens if len(tok) > 3]
    return " ".join(tokens)


# def get_coord(docs):
#     coord_dict = {}
#     print(docs)
#     for idx, doc in enumerate(docs, start=1):
#         bbox = doc['metadata']['bboxes']
#         title = doc['metadata']['paper_title']
#         file_path = doc['metadata']['file_path']
#         bbox = eval(bbox)
#         coord = {"page": 0, "bbox": []}
#         for lst in bbox:
#             page = lst[0]['page']
#             coord["page"] = page
#             for item in lst:
#                 x = float(item['x']) 
#                 y = float(item['y']) 
#                 h = float(item['h']) 
#                 w = float(item['w'])
#                 coord['bbox'].append((x, y, x+h, y+w))
#         x_min = min([v[0] for v in coord['bbox']])
#         y_min = min([v[1] for v in coord['bbox']])
#         x_max = max([v[2] for v in coord['bbox']])
#         y_max = max([v[3] for v in coord['bbox']])
#         coord_dict[f'doc_{idx}'] = {'page': int(coord['page']),
#                                     'title': title,
#                                     "file_path": file_path,
#                                     "bbox": (x_min, y_min, x_max, y_max)}
#     return coord_dict


# def pix2np(pix):
#     im = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
#     im = np.ascontiguousarray(im[..., [2, 1, 0]])  # rgb to bgr
#     return im


# def ndarray_to_b64(ndarray):
#     """
#     converts a np ndarray to a b64 string readable by html-img tags 
#     """
#     img = cv2.cvtColor(ndarray, cv2.COLOR_RGB2BGR)
#     _, buffer = cv2.imencode('.png', img)
#     return base64.b64encode(buffer).decode('utf-8')


# def find_para_in_pdf(path, page_number, bbox):
#     doc = fitz.open(path)
#     page = doc[page_number-1]
#     rect = fitz.Rect(bbox)
#     page.draw_rect(rect=rect, color = (0, 1, 0), width = 2)
#     pix = page.get_pixmap(dpi=200)
#     return pix
#     # pix.pil_save('test_bbox_fitz.png')

# def get_images(coord_dict):
#     def get_pdf_url(file_path):
#         filename = os.path.split(file_path)[-1]
#         filename = re.sub('_', '/', filename)
#         pdf_url = f"https://arxiv.org/pdf/{filename}"
#         return pdf_url
    
#     images = []
#     for key, value in coord_dict.items():
#         print(value)
#         file_path = value['file_path']
#         pdf_url = get_pdf_url(file_path)
#         title = value['title']
#         page_number = value['page']
#         bbox = value['bbox']
#         pix = find_para_in_pdf(file_path, page_number, bbox)
#         img = pix2np(pix)
#         base64_img = ndarray_to_b64(img)
#         images.append((pdf_url, title, base64_img))
#     return images


def get_rag_score(logprobs):
    scores = []
    for logprob in logprobs:
        print(logprob)
        scores.append(np.round(np.exp(logprob['logprob'])*100,2))
    return np.mean(scores)

    