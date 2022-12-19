import requests
import csv
from bs4 import BeautifulSoup as BS



def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup =BS(html,'lxml')
    return soup

def get_data(soup):
    phones=soup.find_all('div',class_="ty-column4")
    i=1
    for phone in phones:
        title = title=phone.find('a',class_='product-title').text.strip()
        print(f'{i} телефон:',title)
        try:
            price = phone.find('span', class_='ty-price-num').text
        except AttributeError:
            price=None

        image = phone.find('img',class_='ty-pict').get('data-ssrc')   
        
    write_csv({
        'title':title,
        'image': image,
        'price': price
    })
def write_csv(data):
    with open('phones.csv','a') as file:
        names = ['title','price','image']
        write = csv.DictWriter(file, delimiter=',',fieldnames=names)
        
        write.writerow(data)

        
        
    
def main():
    BASE_URL='https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru/'
    html =get_html(BASE_URL)
    soup = get_soup(html)
    get_data(soup)
main()