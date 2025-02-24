import pandas as pd
import requests
import os
from datetime import datetime

time = datetime.now()
fileName = f"dataset/OpenDataSet_{time.year}_{time.month}_{time.day}.csv"
domain_Url = 'https://data.gov.tw/api/front/dataset/export?format=csv'

def get_dataset():
    if not os.path.exists(fileName):
        response = requests.get(domain_Url)
        with open(fileName, 'wb') as f:
            f.write(response.content)
    
    # df = pd.read_csv(fileName)
    # s = '盤後資訊'
    # seek = df[df.資料集名稱.str.contains(s,na=False)]
    # seek.to_csv('data/seek.csv',index=False)
    
get_dataset()