import yfinance as yf
import numpy as np
import ta
import pandas as pd  
import json

def get_stock_data(ticker_symbol, period='6mo', interval='1d'):
        # Create ticker object
    ticker = yf.Ticker(ticker_symbol)
    # Fetch data for the last 20 years
    data = yf.download(ticker_symbol, period=period, interval=interval)
    columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    predict_data = data[columns].copy()
    predict_data.reset_index(drop=True, inplace=True)

    predict_data.columns = ['open', 'high', 'low', 'close', 'volume']
    df = predict_data
    print(df.shape)
    # Calculate only the required indicators
    df['macd_DIF'] = ta.trend.macd_diff(df['close'])
    df['macd_SIGNAL'] = ta.trend.macd_signal(df['close'])
    df['macd_HIST'] = ta.trend.macd_diff(df['close'])
    df['EMA5'] = ta.trend.ema_indicator(df['close'], window=5)
    df['EMA10'] = ta.trend.ema_indicator(df['close'], window=10)
    df['EMA25'] = ta.trend.ema_indicator(df['close'], window=25)
    df['rsi_14'] = ta.momentum.rsi(df['close'], window=14)
    df['rsi_9'] = ta.momentum.rsi(df['close'], window=9)
    df['stochrsi_k'] = ta.momentum.stochrsi_k(df['close'], window=14, smooth1=3, smooth2=3)
    df['stochrsi_d'] = ta.momentum.stochrsi_d(df['close'], window=14, smooth1=3, smooth2=3)
    stochastic = ta.momentum.StochasticOscillator(high=df['high'], low=df['low'], close=df['close'], window=14, smooth_window=3)
    df['stoch_%K'] = stochastic.stoch()
    df['stoch_%D'] = stochastic.stoch_signal()
    info = ticker.info
    fundamental_data = {
        '市盈率TTM': info.get("trailingPE", "N/A"), 
        '52周最高': info.get("fiftyTwoWeekHigh", "N/A"),  
        '市淨率': info.get("priceToBook", "N/A"),  
        '流通值': info.get("marketCap", "N/A"),  
        '52周最低': info.get("fiftyTwoWeekLow", "N/A"),  
        '股息率TTM': info.get("dividendYield", "N/A"),  
    }
    indicators_data = df.tail(25)
    
    # Create the desired JSON format
    result = {
        'open': indicators_data['open'].tolist(),
        'high': indicators_data['high'].tolist(),
        'low': indicators_data['low'].tolist(),
        'close': indicators_data['close'].tolist(),
        'volume': indicators_data['volume'].tolist(),
        'macd_DIF': indicators_data['macd_DIF'].tolist(),
        'macd_SIGNAL': indicators_data['macd_SIGNAL'].tolist(),
        'macd_HIST': indicators_data['macd_HIST'].tolist(),
        'EMA5': indicators_data['EMA5'].tolist(),
        'EMA10': indicators_data['EMA10'].tolist(),
        'EMA25': indicators_data['EMA25'].tolist(),
        'rsi_14': indicators_data['rsi_14'].tolist(),
        'rsi_9': indicators_data['rsi_9'].tolist(),
        'stochrsi_k': indicators_data['stochrsi_k'].tolist(),
        'stochrsi_d': indicators_data['stochrsi_d'].tolist(),
        'stoch_%K': indicators_data['stoch_%K'].tolist(),
        'stoch_%D': indicators_data['stoch_%D'].tolist(),
        'fundamental': fundamental_data
    }
    
    return result

