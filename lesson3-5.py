def my_f():
    res = 0

    while True:
        numbers = input('Enter list of number or * to exit: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Конечный итог {res} . Exit')
                    return res
                else:
                    res += int(i)
            except ValueError:
                print('Enter number or *')
        print(f'{i} : итог {res}')


m_ee = my_f()
print(m_ee)
