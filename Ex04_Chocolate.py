# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

size = input('Введите размер шоколадки: ')
size = size.split(' ')
size_list = [int(i) for i in size]
print(size_list)

piece = int(input('Сколько долек нужно отломить: '))
flag = False

for i in size_list:
    if piece % i == 0:
        flag = True
        break
print(flag)