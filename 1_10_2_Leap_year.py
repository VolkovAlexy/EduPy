# Урок 10.1 Задача про високосный год
year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print('Високосный')
else:
    if year % 400 == 0:
       print('Високосный')
    else:
       print('Обычный')