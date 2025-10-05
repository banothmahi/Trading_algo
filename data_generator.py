import numpy as np
import pandas as pd
from datetime import datetime

def generate_synthetic_data(n=400, seed=42):
    np.random.seed(seed)
    dates = pd.date_range(end=datetime.now().date(), periods=n, freq='D')
    t = np.arange(n)
    price = 100 + 0.2 * t + 5 * np.sin(0.06 * t) + np.random.normal(scale=1.5, size=n)
    df = pd.DataFrame({'date': dates, 'close': price}).set_index('date')
    return df
