from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-scrapping')
def populer_scrap():
    artikel_populer = requests.get('https://www.detik.com/terpopuler', params={'tag_from' : 'wp_cb_mostPopular_more'})
    soup = BeautifulSoup(artikel_populer.text, "html.parser")
    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    titles = populer_area.findAll(attrs={'class':'media__title'})
    images = populer_area.findAll(attrs={'class':'media__image'})

    return render_template('index.html',images=images)




if __name__ == '__main__':
    app.run(debug=True)


