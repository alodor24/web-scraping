from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://coinmarketcap.com/es/'
page = requests.get(url)
soup = bs(page.content, 'html.parser')

def getCryptoCurrency(soup):

    # CryptoCurrencies
    find_currency = soup.find_all('a', class_='currency-name-container')
    currencies = []

    for i in find_currency:
        currencies.append(i.text)

    # Return 20 first terms
    return currencies[:20]


def getPriceCryptoCurrency(soup):

    # Price CryptoCurrencies
    find_price = soup.find_all('a', class_='price')
    prices = []

    for i in find_price:
        prices.append(i.text)

    # Return 20 first terms
    return prices[:20]


def showData():

    currencies = getCryptoCurrency(soup)
    prices = getPriceCryptoCurrency(soup)

    # Show data on format table
    data_frame = pd.DataFrame({'Name Crypto Currency': currencies, 'Price': prices}, index = list(range(1, 21)))

    return data_frame



if __name__ == "__main__":

    data = showData()
    print(data)
    # data.to_html('file.html')
    # data.to_json('data.json', index=True)
    # data.to_csv('data.csv', index=False)