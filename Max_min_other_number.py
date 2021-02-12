# Урок 1.12.5 Задача упорядочить три числа  

'''
Напишите программу, которая получает на вход три целых числа, 
по одному числу в строке, и выводит на консоль в три строки 
сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
'''

a, b, c = int(input()), int(input()), int(input())

if  a >= b >= c:
    maxNumber = a
    otherNumber = b
    minNumber = c
elif b >= c >= a:
    maxNumber = b
    otherNumber = c
    minNumber = a
elif c >= b >= a:
    maxNumber = c
    otherNumber = b
    minNumber = a
elif b >= a >= c:
    maxNumber = b
    otherNumber = a
    minNumber = c
elif c >= a >= b:
    maxNumber = c
    otherNumber = a
    minNumber = b
elif a >= c >= b:
    maxNumber = a
    otherNumber = c
    minNumber = b

print(maxNumber) 
print(minNumber)
print(otherNumber)