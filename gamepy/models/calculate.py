#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


class Calcular:
    """
    Classe que define o jogo, com sua dificuldade,
    valores, operações e resultado
    """

    def __init__(self: object, dificuldade: int, /) -> None:
        self._dificuldade: int = dificuldade
        self._valor1: int = self._gerar_valor
        self._valor2: int = self._gerar_valor
        self._operacao: int = randint(1, 3)
        self._resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self._dificuldade

    @property
    def valor1(self: object) -> int:
        return self._valor1

    @property
    def valor2(self: object) -> int:
        return self._valor2

    @property
    def operacao(self: object) -> int:
        return self._operacao

    @property
    def resultado(self: object) -> int:
        return self._resultado

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return (
            f'Valor 1: {self.valor1}\n'
            f'Valor 2: {self.valor2}\n'
            f'Dificuldade: {self.dificuldade}\n'
            f'Operação: {op!r}'
        )

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int, /) -> bool:
        certo: bool = False
        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(
            f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}'
        )
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
