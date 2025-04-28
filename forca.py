'''
Jogo da Forca
- O jogo da forca é um jogo de adivinhação de palavras.
- O jogador deve adivinhar uma palavra secreta, letra por letra. check
- O jogador tem um número limitado de tentativas para adivinhar a palavra. check
- Se o jogador adivinhar a palavra antes de esgotar as tentativas, ele vence. check
- Se o jogador esgotar as tentativas, ele perde e a palavra secreta é revelada. check
- O jogo pode ser jogado com palavras de diferentes categorias, como animais, frutas, etc. check
- O jogo vai ter um registro das palavras já jogadas, para evitar repetições e registra as vitórias. check
'''

import time

letras_erradas = []
letras_certas = []
categorias = {'animais': ['cachorro', 'gato', 'elefante', 'leão', 'tigre'],
             'frutas': ['banana', 'maçã', 'laranja', 'uva', 'morango'],
             'objetos': ['Mesa', 'cadeira', 'televisão', 'celular', 'livro']}
tentativas = 6

def limpar_tela():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sortear_palavra(escolha):
    chave = list(categorias.keys())[escolha]
    categoria = categorias[chave]
    import random
    palavra = random.choice(categoria)
    categoria.remove(palavra)
    categorias[chave] = categoria
    return palavra

def escolher_categoria():
    limpar_tela()
    print("Escolha uma categoria:")
    for i, categoria in enumerate(categorias.keys()):
        print(f"{i + 1}. {categoria}")
    escolha = int(input("Digite o número da categoria: ")) - 1
    if escolha < 0 or escolha >= len(categorias):
        print("Escolha inválida. Tente novamente.")
        time.sleep(2)
        return escolher_categoria()
    return sortear_palavra(escolha)

def tratar_palavra(palavra):
    import unicodedata
    return "".join(
        c for c in unicodedata.normalize('NFKD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

def atualizar_tela():
    limpar_tela()
    print("Bem-vindo ao Jogo da Forca!")
    print(f"{tentativas-len(letras_erradas)} tentativas restantes.")
    
    for letra in palavra:
        if letra in letras_certas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")
    return
    
while True:
    palavra = escolher_categoria()
    palavra_correta = palavra
    palavra = tratar_palavra(palavra)

    atualizar_tela()
    tratar_palavra(palavra)
    palavra_adivinhada = False

    while not palavra_adivinhada and len(letras_erradas) < tentativas:
        letra = input("\nDigite uma letra: ").lower()
    
        if letra in letras_certas: # letra já foi
            print("Você já tentou essa letra. Tente outra.")
            time.sleep(1)
        elif letra in palavra: # letra certa
            letras_certas.append(letra)
        elif letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            time.sleep(1)
        else: # letra errada
            letras_erradas.append(letra)
    
        atualizar_tela()

        qtd_letras_certas = 0
        for letra in palavra:
            if letra in letras_certas:
                qtd_letras_certas += 1
    
        if qtd_letras_certas == len(palavra):
            print(f'Parabéns! Você adivinhou a palavra: {palavra_correta}!')
            time.sleep(2)
            palavra_adivinhada = True
        elif len(letras_erradas) == tentativas:
            print("Você perdeu! A palavra era:", palavra_correta)
            time.sleep(2)

    letras_certas.clear()
    letras_erradas.clear()
    tentativas = 6

