# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

num_list = []
final_dict = {}

with open("6_List.txt", encoding='UTF8') as f_obj:
    count = sum(1 for _ in f_obj)
    f_obj.seek(0, 0)
    for x in range(1, count + 1):
        cont = f_obj.readline()
        temp_list = [x for x in cont.split()]

        for y in range(0, len(temp_list)):  # Удаляем ненужные символы, оставляем только предмет и часы
            temp_list[y] = temp_list[y].replace(":", "")
            temp_list[y] = re.sub(r'\(.*\)', '', temp_list[y])

        for z in temp_list:  # Создаём список с часами, почему-то [z for z in temp_list if z.isdigit] не сработало
            try:
                num_list.append(int(z))
            except ValueError:
                continue
        final_dict[temp_list[0]] = (sum(num_list))
        num_list.clear()
print(final_dict)

# Против лома нет приёма). Как не пытался сделать это всё эллегантнее ничего не получилось :(