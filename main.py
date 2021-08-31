# Задание №1

import json

keys = ['ingridient_name', 'quantity', 'measure', ]
cook_book = {}

with open('dishes_list.txt', encoding='utf-8') as file:
    lines = []
    for line in file:
        line = line.strip()
        if line:
            lines.append(line)
        continue
    lines = iter(lines)

    for name in lines:
        cook_book[name] = []
        num = next(lines)

        for _ in range(int(num)):
            ingridient = next(lines)
            ing = ingridient.split(' | ')
            z = zip(keys, ing)
            ingridient_dict = {k: v for (k, v) in z}
            cook_book[name].append(ingridient_dict)
            continue

        continue
print(json.dumps(cook_book, indent=0, ensure_ascii=False))

# Задание №2

dishes = input('ВВедите название блюда: \n')
person_count = int(input('Введите количество персон: \n'))
def get_shop_list_by_dishes(dishes, person_count):
    for k,v in cook_book.items():
        if dishes in k:
            for ingridients in v:
                b = (int(ingridients['quantity']) * person_count)
                ingridients['quantity'] = b
            return(cook_book[dishes])

print(get_shop_list_by_dishes(dishes, person_count))

