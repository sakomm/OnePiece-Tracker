
    -- for card in cards:
    --     card_data = {}
    --     card_data['Card Name'] = card.find(class_='cardName').text
    --     card_data['Cost'] = card.find(class_='cost').text
    --     card_data['Attribute'] = card.find(class_='attribute').text
    --     card_data['Power'] = card.find(class_='power').text
    --     card_data['Counter'] = card.find(class_='counter').text
    --     card_data['Color'] = card.find(class_='color').text
    --     card_data['Feature'] = card.find(class_='feature').text
    --     card_data['Text Effect'] = ' '.join(card.find(class_='text').text)
    --     card_data['Card Set(s)'] = ' '.join(card.find(class_='getInfo').text)

    --     image_tag = card.find('img')
    --     if image_tag != None:
    --         image_url = image_tag.get('src')
    --         image_url = re.sub(r'\.\./', 'https://en.onepiece-cardgame.com/', image_url)
    --         card_data['Image URL'] = image_url
    
    --     MasterDeck.append(card_data)

CREATE TABLE OP (
    Cname VARCHAR(255),
    Cost INT,
    Atr VARCHAR(255),
    Power INT,
    Ccount INT,
    Color VARCHAR(255),
    Feature VARCHAR(255),
    Effect TEXT,
    Imgurl VARCHAR(5555)
);