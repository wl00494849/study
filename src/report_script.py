from sklearn.metrics.pairwise import cosine_similarity
from src.chat import Chat
from src.similarity import calcute_cos
from pathlib import Path
import pandas as pd
import numpy as np


class Verify_Script:
    def __init__(self,gold_filePath:str):
        self.gold_df = pd.read_csv(gold_filePath)
        self.client = Chat()
        self.total_schema_coverage = 0.0
        self.total_accuracy = 0.0

    def run(self,filePath:str):
        self.schema_coverage(filePath)
        self.cell_accuracy(filePath)
    
    def schema_coverage(self,filePath:str):
        pred = pd.read_csv(filePath)

        gold_col = self.gold_df.columns.to_list()
        pred_col = pred.columns.to_list()

        gold_len = len(gold_col)
        schema_equal = 0

        # 交集
        intersection = set(gold_col) & set(pred_col)
        schema_coverage = len(intersection)/gold_len*100

        self.total_schema_coverage += schema_coverage

        print(f"schema_coverage:{schema_coverage}%")
        

    def cell_accuracy(self,filePath:str):

        pred = pd.read_csv(filePath)
        gold = self.gold_df.copy()

        pred = pred.reindex(columns=gold.columns, fill_value="x")

        min_rows = min(gold.shape[0], pred.shape[0])
        min_cols = min(gold.shape[1], pred.shape[1])

        arr1 = gold.iloc[:min_rows, :min_cols].to_numpy()
        arr2 = pred.iloc[:min_rows, :min_cols].to_numpy()

        comparison = arr1 == arr2
        num_diff = (comparison == False).sum()

        record_path = str(Path(filePath).parent) + "/" + Path(filePath).stem

        with open(f"{record_path}_diffs.txt", 'w', encoding='utf-8') as f:
            diff_indices = np.where(arr1 != arr2)
            for row, col in zip(*diff_indices):
                f.write(f"Row {row}, Column '{gold.columns[col]}': gold = {arr1[row, col]}, test = {arr2[row, col]}\n")

        print(min_rows*min_cols)
        total_cell = self.gold_df.size
        equal_cell = total_cell - num_diff
        cell_accuracy= equal_cell/total_cell*100

        self.total_accuracy += cell_accuracy

        print(f"Cell_Accuracy:{cell_accuracy}%")
        print(f"總格數：{total_cell}")
        print(f"不一致格數：{num_diff}")
        print("=========================================================================")