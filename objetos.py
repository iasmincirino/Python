# Dicionarios usam chave e valor para armazenar informações

# Em uma var temos acesso a três informações:
pessoa = {
    "nome": "Iasmin",
    "idade": 19,
    "peso": 65.5
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])

# Informações do jogador
player = {
    "nome": "Maria",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5
}

# Inimigos
npcs = [
    {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    {"nome": "Monstro", "dano": 5, "hp": 100, "exp": 10},
    {"nome": "Monstrão", "dano": 10, "hp": 150, "exp": 15},
    {"nome": "Chefão", "dano": 25, "hp": 200, "exp": 20}
]
