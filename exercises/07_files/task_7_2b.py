# -*- coding: utf-8 -*-
#!/usr/bin/venv python3

from sys import argv

file1, file2 = argv[1], argv[2]

"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]


with open(file1, 'r') as f1, open(file2, 'w') as f2:
    for line in f1:
        if not ('!' in line) and not (ignore[0] in line) and not (ignore[1] in line) and not (ignore[2] in line):
            f2.write(line)
