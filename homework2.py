# # На столе лежат n монеток. Некоторые из них лежат вверх решкой,а некоторые – гербом.
# # Определите минимальное число монеток, которые нужно перевернуть,
# # чтобы все монетки были повернуты вверх одной и той же стороной.
# # Выведите минимальное количество монет, которые нужно перевернуть

# variant to deal task #1:
# import random
# from random import randint
# amount_coin = int(input('enter the number of coins: '))
# m = 0
# k = 0
# coins = [0, 1]
# for i in range(amount_coin):
#     random.shuffle(coins)
#     print(coins)
#     if int(coins[0]) == 0:
#         k += 1
#     if int(coins[0]) == 1:
#         m += 1
# print(f'total coins {m, k}')

# if m > k:
#     ans = k
# else:
#     ans = m

# print(f"minimum to flip: {ans}")


# # variant to deal task #2:
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)

# # Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# # Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# # Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# # Помогите Кате отгадать задуманные Петей числа.

# # deal of task:
# S = int(input('Enter the sum of the nambers: '))
# P = int(input('Enter the product of the numbers: '))

# X = (S-int((S**2-4*P)**0.5))//2
# Y = S - X
# for x in range(1, 1001):
#     if X <= Y and X * Y == P:
#         print("numbers conceived by Petya is - ", X, "and", Y)
#         break
#     else :
#         print("Petya is trying to confuse")
#         break

# # variant to deal task #2:
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)

# # Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# # Пример:
# # 10 -> 1 2 4 8
# # степень 0 1 2 3 результат не больше 10

# N = int(input('Enter an integer greater than 1: '))
# k = 1
# while k <= N:
#     print(k, end =' ')
#     k = k * 2

# # variant to deal task #2:
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1