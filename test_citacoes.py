import requests
from bs4 import BeautifulSoup
import requests_cache
from citacoes_scrapper import get_caixinhas_citacoes

requests_cache.install_cache('aula.cache')


def test_get_caixinhas():
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)
    xxx = BeautifulSoup(response.text, 'lxml')

    assert isinstance(get_caixinhas_citacoes(xxx), list)
    assert len(get_caixinhas_citacoes(xxx)) >=1
