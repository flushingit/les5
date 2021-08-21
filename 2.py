# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

word_number = []
with open("text.txt") as f_obj:
    count = sum(1 for _ in f_obj)                 # Считаем кол-во строк
    f_obj.seek(0, 0)
    for str_number in range(1, count + 1):
        cont = f_obj.readline()
        temp_list = [x for x in cont.split(' ')]  # Разбиваем строку на слова
        word_number.append(len(temp_list))        # Считаем ко-во слов

print(f"Всего строк {count}")
for x in range(0, count):
    print(f"В {x + 1}-ой строке {word_number[x]} слов(а)")
