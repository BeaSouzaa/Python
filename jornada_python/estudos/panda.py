import pandas as pd

pd.Series(data=5)

lista_nomes = "Beatriz Carolina Ayla Lua Ruy".split()

pd.Series(lista_nomes)


series_dados = pd.Series({
    "nome1": "Beatriz",
    "nome2": "Carolina",
    "nome3": "Ayla",
    "nome4": "Lua",
    "nome5": "Ruy"
}
)


# retorna uma tupla com o número de linhas
print("Quantidade de linhas: ", series_dados.shape)
# retorna o tipo de dados, se for misto será object
print("Tipo de dados: ", series_dados.dtypes)
# retorna um boolean onde verifica se há valores únicos
print("Existem valores únicos: ", series_dados.is_unique)
# retorna um boolean onde verifica se há valores nulos
print("Existem valores nulos: ", series_dados.hasnans)
# retorna a quantidade de dados, ps: método, realiza a ação de contar
print("Quantidade de valores: ", series_dados.count())