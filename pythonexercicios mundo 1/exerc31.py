dis = float(input('\033[1;40mquantos km serão percorridos nessa viagem? \033[m'))
if dis <= 200:
    preço = dis * 0.50-dis
    print(f'\033[1;40mo custo da viagem sera de {preço:.2f} reais\033[m')
else:
    preço = dis * 0.45
    print(f'\033[1;40mo custo da viagem sera de {preço:.2f} reais\033[m')