# Урок 1.12.4 Задача про жителей Малевии
'''
Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают: 
- треугольные, 
- прямоугольные и 
- круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, 
на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.
'''
figure = input()

if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (((p * (p - a)) * (p - b)) * (p - c)) **0.5
elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = float(a * b)
elif figure == 'круг':
    r = int(input())
    S = 3.14 * r ** 2
print(S)