# Урок 1.10 Задача про норму сна
minTime = int(input())
maxTime = int(input())
sleepTime = int(input())
if sleepTime < minTime:
    print('Недосып')
else: 
    if sleepTime > maxTime:
        print('Пересып')
    else:
        print('Это нормально')