import os
import logging
from openai import OpenAI

class Chat():

    def __init__(self, api_key:str=None, api_url:str=None, chat_model:str=None):
        self.__api_key = api_key or os.getenv("API_KEY")
        self.__api_url = api_url or os.getenv("API_URL")
        self.chat_model = chat_model or "gpt-4o-mini"
        self.client = OpenAI(api_key=self.__api_key)

    def response(self, prompt:str)->str:
        messages = []
        if self.chat_model != "o1-mini" or "o1":
            messages.append(
                {
                    "role": "system",
                    "content": "請以繁體中文回答"
                }
            )
        
        respones = self.client.chat.completions.create(
            model=self.chat_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        self.__gpt_logger(model=self.chat_model, prompt=prompt, response=respones.choices[0].message.content, usage=respones.usage)
        return respones.choices[0].message.content

    ## size = 0 -> small, size = 1 -> large
    def get_vector(self, term:list,size:int=0)->list:
        model = "text-embedding-3-small"
        if size > 0:
            model = "text-embedding-3-large"
        print(term)
        respones = self.client.embeddings.create(
            model=model,
            input=term,
        )
        self.__gpt_logger(model=model, prompt=term, usage=respones.usage)
        return respones.data
    
    def __gpt_logger(self,model:str=None, prompt:[str,list]=None, response:str=None, usage:list=None):
        logging.info(f"Use Model: {model}")
        logging.info(f"Prompt string: {prompt}")
        logging.info(f"Response data: {response}")
        logging.info(f"Usage:{usage}")

