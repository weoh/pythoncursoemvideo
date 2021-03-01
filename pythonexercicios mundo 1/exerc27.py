print(
    '\033[1;40mfaça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome \033[m'
    '\033[1;42m separadamente\033[m')

nome = str(input('\n digital seu nome: ')).strip().lower().title().split()

print(f'primeiro nome: {nome[0]}')
print(f'ultimo nome: {nome[len(nome) - 1]}')
