
from datetime import date
ano = int(input('\033[1;40mdigite o ano desejado ou digite 0 pra analisar o atual: v'))
resultado = ano % 4
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'\033[1;40mo ano {ano} é bissexto! \033[m')
else:
    print(f'\033[1;40mo ano {ano} não é bissexto! \033[m')
