dias = int(input('\033[1;42mquantos dias alugados: \033[m'))
km = float(input('\033[1;42mquantos km rodados: \033[m'))
pago = (dias * 60) + (km * 0.15)
print(f'\033[1;42mo total a pagar é de r$ {pago:.2f}\033[m')