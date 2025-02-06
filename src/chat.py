import requests
import os
import logging
from openai import OpenAI

class Chat():

    def __init__(self, api_key:str=None, api_url:str=None, chat_model:str=None):
        self.__api_key = api_key or os.getenv("API_KEY")
        self.__api_url = api_url or os.getenv("API_URL")
        self.chat_model = chat_model or "gpt-4o-mini"

    def response(self, message:str)->str:
        headers = {
            'Authorization': f'Bearer {self.__api_key}',
            'Content-Type': 'application/json'
        }

        messages = []
        if self.chat_model != "o1-mini" or "o1":
            messages.append({
                "role":"system",
                "content":"請以繁體中文回答"
            })

            messages.append({
                "role":"user",
                "content":message
            })

            data = {
                "model": self.chat_model,
                "messages": messages
            }

            response = requests.post(url=self.__api_url, headers=headers, json=data)
            if response.status_code == 200:
                response_data = response.json()
                response = response_data['choices'][0]['message']['content']
                self.__gpt_logger(self.chat_model,prompt=message,response=response,usage=response_data["usage"])
                return response
            else:
                logging.error(f"Error: {response.status_code}_{response.text}")
                return "Error:",response.status_code,response.text
    
    def vector_response(self, term:list)->list:
        client = OpenAI(api_key=self.__api_key)
        model = "text-embedding-3-small"
        print(term)
        respones = client.embeddings.create(
            model=model,
            input=term,
        )

        return respones.data[0].embedding
    
    def __gpt_logger(self,model:str, prompt:str, response:str, usage:list=None):
        logging.info(f"Use Model: {model}")
        logging.info(f"Prompt string: {prompt}")
        logging.info(f"Response data: {response}")
        logging.info(f"Usage:{usage}")

