#Compre o mais barato


produtoA = float(input("Qual é o preço desse produto? "))
produtoB = float(input("Qual é o preço desse produto? "))
produtoC = float(input("Qual é o preço desse produto? "))


if produtoA < produtoB and produtoA < produtoC :
    print("Compre o primeiro produto")
elif produtoB < produtoA and produtoB < produtoC :
    print("Compre o segundo produto")
else :
    print ("Compre o terceiro produto")
