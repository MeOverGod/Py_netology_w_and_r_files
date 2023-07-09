import os
from pprint import pprint

with open('data.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        dishes_count = int(file.readline().strip())
        dishes = []
        for _ in range(dishes_count):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            dishes.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[recipe_name] = dishes

pprint(cook_book, sort_dicts = False)

print()

def get_shop_list_by_dishes(dishes, person_count):

    dict_by_dishes = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingr in cook_book[dish_name]:
                dict_by_dishes[ingr['ingredient_name']] = {
                    'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count
                    }
    pprint(dict_by_dishes)
    

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
