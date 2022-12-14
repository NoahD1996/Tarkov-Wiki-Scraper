import requests
from bs4 import BeautifulSoup


def loadBulletsFromUrl(url):
    web_text = requests.get(url)
    scrape = BeautifulSoup(web_text.text, 'html.parser')
    info = scrape.find("tbody").findAll('tr')
    index = 0
    items = []
    for item in info:
        if(index >= 1):
            names = item.findAll('th')
            details = item.findAll('td')
            bullet = BulletItem()
            bullet.name = names[1].text[:-1]
            bullet.damage = details[0].text[:-1]
            bullet.penetration = details[1].text[:-1]
            bullet.armor_damage = details[2].text[:-1]
            bullet.accuracy = details[3].text[:-1]
            bullet.recoil = details[4].text[:-1]
            bullet.fragmentation_chance = details[5].text[:-2]
            bullet.projectile_speed = details[9].text[:-1]
            bullet.light_bleeding_chance = details[7].text[:-1]
            bullet.heavy_bleeding_chance = details[8].text[:-1]
            bullet.ricochet_chance = details[6].text[:-2]
            items.append(bullet)
        index += 1
    return items


def cleanVariable(variable):
    if variable == '':
        return 0
    elif '+' in variable:
        return variable[1:]
    elif '%' in variable:
        return variable.replace("%",'')
    return variable

def calcDamage(equation):
    if "x" in equation:
        nums = equation.split('x')
        return int(nums[0]) * int(nums[1])
    return equation


class BulletItem(object):
    name = ""
    damage = 0
    penetration = 0
    armor_damage = 0.0
    recoil = 0
    accuracy = 0
    fragmentation_chance = 0.0
    projectile_speed = 0
    light_bleeding_chance = 0
    heavy_bleeding_chance = 0
    ricochet_chance = 0.0

    def printInfo(self):
        print("Name: " + self.name + "\n"
              + "Damage: " + self.damage + "\n"
                + "Penetration: " + self.penetration + "\n"
                + "Armor Damage: " + self.armor_damage + "\n"
                + "Recoil: " + self.recoil + "\n"
                + "Accuracy: " + self.accuracy + "\n"
                + "Fragmentation Chance: " + self.fragmentation_chance + "\n"
                + "Projectile Speed: " + self.projectile_speed + "\n"
                + "Light Bleeding Chance: " + self.light_bleeding_chance + "\n"
                + "Heavy Bleeding Chance: " + self.heavy_bleeding_chance + "\n"
                + "Ricochet Chance: " + self.ricochet_chance + "\n")

    def CreateSqlStatement(self, file):
        self.recoil = cleanVariable(self.recoil)
        self.accuracy = cleanVariable(self.accuracy)
        self.light_bleeding_chance = cleanVariable(self.light_bleeding_chance)
        self.heavy_bleeding_chance = cleanVariable(self.heavy_bleeding_chance)
        self.ricochet_chance = cleanVariable(self.ricochet_chance)
        beginning = "INSERT INTO Bullets(BulletName,Damage,Penetration,ArmorDamage,Recoil,Accuracy,FragmentationChance,ProjectileSpeed,LightBleedingChance,HeavyBleedingChance,RicochetChance) VALUES("
        statement = beginning + "\'" + self.name + "\'," + str(calcDamage(self.damage)) + "," + str(self.penetration) + "," + str(int(self.armor_damage) / 100) + "," + str(self.recoil) + "," + str(self.accuracy) + "," + str(float(
            self.fragmentation_chance) / 100) + "," + str(self.projectile_speed) + "," + str(int(self.light_bleeding_chance) / 100) + "," + str(int(self.heavy_bleeding_chance) / 100) + "," + str(float(self.ricochet_chance) / 100) + ");\n"
        file.write(statement)
