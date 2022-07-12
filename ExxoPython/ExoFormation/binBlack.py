dix = input("entre un nombre pour le transfomer en binaire : ")
dix = int(dix)
list = []
while True:
    list.append(dix % 2)
    dix = dix // 2
    if dix == 0:
        break
print(list)
list.reverse()
print(list)
