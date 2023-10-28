def soma():
    n1 = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))
    print("Soma: ",n1+n2)

def subtracao():
    n1 = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))
    print("Subtracao: ",n1-n2)

def multiplicacao():
    n1 = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))
    print("Multiplicacao: ",n1*n2)

def divisao():
    n1 = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))
    print("Divisao: ",n1/n2)

opcao = 1

while opcao:
    #print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()