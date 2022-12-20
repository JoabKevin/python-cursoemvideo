#aluguel de carros. leia quantos dias o carro foi alugado e quantos km rodou. R$60 por dia e R$0,15 por km.
d = int(input('Quantos dias o carro foi usado? '))
km = float(input('Quantos km rodados nesse período? '))
valor = (d * 60) + (km * 0.15)
print(f'''Tempo utilizado: {d} dias.
Distância percorrida: {km:.1f} quilômetros.
Total a pagar: R${valor:.2f}.''')
