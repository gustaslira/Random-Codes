import random

a, b, c, d, e = 0, 0, 0, 0, 0
enum = ['A','B','C','D','E']

for i in range(1,91):
  r = random.randrange(0,5)
  resposta = enum[r]
  print(f'Questão {i} - {resposta}')

  if resposta == 'A':
    a += 1
  if resposta == 'B':
    b += 1
  if resposta == 'C':
    c += 1
  if resposta == 'D':
    d += 1
  if resposta == 'E':
    e += 1

print(f'''
Quantidade de Questões:
A - {a}
B - {b}
C - {c}
D - {d}
E - {e}''')
