#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите ip-адрес в формате 10.0.1.1: ")
ip_oct = ip.split('.')

if int(ip_oct[0]) >= 1 and int(ip_oct[0]) <= 223:
    print('unicast')
elif int(ip_oct[0]) >= 224 and int(ip_oct[0]) <= 239:
    print('multicast')
elif int(ip_oct[0]) == 255 and int(ip_oct[1]) == 255 and int(ip_oct[2]) == 255 and int(ip_oct[3]) == 255:
    print('local broadcast')
elif int(ip_oct[0]) == 0 and int(ip_oct[1]) == 0 and int(ip_oct[2]) == 0 and int(ip_oct[3]) == 0:
   print('unassigned')
else:
    print('unused')