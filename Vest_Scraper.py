from ArmorItem import ArmorItem,retrieveTable

url = 'https://escapefromtarkov.fandom.com/wiki/Armor_vests'

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
        item.material = details[0].text[:-1]
        item.level = details[1].text[:-1]
        item.zones = details[2].text[:-1]
        item.durability = details[3].text[:-1]
        item.movement = details[5].text[:-1]
        item.turn_speed = details[6].text[:-1]
        item.ergo = details[7].text[:-1]
        item.weight = details[8].text[:-1]
        items.append(item)

    index += 1
with open("vestAdd.sql","w") as sql_file:
    for item in items:    
        sql_file.write(item.CreateSqlStatement() + '\n')
        