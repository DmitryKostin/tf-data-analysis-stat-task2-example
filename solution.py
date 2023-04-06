import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 944932368

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    x_bar = np.mean(x)
    s = np.std(x, ddof=1)
    t_alpha = np.abs(t.ppf(alpha/2, n-1))
    lower = x_bar - t_alpha*s/np.sqrt(n)
    upper = x_bar + (1-t_alpha)*s/np.sqrt(n)
    return lower, upper
