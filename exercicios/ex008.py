# Escreva um programa que leia um valor em metros e a exiba convertido em centímetros e milímetros.

distancia = int(input('Uma distância em metros: '))

print(f'A medida de {distancia:.1f}m corresponde a')
print(f'{distancia / 1000}km')
print(f'{distancia / 100}hm')
print(f'{distancia / 10}dam')
print(f'{distancia * 10}30m')
print(f'{distancia * 100}cm')
print(f'{distancia * 1000}mm')
