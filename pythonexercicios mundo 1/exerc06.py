name = input('\033[1;45mname student: \033[m')
note1 = float(input('\033[1;45mtype the note1: \033[m'))
note2 = float(input('\033[1;45mtype the note2: \033[m'))
average = (note1 + note2)/2
print(f'\033[1;45mthe average student {name} is {(average) :.2f}\033[m')