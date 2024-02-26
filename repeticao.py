# FOR = Loop que percorre sequências, repetindo ações para cada elemento.
# WHILE = Loop que executa ações enquando a condição for vedadeira.

# Dando nota para 5 alunos:
notas = []

# O "x" é um valor temporario que será mudada com a execução do loop
# Range possui 5 itens
for x in range(5):
    cod_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resul = [cod_aluno, nota]
    notas.append(resul)

print("Quantidade de notas", len(notas))

for n in notas:
    cod_aluno = n[0]
    nota = n[1]
    print("O RM", cod_aluno, "tirou a nota:", nota)

# _________________________________________
# Exemplo com WHILE:
    
notass = []
contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    notaa = float(input("Nota: "))
    resultado = [codigo_aluno, notaa]
    notass.append(resultado)

    # alternativa: contador += 1
    contador = contador + 1

print("Quantidade de notas", len(notass))