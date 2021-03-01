import math

a = float(input('ddigite o angulo que vc deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'o angulo de {a} é o seno de {s:.2f} ')
print(f' o angulo de {a} é o cosseno de {c:.2f} ')
print(f' o angulo de {a} é o tangente de {t:.2f}')
