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
    pd.set_option('display.width', None)
    print(data)


def notify_if_strong_fluctuations(data, threshold):
    """
    Notifies the user if the stock price has fluctuated by more than a specified number over a period.
    :param data: DataFrame with data
    :param threshold: value difference threshold
    """
    if data['Close'].max() - data['Close'].min() > threshold:
        print(f'Колебания цены закрытия акций за период более {threshold}.')
