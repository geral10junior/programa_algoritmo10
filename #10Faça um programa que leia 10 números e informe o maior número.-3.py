#Faça um programa que leia 10 números e informe o maior número.

maior = int(input('Informe o número: '))
for i in range(9):
    valor = int(input('Informe o número: '))
    if valor > maior:
        maior = valor
print("O maior valor foi", maior,)

