#Lista : Aglomeram objetos dentro de si, é um tipo de container (Tudo em python que recebe objeto dentro de si leva esse nome) --> Sempre começa a contar do 0
# [-1] --> Final da Lista
# [-1][-1] --> Último elemento dentro do objeto da lista



#Slice : Pedaço da lista
#n[x:]  --> Posição x pra frente
#n[:-x] --> Posição -x pra traz
#n[x:y] --> Vai da posição x até a posição y
#n[::x] --> Pula de x em x posição

minha_lista = ['Arroz', 'Salada', 'Feijão', 10, [585,582,231]]

for item in minha_lista:
    print(item)

#Métodos lista:
# x [1, 2 ,3]
# x.append(4) = [1,2,3,4]                     --> Coloca no final da lista o valor desejado
# x.remove(2) = [1,3]                         --> Remove o valor indicado
# x.insert(4,0) = [1,2,3,0]                   --> Coloca o valor na posição escolhida
# x.pop() = 3|#[1,2]                          --> Tira o valor de dentro da lista
# x.count(2) = 1                              --> Conta a quantidade que tem do número indicado
# x.reverse() = None | # [3,2,1]              --> Inverte a lista


lista_de_compras = []
resposta = ""

while resposta != "Acabou":
    resposta = input("O que temos que comprar? ")
    if resposta != "Acabou" or "acabou":
        lista_de_compras.append(resposta)

print(lista_de_compras)
