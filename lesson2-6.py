goods = []
features = {'название':'', 'кол-во': '', 'ед. измерения': ''}
analitcs = {'название': [], 'кол-во': [], 'ед. измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    features = features.copy()
    for f in features:
        pro = input(f'Введите значения свойства "{f}": ') #Ввод свойства
        features[f] = int(pro) if f == 'цена' or f == 'кол-во' else pro # Меняем тип числовых свойств
        analitcs[f].append(features[f]) # добавляем свойство в аналитику
    goods.append((num, features)) # добавляем свойство в список товаров
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\nТекущая аналитика по товарам: \n{'*' * 60}")
    for key, value in analitcs.items():
        print(f'{key:>30}: {value}')
    print('*' * 60)

