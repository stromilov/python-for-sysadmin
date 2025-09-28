# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan = int(input("Enter VLAN number: "))

template = '{:<9} {:<20} {}'

list_sort = []

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if '.' in line:
            line_list = line.split()
            line_list[0] = int(line_list[0])
            list_sort.append(line_list)

sort = sorted(list_sort)

for i in sort:
    if vlan == i[0]:
        print(template.format(i[0], i[1], i[3]))

print()