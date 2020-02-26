stroka = (input("Введите строку из нескольких слов, разделённых пробелами: ")).split()
print(stroka)

for n, i in enumerate(stroka):
    if len(i) <= 10:
        print("№ {}, элемент: {}".format((n + 1), i))
    else:
        print("№ {}, элемент: {}".format((n + 1), (i[:10])))
