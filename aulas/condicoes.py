#Condições IF, ELIF e ELSE

if False:
    print('É verdadeiro')
elif False:
    print('Agora é verdade')
else:
    print('É sim')

# ---------------------------------------------------------------

nome = input('Qual o seu nome ? ')
idade = int(input('Qual a sua idade? '))


#Limite para pegar empréstimo
idade_menor = 20 #muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')