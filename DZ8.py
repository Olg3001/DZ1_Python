# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить 
# шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

print('Programm to define if it is possible to break off the necessary chokolate piece for single break')
print('Define the numbers')

n = int(input('Input the pieces quantity of the first side: '))
m = int(input('Input the pieces quantity of the second side: '))
k = int(input('Input the pieces number necessary to get: '))

if k > m * n:
    print('Impossible to break as the pieces quantity is more than quantity in che chokolate')
elif (k == m * n and k != 1) or (m == n == 1):
    print('It is not necessary to break off the chokolate')   
elif (k < m * n) and (k % m == 0) or (k % n == 0):
    print('Yes, it is possible to get the necessary piece from one break off')
else:
    print('No, it is impossible to get the necessary piece from one break off')    