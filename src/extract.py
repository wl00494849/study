import pandas as pd

## list[0] = col , list[1] = row
def extract_by_csv(file_name:str)->list:
    mData = list()
    df = pd.read_csv(f"data/{file_name}.csv")
    mData.append(df.columns.to_list())
    mData.append(df.head(10).values.tolist())
    return mData

def extract_by_DF(df:pd.DataFrame)->list:
    mData = list()
    mData.append(df.columns.to_list())
    mData.append(df.head(10).values.tolist())
    return mData