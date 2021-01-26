def my_f(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


val_my_f = my_f(a=float(input('первое число :')),
                b=float(input('второе число :')),
                c=float(input('третье число :')))
print(val_my_f)
