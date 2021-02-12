# Урок 1.12 Задача про формулу Герона
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = (((p * (p - a)) * (p - b)) * (p - c)) **0.5
print(S)