#importação completa
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'''A raiz de {num} é {raiz:.3f};
Arredondada para cima é {math.ceil(raiz)};
Arredondada para baixo é {math.floor(raiz)}.
''')

#Importação otimizada
from math import sqrt
print(f'A raiz de {num} é {sqrt(num)}') 
                        # note que não foi necessário digitar o nome da biblioteca, apenas a função importada.

import random
numero = random.random() #gera um número entre 0 e 1
numint = random.randint(0, 10) #gera um número inteiro entre o intervalo determinado.
print(numero, numint)

import emoji
print(emoji.emojize("Olá, mundo :earth_americas:", use_aliases=True))
