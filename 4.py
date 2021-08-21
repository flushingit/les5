# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


num_dict = dict(One="Адын", Two="Два", Three="Три", Four="Четыре")
cont_wr = []

with open("4_list.txt", encoding='utf8') as read_obj, open("4_res.txt", 'w', encoding='windows-1251') as write_obj:
    cont = read_obj.readlines()
    for x, y in enumerate(num_dict.keys()):
        a = cont[x]
        cont_wr.append(a.replace(y, num_dict.get(y)))  # Формируем список на запись, заменяя значения на русские

    write_obj.writelines(cont_wr)
