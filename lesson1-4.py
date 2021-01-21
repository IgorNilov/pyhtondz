number = int(input('Введите число:'))
i = 0
while number > 0:
    c = number % 10
    if c >= i:
        i = c
    number //= 10
print(i)
