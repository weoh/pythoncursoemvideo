numero = int(input('\033[1;40mdigite um numero inteiro: \033[m'))
resultado = numero % 2
print(f'\033[1;40messe numero é impar!' if resultado >0 else 'esse nuemro é par\033[m')