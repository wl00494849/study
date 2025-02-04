import src.extract as et 
from src.chat import Chat

def main():
    client = Chat()
    
    fileName1 = input("Input fileName 1:")
    fileName2 = input("Input fileName 2:")
    list1 = et.extract_col_csv(fileName1)
    list2 = et.extract_col_csv(fileName2)



        