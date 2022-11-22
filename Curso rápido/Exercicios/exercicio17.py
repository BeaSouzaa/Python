#Um programa, com uma função, que calcula a mediana de uma lista
# sorted (lista) --> Ordena a lista

lista = [7, 85, 9, 5, 1, 2, 2, 32, 3, 4, 5]

def mediana(l):
    tamanho = len(l) // 2                                                            #tamanho = quantidade de caracteres da lista // 2  - Divisão Inteira
    l.sort()                                                                         #Ordena a lista

    if not len(l) % 2:                                                               #Se o reto da divisão dos caracteres por 2
        return (l[tamanho - 1] + l[tamanho]) / 2.0                                   #Retorne a conta

    return l[tamanho]

print(mediana(lista))
