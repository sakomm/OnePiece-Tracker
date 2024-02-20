import requests as rq
from bs4 import BeautifulSoup
import re

url = 'https://en.onepiece-cardgame.com/cardlist/?series=569105'

response = rq.get(url)
html_content = response.content

parser = BeautifulSoup(html_content, 'html.parser')

cards = parser.find_all(class_='modalCol')

MasterDeck = []

for card in cards:
    card_data = {}
    card_data['Card Name'] = card.find(class_='cardName').text
    card_data['Cost'] = card.find(class_='cost').text
    card_data['Attribute'] = card.find(class_='attribute').text
    card_data['Power'] = card.find(class_='power').text
    card_data['Counter'] = card.find(class_='counter').text
    card_data['Color'] = card.find(class_='color').text
    card_data['Feature'] = card.find(class_='feature').text
    card_data['Text Effect'] = ' '.join(card.find(class_='text').text)
    card_data['Card Set(s)'] = ' '.join(card.find(class_='getInfo').text)

    image_tag = card.find('img')
    if image_tag:
        image_url = image_tag.get('src')
        image_url = re.sub(r'\.\./', 'https://en.onepiece-cardgame.com/', image_url)
        card_data['Image URL'] = image_url
    
    MasterDeck.append(card_data)

for card_data in MasterDeck:
    print(card_data)
