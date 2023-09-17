#While = Enquanto uma condição for x , irá executar o que foi proposto
#Break = Parar, brecar a condição
#while se repete baseado em um estado booleano


resposta = input("Vamos sair hoje [s/n]? ")

n = 1


while resposta != "s":
    resposta = input(f'Bora{"a" * n}[s/n]? ')
    n += 1   # n = n+1
    if 'chat' in resposta :
        print("Foi mal!")
        break

else:
    print(f'AEEEEE{"E"*n}')


#For : Para "cada"
#Exemplo : for e in "grupy":        --> Para cada elemento dento do grupy (grupo de python)
#print(e)                           --> Escreva o elemento
#For se repete baseado em algo que tem

palavra = "Python"

for posição, letra in enumerate(palavra):
    print (posição, letra)


frase = "Eduardo foi a feira".split()

for palavra in frase:
    if palavra == 'Eduardo':
        print('Eu')
    else:
        print(palavra)
