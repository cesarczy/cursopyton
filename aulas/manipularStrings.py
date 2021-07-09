# Manipulando Strings
#
# - String indices
# - Fatiamento de Strings [inicio:fim:passo]
# - Funçoes built-in len, abs, type, print, etc..
# Essas funções podem ser usadas diretamento em cada tipo


# positivos

texto1 = 'Cesar Siqueira'
print(texto1[7]) #peguei somente uma letra

texto2 = texto1[2:6] #da letra tal a letra tal
print(texto2)

# negativos /excluidos uma letra

texto3 = texto1[:-1]
print(texto3)

# pulando caracter

texto4 = texto1[0:7:2]
print(texto4)

# imprimir na vertical

print(len(texto1))

for letra in texto1:
    print(letra)







