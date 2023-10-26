import random


def jogar_adv():
    print("***************************************")
    print("Adivinhe o número secreto entre 1 e 100")
    print("***************************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    rodada = 1
    pontos = 0

    print("Escolha a dificuldade:")
    dificuldade = int(input("(1)Fácil (2)Médio (3)Difícil\n"))

    if dificuldade == 1:
        tentativas = 20
        pontos = 100
    elif dificuldade == 2:
        tentativas = 10
        pontos = 200
    elif dificuldade == 3:
        tentativas = 5
        pontos = 250
    else:
        print("Selecione uma dificuldade válida!")

    for rodada in range(1, tentativas + 1):
        print("Rodada {} de {}".format(rodada, tentativas))
        chute = int(input("Digite o número secreto: "))

        if chute < 1 or chute > 100:
            print("Digite um número entre 1 e 100")
            continue

        acerto = numero_secreto == chute
        alto = chute > numero_secreto
        baixo = chute < numero_secreto

        print("Você digitou \n", chute)

        if acerto:
            print("Você acertou com {} pontos!".format(pontos))
            break
        else:
            if alto:
                print("Errou! Chutou alto!")
            elif baixo:
                print("Errou! Chutou baixo!")
            ponto_p = 20
            pontos = pontos - ponto_p

        if rodada == tentativas:
            print("Fim do jogo!\n O número secreto era {}".format(numero_secreto))


if __name__ == "__main__":
    jogar_adv()
