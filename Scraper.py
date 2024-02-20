import requests as rq
from bs4 import BeautifulSoup
import re

url = 'https://en.onepiece-cardgame.com/cardlist/?series=569105'

# Fetch HTML content from the URL
response = rq.get(url)
html_content = response.content

# Parse the HTML content
parser = BeautifulSoup(html_content, 'html.parser')

# Find all elements with class 'modalCol'
cards = parser.find_all(class_='modalCol')

# Initialize an empty list to store dictionaries for each card
all_cards_data = []

# Iterate over each modal element
for card in cards:
    # Extract relevant data from each modal
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
    # Get the image URL
    image_tag = card.find('img')
    if image_tag:
        image_url = image_tag.get('src')
        # Convert relative image URL to absolute URL
        image_url = re.sub(r'\.\./', 'https://en.onepiece-cardgame.com/', image_url)
        card_data['Image URL'] = image_url
    
    # Append the card data dictionary to the list
    all_cards_data.append(card_data)

# Print the list of dictionaries
for card_data in all_cards_data:
    print(card_data)
    print()
