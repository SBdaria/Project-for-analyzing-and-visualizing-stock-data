import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = ''
    while True:
        choice = input("Выберите формат интервала:\n1 - общий период (1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.)\n2 - определенный период (с ГГГГ-ММ-ДД по ГГГГ-ММ-ДД)\nВаш выбор: ")
        if choice == '1':
            period = input("Введите период для данных (например, '1mo' для одного месяца): ")
            break
        elif choice == '2':
            start = input("Введите дату начала периода в формате ГГГГ-ММ-ДД: ")
            end = input("Введите дату окончания периода в формате ГГГГ-ММ-ДД: ")
            break
        else:
            print('Ваш выбор некорректен. Введите 1 или 2.')

    # Fetch stock data
    if period:
        stock_data = dd.fetch_stock_data(ticker, period=period)
    else:
        stock_data = dd.fetch_stock_data(ticker, start=start, end=end)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    #dplt.create_and_save_plot(stock_data, ticker, period)

    # Average closing price of shares
    dd.calculate_and_display_average_price(stock_data)

    # Calculating stock price fluctuations
    # dd.notify_if_strong_fluctuations(stock_data, int(input("Введите максимальную величину колебания цены акций: ")))

    # Saving to a CSV file
    dd.export_data_to_csv(stock_data, f"information_about_stock_price_{ticker}_for_{period}.csv")

    # Calculation of indicators RSI and MACD
    print(f"RSI за данный период = {dd.rsi(stock_data)}")
    print(f"MACD за данный период = {dd.macd(ticker)}")


if __name__ == "__main__":
    main()
