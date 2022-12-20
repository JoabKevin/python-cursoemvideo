#leia o preço de um produto e mostre-o com 5% de desconto.
loja = 'LOJA CANGURU PERNETA'
print('=-'*20)
print(f'{loja:^40}')
print('=-'*20)
preco = float(input('Preço atual do produto: '))
desc = preco - (preco * 5 / 100)
print(f'Preço com 5% de desconto: {desc:.2f}')
