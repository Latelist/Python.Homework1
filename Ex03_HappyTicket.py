# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no

def sum_of_digits(number):
    sum = 0
    while number >= 1:
        sum += number % 10
        number = number // 10
    return sum

ticket = input('Введите шестизначный номер билета: ')
while (ticket.isdigit() == False) or (int(ticket) // 100000 < 1) or (int(ticket) // 100000 > 9):
    print('Номерок левый')
    ticket = input('Введите шестизначный номер билета: ')

ticket = int(ticket)

first = ticket // 1000
last = ticket % 1000 * 1000

first_sum = sum_of_digits(first)
last_sum = sum_of_digits(last)

if first_sum == last_sum:
    print('YES')
else:
    print('NO')
