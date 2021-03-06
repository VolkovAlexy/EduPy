# Шаг 2.2.1
'''
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.
'''

'''
Так как в задаче прерыватель это число больше 100, то это условие нашего цикла.
А вот дальше задачу можно решить по-разному. 
'''
# 1ый вариант использует всё чему научили в этом шаге. 
x = 0
while x <= 100:
    x = int(input())
    if x < 10:
        continue
    if x > 100:
        break
    print(x)
    
# Этот вариант мне нравится больше, но тут не используются continue и brake. 
# x = 0
# while x <= 100:
#     if x > 9: 
#         print(x)
#     x = int(input())