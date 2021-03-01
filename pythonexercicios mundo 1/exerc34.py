from colorama import Back, Style, Fore
salario = float(input('\033[1;40mqual é o salario do funcionario?\033[m'))
if salario <= 1.250:
    aumento = salario * 110 / 100
    print(Back.RED + f'considerando o aumento de 10%, seu salario atual é  {aumento:.2f}')
else:
    aumento = salario * 115 / 100
    print(Back.GREEN + f'considerando o aumento de 15%, seu salario atual é  {aumento:.2f} ')
