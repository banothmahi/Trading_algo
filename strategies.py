import numpy as np

def sma(series, window):
    return series.rolling(window=window).mean()

def rsi(series, window=14):
    delta = series.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.rolling(window=window).mean()
    ma_down = down.rolling(window=window).mean()
    rs = ma_up / ma_down
    return 100 - (100 / (1 + rs))

def apply_sma_strategy(df):
    df['sma_short'] = sma(df['close'], 20)
    df['sma_long'] = sma(df['close'], 50)
    df['sma_signal'] = 0
    df['sma_signal'][20:] = np.where(df['sma_short'][20:] > df['sma_long'][20:], 1, 0)
    df['sma_signal'] = df['sma_signal'].diff()
    return df

def apply_rsi_strategy(df):
    df['rsi'] = rsi(df['close'])
    df['rsi_signal'] = np.where(df['rsi'] < 30, 1, np.where(df['rsi'] > 70, -1, 0))
    return df
