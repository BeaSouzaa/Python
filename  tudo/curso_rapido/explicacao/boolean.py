#São comparativos: verdade, falso, maior (>), menor(<), diferente (!=), igual (==), maior ou igual (>=), menor ou igual (<=)  <- Conectivo lógico.
#Conectivos lógicos:
#And  <- True and True : True ; False and True: False
#Or   <- True or False : True ; False or False: False
#Not  <- Inverte a lógica : not False : True ; not True : False



#python -i

nome1 = "Ana"
idade1 = 28
nome2 = "Ju"
idade2 = 26
nome3 = "Ana"
idade3 = 32

nome1 == nome2                                  #False

nome1 == nome3                                  #True

nome1 != nome2                                  #True

nome1 == nome3 and idade1 == idade3             #False

nome1 == nome3 or idade1 == idade3              #True

not nome1 == nome3                              #False
