num = str(input('\033[1;40m digite um numero de 0 a 9999: \033[m')).zfill(4)

print(f'\033[1;40m \nO numero digitado foi foi {num}\033[m')
print(f'\033[1;40m sua unidade é: {num[3]} \033[m')
print(f'\033[1;40m sua dezena é: {num[2]}\033[m')
print(f'\033[1;40m sua centena é: {num[1]}\033[m')
print(f'\033[1;40m seu milhar é: {num[0]}\033[m')
