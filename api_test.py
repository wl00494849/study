import requests
from src.chat import Chat
from src.search import search_file
from src.similarity import get_cosine_similarity
from dotenv import load_dotenv
import logging
from datetime import datetime


def help():
    print("press h check help")
    print("press q quit process")
    print("press d search open data")
    print("press s get cos similarty")

def main():
    now = datetime.now()
    logging.basicConfig(filename=f'log/{now.year}_{now.month}_{now.day}_test.log', level=logging.INFO)
    load_dotenv()

    model_setting = input("Setting your model：")
    if len(model_setting) != 0:
        chat_model = model_setting
        client = Chat(chat_model=chat_model)
        logging.info(f"Chat model set to: {chat_model}")
    else:
        client = Chat()
        logging.info("Chat model set to: gpt-4o-mini")

    while 1:
        message = input("Input your question：")
        print("========================================")
        match message:
            case "h":
                help()
            case "q":
                logging.info("Quitting the process")
                break
            case "d":
                break
                # key = input("請輸入要搜尋的開放資料名稱:")
                # search_file(keyword=key,top=15)
            case "s":
                term1 = input("請輸入要比較的詞1:")
                term2 = input("請輸入要比較的詞2:")
                print(get_cosine_similarity(term1,term2,1))
            case _:
                response = client.response(message)   
                print(response)
                print("========================================")



print("========================================")
help()
print("========================================")

if __name__ == "__main__":
    main()