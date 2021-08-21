# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.
import json

final_dict ={}
average_profit = 0

with open("7_list.txt") as f_obj:
    count = sum(1 for _ in f_obj)                 # Считаем кол-во строк
    f_obj.seek(0, 0)
    for str_number in range(1, count + 1):
        cont = f_obj.readline()
        temp_list = [x for x in cont.split(' ')]
        if (int(temp_list[2]) - int(temp_list[3])) > 0:
            average_profit = average_profit + (int(temp_list[2]) - int(temp_list[3]))
        final_dict[temp_list[0]] = (int(temp_list[2]) - int(temp_list[3]))
final_list =[final_dict,{"average_profit": average_profit}]

with open("7.json", "w") as write_f:
    json.dump(final_list, write_f)

