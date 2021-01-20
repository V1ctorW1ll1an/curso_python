# Jogar um dado de 6 lados por n vezes
# verificar se o numero retornado pelo dado é par ou impar
# se o numero for impar, continue a verificação
# se o numero for par, exiba uma mensagem de 'ACERTOU'
# se o numero do dado for impar, chame o else e imprima "IMPAR"
from random import randint


def sort_dado():
    return randint(1, 6)


if __name__ == "__main__":
    dado = sort_dado()
    for x in range(7):
        if x % 2 == 1:
            continue
        if x == dado:
            print("Você acertou! numero: ", x, "dado: ", dado)
            break
    else:
        print("Você errou! dado: ", dado)
