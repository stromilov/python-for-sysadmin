#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

ip_list = ['192.168.0.200',  '8.8.8.8',        '8.8.4.4',
           '1.1.1.1',        '208.67.222.222', '4.2.2.2',
           '77.88.8.8',      '9.9.9.9',        '1.0.0.1',
           '208.67.220.220', '94.140.14.14',   '172.10.11.12']


def ping_ip_addresses(ip_list):
    '''
    Функция проверяет пингуются ли IP-адреса
    '''

    allow_ip = []
    not_allow_ip = []

    for i in ip_list:
        res = subprocess.run(['ping', '-c', '1', '-n', i], 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE, 
                             encoding='utf-8')
        
        if res.returncode == 0:    
            allow_ip.append(i)
        else:
            not_allow_ip.append(i)

    return (allow_ip, not_allow_ip)


print(ping_ip_addresses(ip_list))
