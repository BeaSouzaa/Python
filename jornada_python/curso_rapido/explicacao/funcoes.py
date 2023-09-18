#Funçoes :                     Def     (Funções nomeadas)                                        Lambda (funções anônimas)
#                       Função                     Gradores
#                       return                     yield

#               def nome (args):                      #def nome(args):
#                   return args                            yield args
# def      --> define
#nome      --> Como aquele bloco de códigos será nomeado
# (args) : --> Argumento ou parâmetro
#return    -->  Retorno, ou seja quando pedir algo deve-se retornar um valor
# *c empacota o argumento

#Função é um bloco de código
""" def diga_ola(nome_da_pessoa):
    return f'Olá {nome_da_pessoa}'


print(diga_ola("Bea"))
print(diga_ola("Alice"))
print(diga_ola("Carla")) """


#Um pedaço de código que vai repetir, sem precisar escrever todos os momentos que desejo que isso acontece


#sum --> soma
#len --> tamanho

"""

def relatorio(nome, cpf, telefone):
    return f"
                                          |||| RELATÓRIO PARCIAL ||||

    {nome}, portador do CPF {cpf}, telefone : {telefone}, está oficialmente de férias.

    Ass.
    Direção
    "


print(relatorio("Beatriz", "142.858.758/07" , "(19)98357-6631" )) """


def nome ( arg_posicional,*pacote_arg ):        # * Signfica que pode colocar n argumentos
    print( arg_posicional,
           pacote_arg
    )

def nome ( arg_nomeado = "Não tem nada",**pacote_nomeado ):        # ="" --> Na falta de mostra o que está dento do ""  pacote nomeado = dicionário
    print( arg_nomeado,
           pacote_nomeado
    )


    #Python interativo
