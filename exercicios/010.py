# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ele pode comprar
# Considere US$1.00 = R$3.27

carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = carteira / 3.27

print(f'Com {carteira} você pode comprar US$ {dolar:.2f}')