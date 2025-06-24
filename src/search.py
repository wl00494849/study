from src.chat import Chat
from src.heap import max_heap,kv
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import logging

print("Loading Model.....")
df = pd.read_csv("dataset_list/dataset_dimension_large.csv")
print("Compelet.....")

def search_file(keyword:str,top:int=15):
    gpt = Chat()
    heap = max_heap()
    exist = df['dimension'][df['dataset_Name'].isin([keyword])]
    if len(exist) == 0:
        target = gpt.get_vector(keyword,1)[0].embedding
        target = np.array(target).reshape(1, -1)
    else:
        target = np.array([float(x) for x in exist.values[0].strip('[]').split(',')]).reshape(1, -1)
    
    for item in df.values:
        if keyword != item[0]:
            di = np.array([float(x) for x in item[1].strip('[]').split(',')]).reshape(1, -1)
            cos = cosine_similarity(target,di)
            heap.push(kv(item[0],cos))
    
    for i in range(top):
        p = heap.pop()
        print(f"{p.k}:{p.v[0]}")
