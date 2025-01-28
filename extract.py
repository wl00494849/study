import pandas as pd

## list[0] = col , list[1] = row
def extract_col_csv(file_name:str)->list:
    mData = list()
    df = pd.read_csv(file_name)
    mData.append(df.columns.to_list())
    mData.append(list(df[mData[0][0]].values))
    return mData
