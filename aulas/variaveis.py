nome = 'Cesar Siqueira'
idade = 32
altura = 1.80
e_maior = idade > 17
peso = 84
imc = peso / (altura*altura)

# print('Nome:', nome)
# print('Idade:', idade)
# print('Altura:', altura)
# print('É de maior ?:', e_maior)
# print('O IMC é:', imc)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc: .2f}')
print('{0} tem {1} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

