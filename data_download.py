from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
    Retrieves historical stock data for a specified ticker and time period. Returns a DataFrame with data.
    :param ticker: stock ticker
    :param period: time period
    :return: DataFrame with data
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Adds a column to the DataFrame with a moving average calculated based on closing prices.
    :param window_size: sliding window size
    :param data: DataFrame with data about stock data
    :return: DataFrame with data
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    Calculates and displays the average closing price of shares for a given period.
    :param data: DataFrame with data
    """
    print('Средняя цена закрытия акций за заданный период:', data['Close'].mean())


def notify_if_strong_fluctuations(data, threshold):
    """
    Notifies the user if the stock price has fluctuated by more than a specified number over a period.
    :param data: DataFrame with data
    :param threshold: value difference threshold
    """
    if data['Close'].max() - data['Close'].min() > threshold:
        print(f'Колебания цены закрытия акций за период более {threshold}.')


def export_data_to_csv(data, filename):
    """
    Saving downloaded stock data to a CSV file.
    :param data: DataFrame with data
    :param filename: file name with information
    """
    data.to_csv(filename)
    print(f"Файл с информацией об акциях сохранен как {filename}")


def rsi(data):
    """
    function for calculating RSI
    :param data: DataFrame with data
    :return: value of RSI
    """
    au, ad = 0, 0
    close_price = data['Close']
    for i in range(len(close_price) - 1):
        if close_price[i+1] - close_price[i] >= 0:
            au += close_price[i+1] - close_price[i]
        else:
            ad += abs(close_price[i+1] - close_price[i])
    rs = au / ad
    return 100 - 100/(1 + rs)


def ema(data):
    """
    function for calculating EMA
    :param data: DataFrame with data
    :return: value of EMA
    """
    n = len(data)
    alpha = 2 / (n + 1)
    ema = data[-1]
    for i in range(n - 2, -1, -1):
        ema = alpha * data[i] + (1 - alpha) * ema
    return ema

def macd(ticker):
    """
    function for calculating MACD
    :param ticker: stock ticker
    :return: value of MACD
    """
    current_datetime = datetime.now().strftime("%Y-%m-%d")
    earlier_datetime_12 = (datetime.now() - timedelta(days=12)).strftime("%Y-%m-%d")
    earlier_datetime_26 = (datetime.now() - timedelta(days=26)).strftime("%Y-%m-%d")
    stock = yf.Ticker(ticker)
    data_12 = stock.history(start=earlier_datetime_12, end=current_datetime)['Close'].tolist()
    data_26 = stock.history(start=earlier_datetime_26, end=current_datetime)['Close'].tolist()
    return ema(data_12) - ema(data_26)

