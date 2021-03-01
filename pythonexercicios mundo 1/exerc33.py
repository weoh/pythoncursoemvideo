num1 = int(input('\033[1;40mprimeiro valor: \033[m'))
num2 = int(input('\033[1;40segundo valor: \033[m'))
num3 = int(input('\033[1;40terceiro valor: \033[m'))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'\033[1;40m maior valor é {maior}\033[m')
print(f'\033[1;40m menor valor é {menor}\033[m')
