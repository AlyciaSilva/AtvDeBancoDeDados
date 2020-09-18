def calculo(x):
    resultado = ""
    if x == 2 or x == 1:
        resultado = 'sim'
    else:
        if x % 2 != 0:
            if x % 3 != 0:
                if x % 5 != 0:
                    resultado = 'sim'
                else:
                    resultado = 'não'
    return resultado  
n = int (input("Digite um número para verificar se é primo: "))
if calculo(n) == 'sim':
    print("É UM NÚMERO PRIMO!!!!!!!!!!!!!!!!!")
else:
    print ("Não é um primo :(")    