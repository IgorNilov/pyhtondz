def my_f(x_1, x_2):
    try:
        c = x_1 / x_2
        print(f"{c:.2}")

    except ZeroDivisionError:
     print('на 0 делить нельзя')

my_f(float(input("x_1 :")), (float(input("x_2 :"))))
