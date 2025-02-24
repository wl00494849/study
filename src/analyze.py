import src.prompt as prompt
from src.chat import Chat
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import logging



class Analyze:
    def __init__(self):
        self.client = Chat()
        
    def analyze_fileName(self,fileName1:str,fileName2:str)->str:
        str = prompt.st_analysis_ByFileName(fileName1,fileName2)
        res = self.client.response(str) 
        return res

    def get_cosine_similarity(self,term1:str,term2:str,size:int=0)->float:
        logging.info(f"term1:{term1},term2:{term2}")
        response1 = self.client.get_vector(term1,size)
        response2 = self.client.get_vector(term2,size)

        di1 = np.array([response1[0].embedding]).reshape(1, -1)
        di2 = np.array([response2[0].embedding]).reshape(1, -1)
        
        cos = cosine_similarity(di1,di2)
        logging.info(f"cosine_similarity:{cos}")
        return cos

    def strip_address(self,address:str)->list:
        str = prompt.st_analysis_address(address)
        res = self.client.response(str)
        print(res)
        li = res.split("\n")
        print(li)
        p = li[0].lstrip("[").rstrip().rstrip("]").split(",")
        print(p)
        v = li[1].lstrip("[").rstrip("]").split(",")       
        return [p,v]