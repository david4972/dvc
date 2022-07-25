# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('fivethirtyeight')


def market():
    print("TREASURY YIELD (10yr Bond) HISTORICAL MARKET DATA")
    md = pd.read_csv("^TNX.csv")
    print(md)

    plt.figure(figsize=(12.5, 4.5))
    plt.plot(md['Adj Close'], label='Nasdaq')
    plt.title('Futures Closing price history (last 5 years)')
    plt.xlabel('Jan 30,2015 - May 28, 2021')
    plt.ylabel('Closing price USD($)')
    plt.legend(loc='upper left')
    plt.show()

    # mean avg price (1 month)
    SMA30 = pd.DataFrame()
    SMA30['Adj Close'] = md['Adj Close'].rolling(window=30).mean()

    # mean avg price (2 months)
    SMA100 = pd.DataFrame()
    SMA100['Adj Close'] = md['Adj Close'].rolling(window=50).mean()


    # average closing price over last five years
    plt.figure(figsize=(12.5, 4.5))
    plt.plot(md['Adj Close'], label='Treasury Yield (10yr Bond)')
    plt.plot(SMA30['Adj Close'], label='SMA30')
    plt.plot(SMA100['Adj Close'], label='SMA100')
    plt.title('Nasdaq Closing price history (2021)')
    plt.xlabel('Jun 10,2017 - June 10, 2022')
    plt.ylabel('Closing price USD($)')
    plt.legend(loc='upper left')
    plt.show()


def intro():
    print("======= DORMAND CAPITAL =======")
    market()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intro()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
