# Crie um programa que mostre todas as informações possíveis de uma variável por meio da função 'is'.
algo = input('Digite algo: ')
print(f'''Você digitou: {algo}
{algo} contém apenas letras? {algo.isalpha()}
{algo} contém apenas números? {algo.isnumeric()}
{algo} é alfanumérico: {algo.isalnum()}
{algo} é um número decimal? {algo.isdecimal()}
{algo} está escrito em maiúsculas? {algo.isupper()}''')
