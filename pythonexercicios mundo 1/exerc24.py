print('\033[1;40m=====DESAFIO 24=====\033[m')
print('\033[1;40mCrie um programa que leia o nome de uma cidade e diga se ela começa ou não com santo\033[m')

cidade = str(input('\033[1;40mDigite o nome de sua cidade: \033[m')).strip().lower().capitalize()

print('\033[1;40mSanto\033[m' == cidade[:5])
