# Índices
# 0123456789.............................33

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_user = input('Digita um letra: ')

while contador < tamanho_frase:
    # print(frase[contador], contador) um print por execução
    letra = frase[contador]
    if letra == input_do_user:
        nova_string += input_do_user.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
