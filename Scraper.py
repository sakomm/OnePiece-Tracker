import tkinter as tk
from tkinter import scrolledtext
import requests as rq
from bs4 import BeautifulSoup
import re

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

    return MasterDeck

def display_data():
    cards = fetch_data()

    output_text = ""
    for card_data in cards:
        output_text += "Card Name: {}\n".format(card_data['Card Name'])
        output_text += "Cost: {}\n".format(card_data['Cost'])
        output_text += "Attribute: {}\n".format(card_data['Attribute'])
        output_text += "Power: {}\n".format(card_data['Power'])
        output_text += "Counter: {}\n".format(card_data['Counter'])
        output_text += "Color: {}\n".format(card_data['Color'])
        output_text += "Feature: {}\n".format(card_data['Feature'])
        output_text += "Text Effect: {}\n".format(card_data['Text Effect'])
        output_text += "Card Set(s): {}\n".format(card_data['Card Set(s)'])
        output_text += "\n"

    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, output_text)

# Create the main window
root = tk.Tk()
root.title("One Piece Card Data")

# Create a text area to display the data
text_area = scrolledtext.ScrolledText(root, width=80, height=20)
text_area.pack()

# Create a button to fetch and display the data
fetch_button = tk.Button(root, text="Fetch Data", command=display_data)
fetch_button.pack()

# Run the GUI main loop
root.mainloop()



