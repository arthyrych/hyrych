# 1) Напишите программу, вычисляющую среднее арифметическое двух чисел.
# 2) Введите три числа и выведите на экран значения суммы и произведения этих чисел.
# 3) Напишите простой конвертер валют (без возможности динамического выбора валют пользователем).
# Валюты заданы хардкодом и не изменяются. Тип валют на выбор программиста.
# тут обычная арифметика но можешь задать это что бы каждое задание это было новая функция

print('Task 1. Getting an average.')
x = 'Enter the first number: '
y = 'Enter the second number: '


def average(first, second):
    print('The average from', first, 'and', second, 'is', (first + second) / 2)


average(int(input(x)), int(input(y)))

print('\nTask 2. Getting sum and multiplication.')
x = 'Enter the first number: '
y = 'Enter the second number: '
z = 'Enter the third number: '


def user_sum(first, second, third):
    print('The sum from', first, 'and', second, 'and', third, 'is', first + second + third, '\n')


def multiplication(first, second, third):
    print('The multiplication from', first, 'and', second, 'and', third, 'is', first * second * third)


user_sum(int(input(x)), int(input(y)), int(input(z)))
multiplication(int(input(x)), int(input(y)), int(input(z)))

print('\nTask 3. Money exchange UAH to USD.')

x = 'Enter the amount in UAH (Ukrainian Hryvnya): '


def kapusta(bablo):
    print(bablo, 'in USD (US dollars) will be', bablo / 24.1)


kapusta(int(input(x)))