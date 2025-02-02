import requests
from src.chat import Chat
from dotenv import load_dotenv

def help():
    print("press h check help")
    print("press q quit process")

def main():
    load_dotenv()
    model_setting = input("Setting your model：")
    if len(model_setting) != 0:
        chat_model = model_setting
        client = Chat(chat_model=chat_model)
    else:
        client = Chat()

    while 1:
        message = input("Input your question：")
        print("========================================")
        match message:
            case "h":
                help()
            case "q":
                break
            case _:
                response = client.response(message)   
                print(response)
                print("========================================")

print("========================================")
help()
print("========================================")
main() 