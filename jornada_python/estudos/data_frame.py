from sys import displayhoo
import pandas as pd

lista_nomes = "Beatriz Carolina Ayla Lua Ruy".split()
print(pd.DataFrame(lista_nomes, columns=["Nome"]))
