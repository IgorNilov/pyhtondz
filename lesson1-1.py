name = str(input('Введите Ваше Имя :'))
age = int(input('Введите Ваш возраст :'))
pol = input('Введите пол "м" или "ж" :')
if age < 18:
    print('Покиньте сайт', name)
elif pol == "м":
    print('Мальчики на лево!')
elif pol == "ж":
    print("Девочки на право!")
else:
    print('Что-то пошло не так!')
