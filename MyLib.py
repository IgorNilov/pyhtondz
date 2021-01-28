def premia():
    a = int(input('выработка в час :'))
    b = int(input('ставка в час :'))
    c = int(input('процент премии :'))
    return (a + b) + ((a + b) * c) / 100
