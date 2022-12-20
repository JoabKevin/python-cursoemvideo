# Algoritmo que leia duas notas e calcule a média.
escola = 'ESCOLA JAVALI CANSADO'
print('=' * 30)
print(f'{escola:^30}')
print('=' * 30)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Média do aluno: {media:.0f}')
