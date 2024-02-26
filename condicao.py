# Condições
idade = int(input("Informe a sua idade: "))

if idade >= 18:
    print("PERMITIDO!")
else:
    print("BLOQUEADO!")

# Outro exemplo
age = int(input("Informe a sua idade: "))

if age <= 11:
    print("Criança")
elif(age > 11 and age <= 17):
    print("Adolescente")
elif(age > 17 and age <=64):
    print("Adulto")
else:
    print("Idoso")