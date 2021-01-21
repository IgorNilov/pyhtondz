pribil = int(input('введите прибыль :'))
izder = int(input('введите издержки :'))
a = pribil - izder
b = int()
if pribil > izder:
    print(a)
    b = int(input('введите число рабочих :'))
if a > 0:
    c = a / b
    print('по', c, 'на каждого рабочего')
elif pribil < izder:
    print('Вы работаете в убыток')
elif pribil == izder:
    print('У Вас нет прибыли, но и нет убытков')
