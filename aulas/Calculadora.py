while True:
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [S]im ou [N]ão: ')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um numero')
        continue

    num1 = int(num1)
    num2 = int(num2)

    #  + - / *
    if operador == '+':
        print(num1+num2)
    elif operador == '-':
        print(num1-num2)
    elif operador == '/':
        print(num1/num2)
    elif operador == '*':
        print(num1*num2)
    else:
        print('Operador invalido')

