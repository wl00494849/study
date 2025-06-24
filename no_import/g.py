import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_list/OpenDataSet_2025_3_24.csv")

df["檔案格式"] = df["檔案格式"].str.split(";")  
df_exploded = df.explode("檔案格式")            
counts = df_exploded["檔案格式"].value_counts() 

print(counts)

data = {
    "檔案格式": ["CSV", "ZIP", "JSON", "XML", "WEBSERVICES"],
    "數量": [89614, 50809, 33756, 23265, 4111]
}

df = pd.DataFrame(data)

total = sum(df["數量"])
df["百分比"] = df["數量"] / total * 100

# 畫圖
plt.rcParams['font.family'] = 'Heiti TC'
plt.figure(figsize=(8, 5))
# plt.bar(df["檔案格式"], df["數量"], color='skyblue', width=0.5)
# plt.title("前五名檔案格式數量")

plt.bar(df["檔案格式"], df["百分比"], color='skyblue', width=0.5)
plt.title("2025-3-24 前五名檔案格式百分比")

plt.ylim(0, df["百分比"].max() + 5)
plt.xlabel("檔案格式")
plt.ylabel("百分比")


# for i, v in enumerate(df["數量"]):
#     plt.text(i, v + 1000, str(v), ha='center')

for i, v in enumerate(df["百分比"]):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center')

plt.tight_layout()
plt.show()
# v = df["檔案格式"]
# print(v)
# for i in v:
#     data = i.split(";")
#     for j in data:
        