
import sqlite3 as dbc
import os 
from bs4 import BeautifulSoup
import requests as rq
import re

db = "shitdb.db"
sql = "schema.sql"

def check_db():
    return os.path.exists(db)

if not check_db():
    raise Exception("DATABASE DOES NOT EXIST -- PLEASE CHECK PATH")
    
with open(sql, 'r') as rf:
    # Read the schema from the file
    schema = rf.read()

def fetch_data():
    url = 'https://en.onepiece-cardgame.com/cardlist/?series=569105'

    response = rq.get(url)
    html_content = response.content

    parser = BeautifulSoup(html_content, 'html.parser')

    cards = parser.find_all(class_='modalCol')

    MasterDeck = []

    for card in cards:
        card_data = {}
        card_data['Card Name'] = card.find(class_='cardName').text
        card_data['Cost'] = int(card.find(class_='cost').text)
        card_data['Attribute'] = card.find(class_='attribute').text
        card_data['Power'] = int(card.find(class_='power').text)
        card_data['Counter'] = int(card.find(class_='counter').text)
        card_data['Color'] = card.find(class_='color').text
        card_data['Feature'] = card.find(class_='feature').text
        card_data['Text Effect'] = ' '.join(card.find(class_='text').text)
        card_data['Card Set(s)'] = ' '.join(card.find(class_='getInfo').text)

        image_tag = card.find('img')
        if image_tag is not None:
            image_url = image_tag.get('src')
            image_url = re.sub(r'\.\./', 'https://en.onepiece-cardgame.com/', image_url)
            card_data['Image URL'] = image_url
    
        MasterDeck.append(card_data)

        # Insert into the SQLite database
    with dbc.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                INSERT INTO OP (Cname, Cost, Atr, Power, Ccount, Color, Feature, Effect, Imgurl)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
            card_data['Card Name'], card_data['Cost'], card_data['Attribute'], card_data['Power'],
            card_data['Counter'], card_data['Color'], card_data['Feature'], card_data['Text Effect'],
            card_data.get('Image URL', None)
            ))
        conn.commit()

    return MasterDeck
