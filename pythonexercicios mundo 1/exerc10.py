l = float(input('\033[1;43mwidth of your wall: \033[m'))
a = float(input('height of your wall: \033[m'))
ar = l*a
it = 2
qt = ar//it + (ar%it)
print(f'\033[1;43m your wall have the dimension of {l}x{a} and your area is of {ar}m².\033[m')
print(f'\033[1;43m the area of your wall is: {ar} and you will spend {qt} liters of ink to paint the wall\033[m')

