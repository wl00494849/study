from src.integration import Data_Integration
from src.report_script import Verify_Script
from src.integration_copy import Data_Integration as Data_Integration1
from dotenv import load_dotenv
import os
load_dotenv()

def run_script(filePath1:str,filePath2:str,model:str,prompt:str,isCoT:bool,savePath:str="test"):
    total_token=0
    total_error=0
    fail=0
    path=f"report/{savePath}"
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    for i in range(10):
        a = Data_Integration(filePath1=filePath1, filePath2=filePath2,saveName=f"{path}/test{i}",model=model)

        if isCoT:
            a.do(prompt)
        else:
            a.do_no_CoT(prompt)

        if a.fail:
            fail += 1
            
        total_token += a.total_tokens
        total_error += a.total_error

    avg_token= total_token//10

    with open(f"{path}/report.txt", 'a', encoding='utf-8') as f:
        f.write(f"total_token={total_token}\n")
        f.write(f"total_error={total_error}\n")    
        f.write(f"avg_token={avg_token}\n")

def run_script1(filePath1:str,filePath2:str,filePath3:str,model:str,prompt:str,isCoT:bool,savePath:str="test"):
    total_token=0
    total_error=0
    fail=0
    path=f"report/{savePath}"
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    for i in range(10):
        a = Data_Integration1(filePath1=filePath1, filePath2=filePath2,filePath3=filePath3,saveName=f"{path}/test{i}",model=model)

        if isCoT:
            a.do(prompt)
        else:
            a.do_no_CoT(prompt)

        if a.fail:
            fail += 1
            
        total_token += a.total_tokens
        total_error += a.total_error

    avg_token= total_token//10

    with open(f"{path}/report.txt", 'a', encoding='utf-8') as f:
        f.write(f"total_token={total_token}\n")
        f.write(f"total_error={total_error}\n")    
        f.write(f"avg_token={avg_token}\n")

def run_report(savePath:str):
    
    vs = Verify_Script(f"{savePath}/gold.csv")
    fail = 0
    for i in range(10):
        filePath=f"{savePath}/test{i}.csv"
        if os.path.exists(filePath):
            vs.run(filePath)
            print("========================================================")
        else:
            fail += 1
    schema_coverage = vs.total_schema_coverage//(10-fail)
    accuracy = vs.total_accuracy//(10-fail)

    with open(f"{savePath}/indicators_report.txt", 'w', encoding='utf-8') as f:
        f.write(f"總Schema_Coverage:{schema_coverage}%\n")   
        f.write(f"總Accuracy:{accuracy}%\n") 
        
    print(f"總Schema_Coverage:{schema_coverage}%")
    print(f"總Accuracy:{accuracy}%")
