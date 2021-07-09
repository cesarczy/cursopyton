# Formatando valores com modificadores
#
# :s - Texto (Strings)
# :d - Inteiros (int)
# :f - Números de ponto flutuante (float)
# :.(Número) f - Quantidade de casa decimais (float)
# :(Caractere) (> ou < ou ) (Quantidade) (Tipo - s, d ou f)
#
# > - Esquerda
# < - Direita
# ^ - Centro

# Exemplo 1:
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))

# Exemplo 2:
num11 = 1
print(f'{num11:0>10}')

num22 = 1150
print(f'{num22:0>10.2f}')

nome = 'Cesar'
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

# Exemplo 3
nome = 'Cesar Siqueira'
print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) #as primeiras letras das palavras em maiusculo

