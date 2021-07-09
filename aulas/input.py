#Entrada de dados

nome = input("Qual o seu nome ? ")
idade = input("Quantos anos você tem ? ")
ano_nascimento = 2021 - int(idade)

print()

print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}')
