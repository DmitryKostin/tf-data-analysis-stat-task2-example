import pandas as pd
import numpy as np

chat_id = 944932368

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return x.mean() - np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)), x.mean() - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x))
