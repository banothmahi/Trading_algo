from data_generator import generate_synthetic_data
from strategies import apply_sma_strategy, apply_rsi_strategy
from backtester import backtest_signals
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

df = generate_synthetic_data()
df = apply_sma_strategy(df)
df = apply_rsi_strategy(df)

trades_sma, equity_sma, metrics_sma = backtest_signals(df, 'sma_signal')
trades_rsi, equity_rsi, metrics_rsi = backtest_signals(df, 'rsi_signal')

os.makedirs("output", exist_ok=True)
pdf_path = "output/Algo_Trading_Assignment_Output.pdf"

with PdfPages(pdf_path) as pdf:
    plt.figure(figsize=(10,5))
    plt.plot(df.index, df['close'], label='Close')
    plt.plot(df['sma_short'], label='SMA 20')
    plt.plot(df['sma_long'], label='SMA 50')
    plt.legend(); plt.title("SMA Strategy"); pdf.savefig(); plt.close()

    plt.figure(figsize=(10,5))
    plt.plot(equity_sma.index, equity_sma['equity'], label='SMA Equity')
    plt.legend(); plt.title("Equity Curve - SMA"); pdf.savefig(); plt.close()

print("✅ PDF Generated:", pdf_path)
print("SMA Metrics:", metrics_sma)
print("RSI Metrics:", metrics_rsi)
