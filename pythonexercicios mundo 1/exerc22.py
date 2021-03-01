name = str(input('\033[1;40mdigite seu nome completo: ')).strip()
name_upper = name.upper()
name_lower = name.lower()
name_all = len(name) - name.count(' ')
name_pr = len(name.split()[0])
print(f"\033[1;40mo seu nome em maisculos fica {name_upper}'\n"
      f"o seu nome minusculo fica: {name_lower}\n"
      f"o seu nome possui: {name_all} caracteres\n"
      f"o seu primeiro nome possui: {name_pr} letras \033[m")

