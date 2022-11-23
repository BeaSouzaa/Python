#Tuplas ()  --> Permite o desempacotamento , são imutáveis e podem devolver mais de um valor ao mesmo tempo


minha_tupla = ('Bea', 26, '4541515', 'R fkieikc', 0)
nome, idade, *coisas_que_nao_quero = minha_tupla                  #empacotamento só pode ocorre em uma vez
nome, idade = idade, nome
