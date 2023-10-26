import random


def jogar_for():
    imprime_msg_de_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_a = inicializa_letras_acertadas(palavra_secreta)

    erros = 0
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = pede_chute()

        index = 0
        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_a, index)
        else:
            erros += 1
        print(letras_a)

        enforcou = erros == 6
        acertou = "_" not in letras_a

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")


def imprime_msg_de_abertura():
    print("***************************************")
    print("************Jogo da Forca**************")
    print("***************************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    #   print(palavras)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper().lower()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    letras_a = ["_" for letra in palavra_secreta]
    return letras_a


def pede_chute():
    chute = input("Qual a letra?\n")
    chute = chute.strip().upper().lower()
    return chute


def marca_chute_correto(palavra_secreta, chute, letras_a, index):
    for letra in palavra_secreta:
        if chute == letra:
            letras_a[index] = letra
            # print("Encontrei a letra {} na posição {}".format(letra, index))
        index += 1  # (index = index + 1)


if __name__ == "__main__":
    jogar_for()
