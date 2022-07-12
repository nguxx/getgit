dix = input("entre un nombre pour le transfomer en binaire :")
print(dix)
print(type(dix))
dix = int(dix)
list = []
print(dix)
while True:
    print("dix =", dix)
    list.append(dix%2)
    dix = dix//2
    if dix == 0:
        break
print(list)
list.reverse()
print(list)
