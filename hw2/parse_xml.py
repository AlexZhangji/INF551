import xml.etree.ElementTree as ET

tree = ET.parse('nutrition.xml')
root = tree.getroot()

for food in root.findall('food'):
    name = food.find('name').text
    vit_a = food.find('vitamins').find('a').text
    cal = food.find('calories').get('total')

    print 'name:{}\nvitamin a:{}\ncalories:{}\n'.format(name, vit_a, cal)
