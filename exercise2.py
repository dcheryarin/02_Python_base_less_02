list = []
while True:
    elem = input("Введите элемент списка: ")
    list.append(elem)
    elem_end = (input("Это все элементы списка? (Y/N)")).upper()
    if elem_end == "Y":
        break
print(list)
for ind, el in enumerate(list):
    print(ind, el)
print(len(list))
print(len(list) // 2)
while len(list) // 2
