#Cálculo de notas


nota1 = float(input("Por favor, digite sua primeira nota: "))
nota2 = float(input("Por favor, digite sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7 :
    print("Parabéns, você está aprovado")
elif media == 10 :
    print ("Parabéns, você foi aprovado com distinção")
else:
    print("Não foi dessa vez")
