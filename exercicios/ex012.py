# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Qual é o preço do produto? R$'))

print(f'O produto que custava R${preco_produto}, na promoção com desconto de 5% vai custar R${preco_produto - (preco_produto/100 * 5):.2f}')