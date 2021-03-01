from typing import List
from random import shuffle

n1 = input('\033[1;40mprimeiro aluno: \033[m')
n2 = input('\033[1;40msegundo aluno: \033[m')
n3 = input('\033[1;40mterceiro aluno: \033[m')
n4 = input('\033[1;40mqaurto aluno: \033[m')
lista: List[str] = [n1, n2, n3, n4]
shuffle(lista)
print(f'\033[1;40ma ordem de apresentação sera \033[m')
print(lista)
