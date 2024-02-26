# Funções são blocos reutilizaveis de códigos 
# Ao inves de ficar replicando o código, vc pode criar uma função e chamar ela toda vez que for necessário

# Vai somar os números e retornar um valor

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)