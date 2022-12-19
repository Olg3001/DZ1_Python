# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

print('Programm to count the cranes number each kid had done if we know the sum.')
input = int(input('Input the cranes number:\t'))

if (input % 6 == 0):
    petyaAndSergResult = input // 6
    katyaResult = petyaAndSergResult * 4

    print(f'Petyas cranes quantity: {petyaAndSergResult}')
    print(f'Serezhas cranes quantity: {petyaAndSergResult}')
    print(f'Katyas cranes quantity: {katyaResult}')

else:
    print('Impossible to solve the task with the inputed number')