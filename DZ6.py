# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным 
# номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет 
# с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

print('Programm to count if the ticket number is lucky or not')
input = input('Input ticket number:\t')

def CheckTicket(input):
    sum1 = int(input[0]) + int(input[1]) + int(input[2])
    sum2 = int(input[3]) + int(input[4]) + int(input[5])
    if (sum1 == sum2):
        return ('The ticket is lucky')
    else:
        return ('The ticket is not lucky')

CheckTicket(input)

if (99999 < int(input) < 1000000):
    print(CheckTicket(input))
else:
    print('Incorrect unput. The ticket number should have 6 digits.')     