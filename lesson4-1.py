from sys import argv

name, s_1, s_2, s_3 = argv
try:
    s_1 = float(s_1)
    s_2 = float(s_2)
    s_3 = float(s_3)
    zp = float((s_1 + s_2) + (((s_1 + s_2) * s_3) / 100))

except (TypeError, ValueError, NameError):
    print('введите число')

print(argv)
print(f"выработка в часах :{s_1} $")
print(f"ставка в час :{s_2} $")
print(f"премия :{s_3} %")
print(f"ваша зп : {zp:.2f} $")

