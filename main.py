def hisobla(a, b):
    natija = []
    for i in range(len(a)):
        natija.append(a[i]**3 + b[i]**3)
    return natija

a = [1, 2, 3]
b = [4, 5, 6]
print(hisobla(a, b))
