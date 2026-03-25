#4-3

numeros = list(range(1, 21))
print(numeros)

#4-4
numeros2 = []
for i in range(1, 101):
    numeros2.append(i)

print(numeros2)

#4-5
numeros3 = []
for i in range(1, 101):
    numeros3.append(i)

print(sum(numeros3))

#4-6

numeros4 = []
for i in range(1, 21, 2):
    numeros4.append(i)

print(numeros4)

#4-7

numeros5 = []
for i in range(3, 31):
    if i % 3 == 0:
        numeros5.append(i)

print(numeros5)

#4-8
numeros6 = []
for value in range(1, 11):
    elevado = value **3
    numeros6.append(elevado)
    print(elevado)

#4-9
numeros7 = [value**3 for value in range(1, 11)]
print(numeros7)













