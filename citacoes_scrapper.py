import requests
from  bs4 import BeautifulSoup
# url = 'http://quotes.toscrape.com/'


# response = requests.get(url)

# xxx = BeautifulSoup(response.text, 'lxml')


def get_caixinhas_citacoes(soup):
    caixinhas = soup.select('div.quote')
    print(type(caixinhas), 'ola passei aqui')
    return caixinhas