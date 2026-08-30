import os

def operação_valores(n1, n2, op):
    match op:
        case "+":
            return n1+n2
        case "-":
            return n1-n2
        case "*":
            return n1*n2
        case "/":
            return n1/n2
        case _:
            print("INVALIDO!")

def percorrendo_vetor(vetor = []):
    for i in range(1,5):
        nome = int(input(f"Digite o valor de {i} : "))
        vetor.append(nome)
        
nome = input("Digite o seu nome: ")
print("Agora vamos fazer as operações básicas")
n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))
resposta = input("Digite SIM, caso deseje prosseguir e NÃO para o contrário: ")
if resposta == "SIM":
    op = input("Digite a operação a ser feita: ")
    print(operação_valores(n1,n2,op))
print(nome)
resposta = input("Digite SIM, caso deseje prosseguir e NÃO para o contrário: ")
if resposta == "SIM":
    print("Vamos preencher vetores e demonstrar")
    vetor = []
    percorrendo_vetor(vetor)
    print(vetor)