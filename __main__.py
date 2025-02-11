from src.chat import Chat
from datetime import datetime
from dotenv import load_dotenv
from src.analyze import Analyze
from openai import OpenAI
import os
import src.prompt as pt
import src.extract as et 
import logging
import numpy as np
import ast

now = datetime.now()
logging.basicConfig(filename=f'log/{now.year}_{now.month}_{now.day}_test.log', level=logging.INFO)
load_dotenv()

def main():
    aly = Analyze()
    li = aly.strip_address("新竹科學園區新竹市力行六路8號")
    print(li)

if __name__ == "__main__":
    main()

        