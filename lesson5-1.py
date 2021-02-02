fail = input('имя файла :')
f = open(fail, 'w', encoding='utf-8')
while True:
    s = input('Введите строку : \n')
    if s == '': break
    f.writelines(s + '\n')
f.close()
f = open(fail, 'r')
content = f.readlines()
print(content)
f.close()
