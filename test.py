import requests
from src.chat import Chat
from src.analyze import Analyze
from dotenv import load_dotenv
import logging
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import pandas as pd
import numpy as np

def test():
    gpt = Chat()
    aly = Analyze()
    # df = pd.read_csv("dataset/OpenDataSet_2025_2_24.csv")
    # dataName = df['資料集名稱'].values
    ## dataName len = 52201
    ## MAX_TOKENS = 8192

    # new_df = pd.DataFrame(li, columns=['dataset_Name','dimension'])
    # new_df.to_csv('dataset/dataset_dimension.csv', index=False)
    
    # df = pd.read_csv("dataset/dataset_dimension.csv")
    # t = df.iloc[3,0]
    # print(t)

    # di1 = np.array([float(x) for x in df.iloc[3,1].strip('[]').split(',')]).reshape(1, -1)
    # di2 = np.array([float(x) for x in df.iloc[6,1].strip('[]').split(',')]).reshape(1, -1)

    # cos = cosine_similarity(di1,di2)
    # print(cos)

    # res = gpt.vector_response("有線廣播電視事業發展基金附屬單位決算")
    # print(res[0].embedding)
    # cos = aly.get_cosine_similarity("地址","address")
    # print(cos)
    
    gpt.get_vector(["地址","住址","地點"])

test()