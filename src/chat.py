import requests
import os
import logging

class Chat():

    def __init__(self, api_key:str=None, api_url:str=None, chat_model:str=None):
        self.api_key = api_key or os.getenv("API_KEY")
        self.api_url = api_url or os.getenv("API_URL")
        self.chat_model = chat_model or "gpt-4o-mini"
        print(f"Using model: {self.chat_model}")

    def response(self, message:str)->str:
        headers = {
            'Authorization': f'Bearer {self.api_key}',
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

            response = requests.post(url=self.api_url, headers=headers, json=data)
            if response.status_code == 200:
                response_data = response.json()
                return response_data['choices'][0]['message']['content']
            else:
                logging.error(f"Error: {response.status_code}_{response.text}")
                return "Error:",response.status_code,response.text

