m = float(input('\033[1;41mdigite quantos metros você quer que seja convertido em centímetos e milímetros:\033[m'))
km = m*10 ** -3
hm = m*10 ** -2
dam = m*10 ** -1
dm = m*10 ** 1
c = m*10 ** 2
mi = m*10 ** 3
print(f'\033[1;41m{m}m em centímetros é {c}cm\033[m')
print(f'\033[1;41m{m}m em milímetros é {mi}mm\033[m')
print(f'\033[1;41m{m}m em decimetros é {dm}dmm\033[m')
print(f'\033[1;41m{m}m em decâmetros é {dam}dam\033[m')
print(f'\033[1;41m{m}m em hectõmetros é {hm}hm\033[m')
print(f'\033[1;41m{m}m em kilometros é {km}km\033[m')
