import requests
from bs4 import BeautifulSoup as bs

def get_page(url):
    page = requests.get(url)
    if page.status_code==200:
        soup = bs(page.text, 'html.parser')
    else:
        soup = {'Server Responded': page.status_code}
    return soup

def index(soup):
    try:
        page =soup.find('p', class_='result-message').text.split(' ')[28]
        page_num = int(page)//50+1
    except:
        page_num = ''
    print(page_num)

def get_detail(soup):
    name = soup.find('li', class_='profile-compact')
    print(len(name))

def main():
    url = 'https://www.floridabar.org/directories/find-mbr/?fName=a&pageNumber=1&pageSize=50'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    urls = []
    for letter in letters:
        url = f'https://www.floridabar.org/directories/find-mbr/?fName={letter}&pageNumber=1&pageSize=50'
        urls.append(url)
        for url in urls:
            get_detail(get_page(url))




if __name__ == '__main__':
    main()
