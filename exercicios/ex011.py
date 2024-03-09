# Faça um programa que leia o largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Largura de parede: '))
altura = float(input('Altura da parede: '))

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura * altura}m²')
print(f'Para pintar essa parede, você precisará de {largura * altura / 2}L de tinta.')