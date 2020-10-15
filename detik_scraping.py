from bs4 import BeautifulSoup
import requests

artikel_populer = requests.get('https://www.detik.com/terpopuler', params={'tag_from' : 'wp_cb_mostPopular_more'})
soup = BeautifulSoup(artikel_populer.text, "html.parser")
populer_area = soup.find(attrs={'class': 'grid-row list-content'})
titles = populer_area.findAll(attrs={'class':'media__title'})
images = populer_area.findAll(attrs={'class':'media__image'})


for image in images :
    print(image.find('a').find('img')['title'])

