velo = float(input('\033[1;40mquantos km/h o veiculo tava percorrendo \033[m'))
if velo > 80:
    print('\033[1;40mtudo, esta dentro da faixa permitida!\033[m')
else:
    multa = (velo-80)*7
    print(f'\033[1;40msera aplicada uma multa de {multa:.2f} reais!\033[m')
