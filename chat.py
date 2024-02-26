import os

mensagens = [] # Lista vazia

nome = input("Nome: ") # Recebe um nome

while True: # Inicia um loop

    # Lipando terminal
    os.system('cls')

    # Verifica se tem mensagens
    if len(mensagens) > 0:
        for m in mensagens:
            # Se tiver, exibe
            print(m['nome'], "-", m['texto'])
    
    print("_________________")

    # Obtendo texto 
    texto = input("mensagen: ")
    if texto == "fim": # Verifica se o texto é "fim"
        break # Se for, acaba o loop

    # Adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })