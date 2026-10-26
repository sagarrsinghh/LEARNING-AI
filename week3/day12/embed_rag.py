import os

import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")

text1 = "There are 24 paid leaves."
text2 = "Cat is a wild animal."

v1 = model.encode(text1)
v2 = model.encode(text2)
print(cosine_similarity(v1, v2))
