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
        pass

    @property
    def _gerar_resultado(self: object) -> int:
        pass

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

    def checar_resultado(self: object, resposta: int, /) -> bool:
        pass

    def mostrar_operacao(self: object) -> None:
        pass
