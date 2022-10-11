import requests
from bs4 import BeautifulSoup as bs





def get_link(url):
    
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    card = soup.find_all('a', class_='grid-item-link')
    print('Data searching')
    links = [item.get('href') for item in card]
    for link in links:
        get_data(link)
        break
def get_data(url):
    li = 'https://www.artadvisors.org'
    page = requests.get(li+url)
    soup = bs(page.text, 'html.parser')
    name = soup.find('h1', class_='ProductItem-details-title').text.strip()
    degignation = soup.find('div', class_='ProductItem-details-excerpt').find('p').text.replace('Email:', ' ')
    degignation.replace('Website:', ' ')
    a= degignation.lstrip('Phone:')
    print(a)
def main():
    url ='https://www.artadvisors.org/art-advisor-directory'
    get_link(url)

if __name__ == '__main__':
    main()