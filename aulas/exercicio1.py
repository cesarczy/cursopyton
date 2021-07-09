# * Criar variáveis para nome (str), idade (int), altura(float) e peso (float) de uma pessoa.
# * Criar variavel com o ano atual(int)
# * Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# * Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
# * Exibir um texto com todos os valores na tela usando F-Strings (com chaves)

ano_atual = 2021
nome = 'Cesar Siqueira'
idade = 32
altura = 1.80
e_maior = idade > 17
peso = 84
imc = peso / (altura**2)
nasc = ano_atual - idade


print(f'{nome} tem {idade} anos, {altura: .2f} de altura e pesa {peso}')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'César nasceu em {nasc}')

