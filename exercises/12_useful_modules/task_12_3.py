# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate


reach_ip_list = ['10.1.1.1', '10.1.1.2']
unreach_ip_list = ['10.1.1.7', '10.1.1.8', '10.1.1.9']

def print_ip_table(reach_ip_list, unreach_ip_list):
    """
    Отображает таблицу доступных и недоступных IP-адресов.
    
    Args:
        reachable_ips (list): Список доступных IP-адресов
        unreachable_ips (list): Список недоступных IP-адресов
    """
    
    ip_table = [('Reachable', 'Unreachable')]
    
    # Определяем максимальную длину списков
    max_length = max(len(reach_ip_list), len(unreach_ip_list))
    
    
    for i in range(max_length):
        reachable = reach_ip_list[i] if i < len(reach_ip_list) else ""
        unreachable = unreach_ip_list[i] if i < len(unreach_ip_list) else ""
        ip_table.append([reachable, unreachable])


    print(tabulate(ip_table, headers='firstrow'))


print_ip_table(reach_ip_list, unreach_ip_list)