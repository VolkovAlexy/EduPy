'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт 
биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, 
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', 
то есть группы одинаковых символов исходной строки заменяются на этот символ и количество 
его повторений в этой позиции строки.'

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит 
закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр 
символов.
'''


dna = input() + ' '
cnt = 1

for i in range (0, len(dna) - 1):
    if dna[i] == dna[i + 1]:
        cnt += 1
    else:
        print((dna[i] + str(cnt)), end='')
        cnt = 1


# Это решение крутилось в голове, но смог оформить только после решения способом выше. 
# Ложился спать и пришла такая логика. Нужно присвоить новой переменной значение первой 
# буквы и сравнивать её по порядку в массиве. Как только буква в переменной не ровна букве
# в цикле нужно отправить на печать букву и счётчик, а потом присвоить переменной новую 
# букву из цикла и сбросить счётчик. Но утром оформить это не смог :D

# dna = input() + ' '
# cnt = 0
# x = dna[0]
# for i in dna:       
#     if x != i:
#         print(x + str(cnt), end = '')
#         cnt = 0
#         x = i
#     cnt += 1

