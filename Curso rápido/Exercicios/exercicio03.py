# Loja de Tintas

# Tamanho em metros quadrados da área a ser pintada?
#cobertura da tinta é 1 litro para cada 3 metros
# Volume da lata 18 litros
#Valor R$80, 00

#Informar a quantidade de latas que precisa ser compradas e o valor total

print ("\n||| Bem vindo ao Color Tintas |||")
print ("Trabalhamos com latas de 18 litros! Garantimos que cada litro de tinta efetua uma excelente cobertura de uma área de 3 m²")
print ("\n|||||||| MEGA PROMOÇÃO: HOJE QUALQUER LATA DE TINTA CUSTA APENAS R$80,00 ||||||||")
print ("\nPara podermos atender melhor, por favor, preencha corretamente as informações solicitadas na tela")


nome = input ("Como você gostaria de ser chamado? ")


print (f'Olá, {nome}')

tamanho = float(input("Qual é o tamanho da área que irá pintar? "))

quantidadequeumalatafaz = 6
valor = 80.00

quantidadetinta = float((tamanho)//(quantidadequeumalatafaz))

valor_total =  float(quantidadetinta*valor)

print (f'Você irá precisar de {quantidadetinta} latas')

print (f'O valor a ser pago é de R$ {valor_total}')
