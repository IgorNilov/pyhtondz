my_str = input('Введите строку :')
my_str = my_str.split()
for x, b in enumerate(my_str, 1):
    print(f"{x} {b:.10}")

