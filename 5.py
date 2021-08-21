#  5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randrange

a = ""
for x in range(randrange(1, 10)):
    a = a + str(randrange(1, 100)) + " "

with open("5_list.txt", 'w') as write_obj:
    write_obj.writelines(a)
with open("5_list.txt") as read_obj:
    cont = read_obj.read()
    print(f"Числа в файле {cont}")
    num_list = [int(x) for x in cont.split()]
    print(f"Сумма чисел {sum(num_list)}")
