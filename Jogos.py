import Forca
import Adivinhacao


def jogos():
    print("***************************************")
    print("***********Escolha seu jogo************")
    print("***************************************")

    jogo = int(input("(1)Forca (2)Adivinhação"))

    if jogo == 1:
        print("Jogando Forca")
        Forca.jogar_for()
    elif jogo == 2:
        print("Jogando Adivinhação")
        Adivinhacao.jogar_adv()


if __name__ == "__main__":
    jogos()
