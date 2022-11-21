#Estrutura de decisão: if, elif, else
#Python não precisa de "" entre os conectivos


#EXEMPLO 1
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

if x == y :
     print ("Mesmo valor")
elif x > y :
     print ("X é maior do que y")
else:
     print (f"Não sei resolver {x} e {y}")


#EXEMPLO 2

carteira = input("Quanto tenho na carteira? ")
tenis = input("Qual é o valor do tênis? ")
necessidade = input("Você precisa mesmo disso? [s/n]: ")

if carteira >= tenis and necessidade == 's':
    print("Compre o tênis")
elif carteira > tenis and necessidade == 'n':
    print("Você não precisa disso")
else :
    print("Deixa para o mês que vem")
