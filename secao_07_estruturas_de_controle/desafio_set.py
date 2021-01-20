PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
# se usarmos o ! no final de uma palavra ele considera o ! como sendo
# parte da palavra
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

if __name__ == "__main__":
    for texto in textos:
        intersecao = PALAVRAS_PROIBIDAS.intersection(
            set(texto.lower().split()))
        if intersecao:
            print("Possui a palavra: ", intersecao)
        else:
            print("Não possui palavras proibidas")
