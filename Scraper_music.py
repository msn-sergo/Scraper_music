# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
          }
    r = requests.get(url, headers = headers)
    return r.text 


def download(name, href):
    #path = (r'D:\music\Muzakis\Наши\Rock\M\Machete\\')
    path = ('I:\\testdata\\mp3_music\\')
    fullpath = ( path + name + ".mp3")        
    r = requests.get(href, stream = True)
    with open(fullpath, 'wb') as f:
        for ch in r:
            f.write(ch)    


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    link_mp3 = soup.find('div', class_="main_box").find_all('div', class_="song playitem")
    for link in link_mp3:
        href = 'https://wwvv.muzofon-online.com' + link.find('div', class_='button').find('button').get('data-norber')
        name = link.find('div', class_='button').find('button').get('data-xftitle')
        download(name, href)


def main():
    #url = 'https://wwvv.muzofon-online.com/search/%D0%BC%D0%B0%D1%87%D0%B5%D1%82%D0%B5'
    url = 'https://wwvv.muzofon-online.com/search/xov'
    print('Start downloading ...')
    get_page_data((get_html(url)))
    print('Done')

if __name__ == '__main__':
    main()






