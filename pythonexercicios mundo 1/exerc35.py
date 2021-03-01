print('\033[1;40mme diga os 3 pra ver se ele pode ser um triangulo ou não\033[m')

l1 = int(input('\033[1;40mlado 1:\033[m'))
l2 = int(input('\033[1;40mlado 2:\033[m'))
l3 = int(input('\033[1;40mlado 3:\033[m'))

if l1 > (12 + 13) or 12 > (11 + 13) or 13 > (11 + 12):
    print("\033[1;40mnao pode ser um triangulo\033[m")
elif 11 == 12 == 12:
    print('\033[1;40mé um triangulo equilatero\033[m')
elif 11 == 12 or 11 == 13 or 12 == 13:
    print('\033[1;40mé um triangulo isosceles\033[m')
else:
    print('\033[1;40mé um triangulo escaleno\033[m')

