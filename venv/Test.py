def create_cook_book(dishes):
    cook_book = {}

    try:
        # читаем файл. разбиваем на строки. записываем строки в список lst для более удобной работы
        with open("dishes", encoding='utf-8') as f:
            lst = [line.strip() for line in f]

        # тут долго ломал голову как лучше начать и взять название блюда... ничего лучше в голову не пришло...
        for i, c in enumerate(lst):
            if c.isdigit():
                # если элемент == цифра ==> берем название блюда из предшествующего элемента
                cook_book[lst[i-1]] = []

                # собираем ингридиенты в срезе с индекса после кол-ва ингр-ов до : индекс + кол-во ингр-ов + 1
                for slice in lst[i+1:i+int(c)+1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]

                    cook_book[lst[i-1]].append({'ingredient_name':ingredient_name,
                                                'quantity':quantity,
                                                'measure':measure})
        return cook_book

    except FileNotFoundError:
        return(f'Файл: {input_file_name} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'