import requests
from src.chat import Chat
from src.analyze import Analyze
from dotenv import load_dotenv

def help():
    print("press h check help")
    print("press q quit process")
    print("press g use gpt")

def main():
    load_dotenv()
    model_setting = input("Setting your model：")
    aly = Analyze()
    if len(model_setting) != 0:
        chat_model = model_setting
        client = Chat(chat_model=chat_model)
    else:
        client = Chat()

    while 1:
        cmd = input("Input your command：")
        print("========================================")
        match cmd:
            case "h":
                help()
            case "q":
                break
            case "g":
                message = input("Input your question：")
                response = client.response(message)   
                print(response)
            case "s":
                term1 = input("Input term1:")
                term2 = input("Input term2:")
                print(aly.get_cosine_similarity(term1,term2))
            case _:
                print("Input error")
            
        print("========================================")

print("========================================")
help()
print("========================================")
main() 