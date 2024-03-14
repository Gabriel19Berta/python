# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario + (salario/100 * 15):.2f}')