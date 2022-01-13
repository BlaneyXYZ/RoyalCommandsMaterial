import requests, re, csv, os
from bs4 import BeautifulSoup

os.remove("items.csv") # bad but I lazy

def createAlias(material):
    material_re = re.compile("^(.+)_(.+)")
    if "LEGACY_" in material:
        return
    alias = []
    alias.append(material)
    alias.append(material.replace("_", ""))
    if "_SPAWN_EGG" in material:
        material = material.replace("_SPAWN", "")
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    if "_WOOD" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    if "_DOOR" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    if "_SLAB" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    if "_STAIR" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    if "REDSTONE_" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[1], x[2]))
    if "_ORE" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    if "_WOOL" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    if "_CARPET" in material:
        if material_re.search(material):
            x = re.search("^(.+)_(.+)", material)
            alias.append("{}:{}".format(x[2], x[1]))
    alias_string = ','.join(alias)
    return alias_string

page = requests.get("https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html")
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('section', class_='constants-summary')
for data in table.find_all('div', class_='col-first'):
    for item in data.find_all('a'):
        row = [item.text, 0, "{}".format(createAlias(item.text))]
        with open('items.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            # write the data
            writer.writerow(row)
