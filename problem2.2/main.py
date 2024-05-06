bilangan = int(input("masukkan bilangan: "))

faktor = []
for i in range(1, bilangan + 1):
    if bilangan % i == 0:
        faktor.append(i)

print("faktor", bilangan, "adalah:")
for i in range(len(faktor) -1, -1, -1):
    print(faktor[i])