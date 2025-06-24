from sklearn.metrics.pairwise import cosine_similarity
from src.chat import Chat
from src.similarity import calcute_cos
from src.report_script import Verify_Script
from src.auto_script import run_report
from pathlib import Path
import os
import pandas as pd
import numpy as np


def main():
    savePath="report/iTaiwanNoCoT-4o-mini"
    run_report(savePath)

main()