#While, continue

#Exemplo 1
# x = 0
# # while x <= 100:
# #     print(x)
# #     x = x + 1

# #Exemplo2
# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         continue
#     print(x)
#     x = x+1

#Exemplo 3

# x = 0 #coluna
# while x < 10:
#     y = 0 # linha
#
#     while y < 5:
#         print(f'{x}, {y}')
#         y+=1
#     x += 1 # x = x + 1
# print('Acabou! ')

#For

# texto = 'Python'
#
# for n, letra in enumerate(texto):
#     print(n, letra)
#
# Função range (start=0, stop, step=1)

for num in range(5, 10, 1):
    print(num)
