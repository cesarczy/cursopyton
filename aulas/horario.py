# #Faça um programa que pergunte a hora ao usuario e, baseando-se no horário descrito,
# exiba a saudação apropriada. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

hora1 = input('Quantas horas? ')

if hora1.isdigit():
    hora1 = int(hora1)

    if hora1 < 0 or hora1 > 23:
        print('Horário inválido ')

    else:
        if hora1 <= 11:
            print('Bom dia ')
        elif hora1 <= 17:
            print('Boa tarde ')
        else:
            print('Boa noite')

else:
    print("Por favor, digite um horário entre 0 e 23")