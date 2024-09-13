import random
lista = []
rangenumbeers = 10

for i in range(rangenumbeers):
    
    number = random.randint(1,50)
    lista.append(number)

print(lista)
print(f"W liście jest {len(lista)} liczb")
print("Najmniejsza liczta to: " , min(lista))
print("Największa liczta to: " , max(lista))
