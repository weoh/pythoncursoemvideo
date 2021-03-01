import random

from colorama import Back, Fore

numero: int = int(random.randint(0, 5))
tentativa = int(input('adivinhe o numero que eu estou pensando:'))
if tentativa == numero:
    print(Back.GREEN + 'voce acertou filho da puta! parabens! ')
else:
    print(Fore.RED + 'voce errou cuzão! tente na proxima!')
