# Hello Emmanual

# Let's Start
#1 Make a request to get data from ebay.com
#2 Collect data from each detail page
#3 Collect all link to detail page of each product
#4 Write scrapped data to a csv file


from urllib import response
import requests
from bs4 import BeautifulSoup as bs

def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = bs(response.text, 'html.parser')
    return soup

def get_detail_data(soup):
    title = ''
    price = 0
    sold_item = 0
    try:
        title = soup.find('h1', class_='x-item-title__mainTitle').find('span').text
    except:
        title = ''
        
    try:
        price = soup.find('div', id='vi-mskumap-none').find('span').text.split(' ')[1]
    except:
        price = ''
    try:
        sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.split(' ')[0].replace(',','')
    except:
        sold = ''
    data = {
        'title': title,
        'price': price,
        'sold': sold
    }
    return data


def main():
    url = 'https://www.ebay.com/itm/263038140739?hash=item3d3e4b8143:g:IIEAAOSwN1peYA5n&amdata=enc%3AAQAHAAAAoH03XKH12LLbrs0QUg6AxhV8F%2BHnWEpUcPz1TUxwEooIGiJ%2BQyLV%2Bpp3dzVgNaj5QFG33zwASqwvj0PfsIx8G9yvB2PqhuCRJtoIUp3fuZVUDdoPdkAWDYKA2LNhrnEMakz1w5VlRyRDePwBWPwK8N%2BZeQwbkz7HAejtGJO4kZdNSHpi8lH4b8xCbfH3h4VabgeZSPvFT1%2Bxxk%2F%2B1YQNpUA%3D%7Ctkp%3ABk9SR6j9npL4YA'
    get_page(url)
    print(get_detail_data(get_page(url)))




if __name__ == '__main__':
    main()