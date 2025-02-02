import extract
import prompt
from chat import Chat

chat = Chat(chat_model="gpt-4o")
def analyze_fileName(fileName1:str,fileName2:str):
    str = prompt.st_analysis_ByFileName(fileName1,fileName2)
    res = chat.response(str) 
    return res