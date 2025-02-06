from src.chat import Chat
from datetime import datetime
from dotenv import load_dotenv
from src.analyze import get_cosine_similarity
import src.prompt as pt
import src.extract as et 
import logging

now = datetime.now()
logging.basicConfig(filename=f'log/{now.year}_{now.month}_{now.day}_test.log', level=logging.INFO)
load_dotenv()
client = Chat() 

def main():
    
    # fileName1 = input("Input fileName 1:")
    # fileName2 = input("Input fileName 2:")
    # list1 = et.extract_col_csv("112年國道每月營業額.csv")
    # list2 = et.extract_col_csv("113年國道每月營業額.csv")

    # prompt_str = pt.st_analysis_ByFileName("112年國道每月營業額.csv","113年國道每月營業額.csv")
    # response = client.response(prompt_str)
    # print(response)

    print(get_cosine_similarity("地址","縣市"))

if __name__ == "__main__":
    main()

        