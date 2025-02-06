from src.chat import Chat
from datetime import datetime
from dotenv import load_dotenv
from src.analyze import Analyze
from openai import OpenAI
import os
import src.prompt as pt
import src.extract as et 
import logging

now = datetime.now()
logging.basicConfig(filename=f'log/{now.year}_{now.month}_{now.day}_test.log', level=logging.INFO)
load_dotenv()
# client = Chat() 

def main():
    
    # fileName1 = input("Input fileName 1:")
    # fileName2 = input("Input fileName 2:")
    # list1 = et.extract_col_csv("112年國道每月營業額.csv")
    # list2 = et.extract_col_csv("113年國道每月營業額.csv")

    # prompt_str = pt.st_analysis_ByFileName("112年國道每月營業額.csv","113年國道每月營業額.csv")
    # response = client.response(prompt_str)
    # print(response)

    # aly = Analyze()
    # print(aly.get_cosine_similarity("1月","一月"))
    client = OpenAI(api_key=os.getenv("API_KEY"))
    prompt = input("Input your question：")
    response = client.chat.completions.create(
        model="o3-mini",
        reasoning_effort="low",
        messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
        )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()

        