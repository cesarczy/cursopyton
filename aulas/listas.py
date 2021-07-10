# Listas
# append - insere um valor no final da lista
# insert - insere um valor em qualquer lugar que eu quiser
# pop - deleta o elemento final da lista
# del - deleta o elemento ou fatia
# clear
# extend - juntou as listas com a função extend
# min - pega o menor valor da lista
# max - pega o maior indice da lista
# range - facilidade para criar lista

#Extend // juntou as listas com a função extend
l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['f', 'g', 'h', 'i', 'j']
l1.extend(l2)
print(l1)

print('############################################')

# append insere um valor no final da lista
l1.append('Cesar')
print(l1)

#Insert insere um valor em qualquer lugar que eu quiser

l2.insert(3, 'Siqueira')
print(l2)

del (l2[0:3]) # deleta o elemento ou fatia
print(l2)

#Min e Max
print(max(l2))
print(min(l2))

# Range facilita na criação das listas

new1 = list(range(1,10))
print(new1)

# acessando os valores dos elementos de uma lista

new2 = ['Cesar', True, 20, 30.5]

for elem in new2:
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}')


