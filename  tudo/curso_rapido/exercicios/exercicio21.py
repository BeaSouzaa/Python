
def quadrado(lista_numeros):                                                        #definindo quadrada como lista_numeros
    lista_resposta = []
    for numero in lista_numeros:                                                    #Para cada número na lista de números
        lista_resposta.append(numero ** 2)                                          #Adiciona na lista_resposta e elevando cada número ao quadrado
    return lista_resposta                                                           #Retorna o valor da lista com cada número elevado ao quadrado

def cubo(lista_numeros2):
    lista_resposta2 = []
    for numero in lista_numeros2:
        lista_resposta2.append(numero ** 3)
    return lista_resposta2

lista_valores = []

for valor in range(10):                                                             #Até o tamanho 10
    lista_valores.append(                                                           #Adicione a lista_valores
        int(input("Digite um númeto:   "))                                          # O números que o usuário digitar
    )


dicionario = {
    'lista padrão': lista_valores,
    'lista ao quadrado': quadrado(lista_valores),
    'lista ao cubo': cubo(lista_valores)
}

print(dicionario)
