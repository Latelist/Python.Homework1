# Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Enter number: '))
sum = 0
while number >= 1:
    sum += number % 10
    number = number // 10

print(sum)