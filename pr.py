import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# === 取得真值與預測 ===
gold = pd.read_csv('report/聯發科CoT-4.1-mini/gold.csv')      # 含全部欄位
pred  = pd.read_csv('report/聯發科CoT-4.1-mini/test1.csv')     # 含全部欄位

# === 把 pred 裡的所有列組成元組集合 ===
pred_set = set(map(tuple, pred.values))
gold_set = set(map(tuple,gold.values))

y_true = [1] * len(gold_set)                         
y_pred_for_gold = [1 if p in pred_set else 0 for p in gold_set]

extra_preds = pred_set - gold_set
y_pred_for_extra = [1] * len(extra_preds)

y_pred_total = y_pred_for_gold + y_pred_for_extra
y_true_total = [1] * len(gold_set) + [0] * len(extra_preds)

P = precision_score(y_true_total, y_pred_total)
R = recall_score(y_true_total, y_pred_total)
F1 = f1_score(y_true_total, y_pred_total)

print(f'Precision={P:.2%}, Recall={R:.2%}, F1={F1:.2%}')