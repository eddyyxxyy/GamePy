#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.calculate import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(
        input('Informe o nível de dificuldade desejado: [1, 2, 3 ou 4]\n-> ')
    )

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    if continuar := int(
        input('Deseja continuar no jogo? [1 - Sim, 0 - Não]\n-> ')
    ):
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
