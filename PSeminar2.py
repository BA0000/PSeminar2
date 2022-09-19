# 1.	Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# x = float(input('Input real number: '))
# while x % 1 > 0:
#     x *= 10
# sum = 0    
# while x > 0:
#     sum += x % 10
#     x //= 10
# print(int(sum))


# 2.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# n = int(input('Input number: '))
# count = 1
# for i in range(1, n+1):
#     count *= i 
#     print(count, end=' ')
# print()



# 3.	Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# x = int(input('Enter number: '))
# sum = 0
# for x in range(1, x + 1):
#     sum = sum + round((1 + 1/x)**x, 2)
# print(sum)


# 4.	(ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


# from random import randint

# n = int(input('Input number: '))
# numbers = []
# for i in range(n):
#     numbers.append(randint(-n, n))
# print(numbers)

# f = open('file.txt', 'w')
# while True:
#     s = input('Enter position: ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)



# 5.	Реализуйте алгоритм перемешивания списка.

# from random import shuffle
# list = [1, 2, 3, 4, 5, 6, 7]
# shuffle(list)
# print(list)






















