from bs4 import BeautifulSoup
import requests

destructibility = {}
destructibility['Aramid'] = 0.25
destructibility['UHMWPE'] = 0.45
destructibility['Combined materials'] = 0.5
destructibility['Titan'] = 0.55
destructibility['Aluminium'] = 0.6
destructibility['Armor steel'] = 0.7
destructibility['Ceramic'] = 0.8
destructibility['Glass'] = 0.8

def retrieveTable(url):
    web_text = requests.get(url)
    scrape = BeautifulSoup(web_text.text, 'html.parser')
    armor_table = scrape.find('table',class_='wikitable sortable')
    return armor_table.findAll("tr")

class ArmorItem(object):
    icon = ""
    name = ""
    material = ""
    level = ""
    zones = ""
    durability = ""
    movement = ""
    turn_speed = ""
    ergo = ""
    weight = ""
    
    def printInfo(self):
        print(  ' Name: ' + self.name + '\n',
                'Material: '+ self.material + '\n',
                'Class: ' + self.level + '\n',
                'Zones: ' + self.zones + '\n',
                'Durability: ' + self.durability + '\n',
                'Movement Speed: ' + self.movement + '\n',
                'Turn Speed: ' + self.turn_speed + '\n',
                'Ergonomics: ' + self.ergo + '\n',
                'Weight: ' + self.weight + '\n')
    
    def CreateSqlStatement(self):
        
            beginning = "INSERT INTO Armor (ArmorName, MaxDurability, [Level], Material, Destructibility, Zones, MovementSpeed, TurnSpeed, Ergonomics, [Weight]) VALUES("
            return beginning +'\''+ self.name +'\''+ ',' + self.durability + ',' + self.level + ',' +'\''+ self.material +'\''+ ',' + str(destructibility[self.material]) + ',' +'\''+ self.zones+'\''+ ','  + str(float(self.movement[:-1]) / 100) + ',' + str(float(self.turn_speed[:-1]) / 100) + ','+ self.ergo + ',' + str(float(self.weight[:-3])) + ");"
            
