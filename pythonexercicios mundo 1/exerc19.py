from random import choice

aluno1 = input('\033[1;41mnome do 1 aluno: \033[m')
aluno2 = input('\033[1;41mnome do 2 aluno: \033[m')
aluno3 = input('\033[1;41mnome do 3 aluno: \033[m')
aluno4 = input('\033[1;41mnome do 4 aluno: \033[m')
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(alunos)
print(f'\033[1;41mo nome dos quatros alunos são: {aluno1} , {aluno2}, {aluno3}, {aluno4}.\ne o sorteado é: {sorteado}\033[m')
