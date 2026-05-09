import requests
from bs4 import BeautifulSoup

def fetch_product_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find('h1').text.strip() if soup.find('h1') else '未知商品'
    description = soup.find('div', {'class':'product-description'}).text.strip() if soup.find('div', {'class':'product-description'}) else ''
    return {'title': title, 'description': description}
