# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:
# o	6782 -> 23
# o	0.56 -> 11

n = input('Введите вещественное число: ')

sum = 0
for i in range(len(n)):
    if n[i].isdigit():
        sum += int(n[i])

print(sum)

# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:
# o	пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N: '))

pr = 1
sp = []
for i in range(1, n + 1):
    pr *= i
    sp.append(pr)

print(sp)

# 3. Задайте список из n чисел последовательности (1+1/n)**n 
# выведите на экран их сумму.

try:
    n = int(input('Введите положительное число N: '))
    sum = 0
    for i in range(1, n + 1):
        sum += (1 + 1 / i) ** i
    print('Сумма чисел последовательности: ', round(sum, 3))
except ValueError:
    print('Вы ввели НЕ число')

# 4. Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число N: '))
sp = []

for i in range(-n, n+1):
    sp.append(i)

print(sp)

pr = 1
try:
    with open('file.txt') as f:
        for line in f:
            pr *= sp[int(line)]
    print(pr)
except FileNotFoundError:
    print('Файл не найден!')
finally:
    f.close()

# 5. Реализуйте алгоритм перемешивания списка 
# (shuffle использовать нельзя, другие методы из библиотеки random - можно)

import random

n = int(input('Введите длину списка N: '))
sp = []

for i in range(n):
    a = random.randint(0, 9)
    sp.append(a)

print('Cгенерированный рандомный список в границах : ', sp)


for i in range(0, len(sp)):
    random_index = random.randint(0,len(sp) - 1)
    sp[i], sp[random_index] = sp[random_index], sp[i]

print('Перемешанный рандомный список: ', sp)