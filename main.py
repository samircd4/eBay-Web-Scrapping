# Hello Emmanual

# Let's Start
#1 Make a request to get data from ebay.com
#2 Collect data from each detail page
#3 Collect all link to detail page of each product
#4 Write scrapped data to a csv file

import requests
from bs4 import BeautifulSoup as bs
import csv

def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = bs(response.text, 'html.parser')
    return soup

def get_detail_data(soup):
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

def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []
    # urls = [item.get('href') for item in links]
    urls = [item.get('href') for item in links]
    return urls

def write_csv(data, url):
    with open('output.csv', 'a') as file:
        writer = csv.writer(file)
        row = [data['title'], data['price'], data['sold'], url]
        writer.writerow(row)

def main():
    url = 'https://www.ebay.com/sch/i.html?&_nkw=android'
    products = get_index_data(get_page(url))
    for link in products[1:]:
        data = get_detail_data(get_page(link))
        write_csv(data, link)
    




if __name__ == '__main__':
    main()