time = int(input('Введите время в секундах :'))
hour = time // 3600
minute = (time - hour * 3600) // 60
sek = time - (hour * 3600) - (minute * 60)
print(f'{hour:02}:{minute:02}:{sek:02}')
