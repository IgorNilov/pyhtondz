den = 1
a = float(input('введите сколько бегаете км:'))
b = float(input('введите сколько хотите пробегать :'))
while a < b:
        a += a * 0.1
        den += 1
print(f"через {den}")
