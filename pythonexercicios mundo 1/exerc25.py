print("\033[1;40mcrie um programa que leia o nome de uma pessoa e\n diga se ela tem silva no nome\033[m")

nome = str(input('\033[1;40digite o seu nome: \033[m')).lower().title().strip()

print('Silva' in nome)
