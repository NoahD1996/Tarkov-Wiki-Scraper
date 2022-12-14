from bs4 import BeautifulSoup
import requests
from ArmorItem import ArmorItem,retrieveTable

url = 'https://escapefromtarkov.fandom.com/wiki/Chest_rigs#Armored'

armors = retrieveTable(url)

index = 0
items = []
for armor in armors:
    #print(str(armor) + '\n\n')
    if(index >= 3):
        names = armor.findAll('th')
        details = armor.findAll('td')
        #print(str(details) + '\n')
        item = ArmorItem()
        item.name = names[1].text[:-1]
        item.material = details[3].text[:-1]
        if(item.material == 'Combined\nmaterials\n'):
            item.material = 'Combined materials'
        if(item.material == 'Armor\nsteel\n'):
            item.material = 'Armor steel'
        item.level = details[4].text[:-1]
        item.zones = details[5].text[:-1]
        item.durability = details[6].text[:-1]
        item.movement = details[8].text[:-1]
        item.turn_speed = details[9].text[:-1]
        item.ergo = details[10].text[:-1]
        item.weight = details[11].text[:-1]
        items.append(item)

    index += 1
with open("carrierAdd.sql","w") as sql_file:
    for item in items:    
        sql_file.write(item.CreateSqlStatement() + '\n')