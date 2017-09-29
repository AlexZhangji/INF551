import pprint
import xml.etree.ElementTree as ET


def answer(food_list):
    answer_list = [[] for _ in range(6)]

    max_cal_per_ser = 0
    max_cal_food = ''

    for food in food_list:
        name = food.find('name').text.lower()

        vit_c = float(food.find('vitamins').find('c').text)
        vit_a = float(food.find('vitamins').find('a').text)
        tot_fat = float(food.find('total-fat').text)
        sat_fat = float(food.find('saturated-fat').text)
        tot_cal = float(food.find('calories').get('total'))
        serving = float(food.find('serving').text)
        # q1
        if 'chicken' in name:
            # print '{} has {} cal per serving'.format(name, tot_cal / serving)
            answer_list[0].append(tot_cal / serving)
        # q2
        if vit_c:
            answer_list[1].append(name)
            if vit_a:  # q3
                answer_list[2].append(name)
        # q4
        if tot_fat:
            if sat_fat / tot_fat >= 1 / 2:
                answer_list[3].append(name)
        # q5
        cal_per_ser = tot_cal / serving
        if cal_per_ser > max_cal_per_ser:
            max_cal_per_ser = cal_per_ser
            max_cal_food = name
        # q6
        calcium = float(food.find('minerals').find('ca').text)
        if calcium:
            answer_list[5].append([name, tot_fat / serving])
    # q5 has to iterate whole list
    answer_list[4] = max_cal_food
    return answer_list


tree = ET.parse('nutrition.xml')
root = tree.getroot()
food_list = root.findall('food')
results = answer(food_list)

pprint.pprint(results)