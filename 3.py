# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

income = {}

with open("3_List.txt", encoding='UTF8') as f_obj:
    count = sum(1 for _ in f_obj)
    f_obj.seek(0, 0)
    for x in range(1, count + 1):
        cont = f_obj.readline()
        cont = cont.replace("\n", "")
        temp_list = [x for x in cont.split(' ')]
        income[temp_list[0]] = float(temp_list[1])
print("За чертой бедности :")
for x in income.keys():
    if income.get(x) < 20000:
        print(x)
print(f"Средний доход сотрудников равен {round(sum(income.values()) / count, 2)} рублей")
