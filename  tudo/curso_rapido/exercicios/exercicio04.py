#Fça um programa que peça 2 números inteiro e um float

NumeroInt01 = int(input("Digite um número inteiro: "))
NumeroInt02 = int(input("Digite outro número inteiro: "))
NumeroFloat = float(input("Digite um número decimal: "))

#Qual é o produto do dobro do primeiro com metade do segundo


resp1 = (NumeroInt01*2)*(1/2)*(NumeroInt02)

print (f'O produto do dobro do primeiro com metade do segundo é :  {resp1}')


#A soma do triplo do primeiro com o terceiro

resp2 =float((3*(NumeroInt01))+(NumeroFloat))


print (f'A soma do triplo do primeiro com o terceiro é : {resp2}')

#O terceiro elevado ao cubo

resp3 = (NumeroFloat)**3

print(f'O terceiro elevado ao cubo é: {resp3}')
