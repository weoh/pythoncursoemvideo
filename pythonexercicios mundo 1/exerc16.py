from math import hypot

co = float(input('\033[1;43mcateto oposto: \033[m'))
ca = float(input('\033[1;43mcateto adjacente: \033[m'))
h1 = hypot(co, ca)
print(f'\033[1;43m o comprimento da hipotenusa do triangulo é: {h1:.2f}\033[m')
