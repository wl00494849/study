import src.prompt as prompt
from src.chat import Chat
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

client = Chat()
def analyze_fileName(fileName1:str,fileName2:str):
    str = prompt.st_analysis_ByFileName(fileName1,fileName2)
    res = client.response(str) 
    return res

def get_cosine_similarity(term1:str,term2:str):
    response1 = client.vector_response(term1)
    response2 = client.vector_response(term2)

    response1 = np.array([response1])
    response2 = np.array([response2])
    
    response1 = response1.reshape(1, -1)
    response2 = response2.reshape(1, -1)

    return cosine_similarity(response1,response2)