print("""\033[1;40mFaça um programa que leia uma frase e mostre:
1- Quantas vezes aparece a letra A
2- Em que posição ela aparece a primeira vez
3- em que posição ela aparece a ultima vez \033[m""")

frase = str(input('\033[1;40m digite uma frase: \033[m')).strip().lower()

print("\033[1;40mQuantidade de vezes que a letra ""a"" aparece: {}\033[m".format(frase.count('a')))

print(f'\033[1;40m em que posição o a aparece a primeira vez: {frase.find("a") + 1}\033[m')

print(f'\033[1;40m em que posição o a aparece pela ultima ve z: {frase.rfind("a") + 1}\033[m')
