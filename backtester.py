import pandas as pd

def backtest_signals(data, signal_col, initial_cash=10000, position_size=0.2):
    cash = initial_cash
    position = 0.0
    trades, equity_curve = [], []

    for idx, row in data.iterrows():
        price = row['close']
        sig = row[signal_col]
        if sig == 1:  # Buy
            equity = cash + position * price
            alloc = equity * position_size
            shares = alloc // price
            if shares > 0:
                cash -= shares * price
                position += shares
                trades.append({'date': idx, 'side': 'BUY', 'price': price, 'shares': shares, 'cash': cash})
        elif sig == -1 and position > 0:  # Sell
            cash += position * price
            trades.append({'date': idx, 'side': 'SELL', 'price': price, 'shares': position, 'cash': cash})
            position = 0.0
        equity = cash + position * price
        equity_curve.append({'date': idx, 'equity': equity})

    equity_df = pd.DataFrame(equity_curve).set_index('date')
    trades_df = pd.DataFrame(trades)
    metrics = {
        'initial_cash': initial_cash,
        'final_equity': equity_df['equity'].iloc[-1] if not equity_df.empty else initial_cash,
        'total_trades': len(trades_df)
    }
    return trades_df, equity_df, metrics
