# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("Введите ip-адрес в формате 10.0.1.1: ")
ip_oct = ip.split('.')

if (not ip_oct[0].isnumeric() or not ip_oct[1].isnumeric() or not ip_oct[2].isnumeric() or not ip_oct[3].isnumeric()):
    print("Неправильный IP-адрес")

else:
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