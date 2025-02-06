def st_analysis_ByFileName(fileName1:str,fileName2:str)->str:
    return f"fileName1:{fileName1},fileName2:{fileName2}。這兩筆檔案名稱適合時間分析，還是空間分析？\n是時間分析的話只回答我time,空間分回答我space,兩個都行回答我time,space,都沒有的話給我None"

def st_analysis_ByFieldName(field1:list,field2:list)->str:
    return f"File1 row:{field1[0]},col:{field2[1]}\nFile2 row:{field2[0]},col:{field2[1]}\n這兩筆資料的欄位名稱有哪些適合合併的？請只給我適合合併欄位名稱就好。並以空格區隔"
