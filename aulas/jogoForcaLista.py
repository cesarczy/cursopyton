palavra = 'carteira'
digitadas = []
chances = 3

while True:

    if chances <= 0:
        print('Você perdeu!!! ')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Você digitou mais que uma letra')
        continue

    digitadas.append(letra)

    if letra in palavra:
        print(f'Você acertou a letra: {letra.upper()}')
    else:
        print(f'Você errou, a letra: {letra.upper()} não tem nessa palavra')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == palavra:
        print(f'Fim de jogo, a palavra é: {palavra}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')

    if letra not in palavra:
        chances -= 1

    print(f'Você ainda tem {chances} chances. ')
    print()
