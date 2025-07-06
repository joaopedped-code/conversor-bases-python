from __future__ import annotations 
from Converso.converte import Conversor
from typing import Union, Callable
import operator
class OperaBase(Conversor):
    def __init__(self, numero: Union[Conversor,float,int, str], base_origem=10, other_base=2):
        '''
        Construtor da classe OperaBase.

        Args:
            numero (Union[Conversor,float,int, str]): O número a ser convertido.
            base_origem (int): A base do número de entrada.
            other_base (int): A base do número que será operador com o OperaBase.
        '''
        super().__init__(numero, base_origem)
        self.other_base = other_base

    def _verificar_operando(self, other: Union[int, str, OperaBase, Conversor], nome_operacao: str) -> int:
        """
        Converte o operando para inteiro (decimal), independentemente de seu tipo.

        Args:
            other: O outro operando (int, str ou OperaBase).
            nome_operacao: Nome da operação (apenas para mensagens de erro).

        Returns:
            int: Valor decimal do operando.
        """
        match other:
            case OperaBase() | Conversor():
                return other.decimal
            case int():
                return other
            case str():
                return Conversor(other, base_origem=self.other_base).decimal
            case _:
                raise TypeError(f"Tipo não suportado para {nome_operacao}: {type(other)}")

            

    def __add__(self, other): return self._operar(other,  operator.add)
    def __sub__(self, other): return self._operar(other,  operator.sub)
    def __mul__(self, other): return self._operar(other,  operator.mul)
    def __truediv__(self, other): 
        if self._verificar_operando(other, 'divisão') == 0:
            raise ZeroDivisionError("Divisão por zero.")
        return self._operar(other, operator.truediv)
    def __floordiv__(self, other): 
        if self._verificar_operando(other, 'divisão') == 0:
            raise ZeroDivisionError("Divisão por zero.")
        return self._operar(other, operator.floordiv)
    def __mod__(self, other): return self._operar(other, operator.mod)
    def __pow__(self, other): return self._operar(other, operator.pow)
    def __radd__(self, other): return self.__add__(other)
    def __rsub__(self, other): return OperaBase(other, base_origem=self.other_base) - self
    def __rmul__(self, other): return self.__mul__(other)
    def __rfloordiv__(self, other): return OperaBase(other, base_origem=self.other_base) // self
    def __rtruediv__(self, other): return OperaBase(other, base_origem=self.other_base) / self
    def __rmod__(self, other): return OperaBase(other, base_origem=self.other_base) % self
    def __rpow__(self, other): return OperaBase(other, base_origem=self.other_base) ** self
    def __eq__(self, other):
        if isinstance(other, (OperaBase, Conversor)):
            return self.decimal == other.decimal
        return self.decimal == other

    def __lt__(self, other):
        if isinstance(other, (OperaBase, Conversor)):
            return self.decimal < other.decimal
        return self.decimal < other

    def __le__(self, other):
        if isinstance(other, (OperaBase, Conversor)):
            return self.decimal <= other.decimal
        return self.decimal <= other

    def __gt__(self, other):
        if isinstance(other, (OperaBase, Conversor)):
            return self.decimal > other.decimal
        return self.decimal > other

    def __ge__(self, other):
        if isinstance(other, (OperaBase, Conversor)):
            return self.decimal >= other.decimal
        return self.decimal >= other

    def __ne__(self, other):
        if isinstance(other, (OperaBase, Conversor)):
            return self.decimal != other.decimal
        return self.decimal != other


    
    def _operar(self, other: Union[int, str, OperaBase,Conversor], func: Callable[[int, int], int]) -> OperaBase:
        """
        Executa uma operação binária entre self e other, usando a função passada.

        Args:
            other: O outro operando (int, str ou OperaBase).
            func: Uma função que recebe dois inteiros e retorna um inteiro (ex: operator.add).

        Returns:
            OperaBase: Resultado da operação.
        """
        valor = self._verificar_operando(other, "operação")
        return OperaBase(func(self.decimal, valor), base_origem=10)

