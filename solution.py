import pandas as pd
import numpy as np

chat_id = 944932368

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    b_min = np.min(x) / (1 - alpha)
    b_max = np.max(x) / (1 - alpha)
    return b_min, b_max
