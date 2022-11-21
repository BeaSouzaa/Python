
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
num4 = float(input("Digite o 4º número: "))
num5 = float(input("Digite o 5º número: "))


if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 :
    print (f'O maior número é o {num1}')
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5 :
    print(f'O maior número é o {num2}')


if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5 :
    print(f'O maior número é o {num3}')
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print(f'O maior número é o {num4}')


if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print(f'O maior número é o {num5}')
else:
    print("Os números digitados não podem ser iguais")
