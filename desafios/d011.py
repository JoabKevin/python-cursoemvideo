# calcular area da parede e quantos litros de tinta serão necessarios. 1L de tinta pinta 2m².
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
tinta = area / 2
print(f'Área total: {area} m². \nPara pintar {area} m², você precisará de {tinta} litros de tinta.')
