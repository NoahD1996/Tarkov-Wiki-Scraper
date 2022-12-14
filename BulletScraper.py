from BulletItem import BulletItem, loadBulletsFromUrl

bullets = []
urls = [
    "https://escapefromtarkov.fandom.com/wiki/12x70mm",
    "https://escapefromtarkov.fandom.com/wiki/20x70mm",
    "https://escapefromtarkov.fandom.com/wiki/23x75mm",
    "https://escapefromtarkov.fandom.com/wiki/9x18mm_Makarov",
    "https://escapefromtarkov.fandom.com/wiki/7.62x25mm_Tokarev",
    "https://escapefromtarkov.fandom.com/wiki/9x19mm_Parabellum",
    "https://escapefromtarkov.fandom.com/wiki/.357_Magnum",
    "https://escapefromtarkov.fandom.com/wiki/.45_ACP",
    "https://escapefromtarkov.fandom.com/wiki/9x21mm_Gyurza",
    "https://escapefromtarkov.fandom.com/wiki/5.7x28mm_FN",
    "https://escapefromtarkov.fandom.com/wiki/4.6x30mm_HK",
    "https://escapefromtarkov.fandom.com/wiki/9x39mm",
    "https://escapefromtarkov.fandom.com/wiki/.366_TKM",
    "https://escapefromtarkov.fandom.com/wiki/5.45x39mm",
    "https://escapefromtarkov.fandom.com/wiki/5.56x45mm_NATO",
    "https://escapefromtarkov.fandom.com/wiki/.300_Blackout",
    "https://escapefromtarkov.fandom.com/wiki/7.62x39mm",
    "https://escapefromtarkov.fandom.com/wiki/7.62x51mm_NATO",
    "https://escapefromtarkov.fandom.com/wiki/7.62x54mmR",
    "https://escapefromtarkov.fandom.com/wiki/.338_Lapua_Magnum",
    "https://escapefromtarkov.fandom.com/wiki/12.7x55mm_STs-130"
]



with open("bulletAdd.sql","w") as file:
    for url in urls:
        for item in loadBulletsFromUrl(url):
            item.CreateSqlStatement(file)