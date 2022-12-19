# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Programm to count the digits sum of the three-digit number')
input = int(input('Iput three-digit integer:\t'))

if (99 < input < 1000):
    result = input // 100 + input // 10 % 10 + input % 10
    print(result)
else:
    print('Incorrect input')