from __future__ import annotations 
from typing import Union

class Conversor(object):
    """
    Uma classe para realizar conversões entre bases numéricas.

    Suporta bases de 2 a 62. A classe pode ser instanciada com um número
    e sua base original, e então fornecer representações em outras bases
    (binário, octal, hexadecimal, etc.).
    """
    SIMBOLOS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'  # Suporta até base 62
    
    def __init__(self,numero: Union[Conversor,float,int, str], base_origem=10):
        """
        Inicializa o conversor com um número e sua base.

        Args:
            numero: O número a ser convertido. Pode ser um inteiro (assumido ser base 10), um float,
                    ou uma string. Strings com prefixos '0b', '0o', '0x' terão
                    sua base detectada automaticamente, ignorando `base_origem`, também pode ser um objeto Conversor .
            base_origem: A base do número de entrada, se não houver prefixo.
            mostrar_processo: Se True, imprime os passos da conversão de decimal para outras bases.
        """
        # Guarda os valores originais para referência
        self.numero_original = numero
        self.base_original = base_origem

        self.decimal = self._calcular_valor_decimal(self.numero_original, self.base_original)
        self.binario = self.de_decimal_para_base(self.decimal, 2)
        self.hexadecimal = self.de_decimal_para_base(self.decimal, 16)
        self.octal = self.de_decimal_para_base(self.decimal, 8)
        
    def _calcular_valor_decimal(self, valor, base_origem=10):
        """Método auxiliar para converter o número de entrada para decimal.
        
        
        Args:
            numero_decimal: O número a ser convertido. Pode ser um inteiro (base 10)
                    ou uma string.
                    
        Returns:
            int: O número convertido para decimal.
        """
        if isinstance(valor, int):
                return valor # Inteiros são sempre base 10
        numero_str = str(valor).lower()
        prefixos = {'0b': 2, '0o': 8, '0x': 16}

        prefixo = numero_str[:2]
        if prefixo in prefixos:
            base = prefixos[prefixo]
            valor_sem_prefixo = numero_str[2:]
            return self.de_base_para_decimal(valor_sem_prefixo, base)
        else:
            return self.de_base_para_decimal(numero_str, base_origem)
            
        
            
    
    def de_decimal_para_base(self, numero_decimal, base_destino, precisao=10):
        """
        Converte número decimal (int ou float) para base destino com suporte à parte fracionária.

        Args:
            numero_decimal (float): Número decimal a converter.
            base_destino (int): Base para converter.
            precisao (int): Quantidade máxima de dígitos para parte fracionária.

        Returns:
            str: Número convertido para a base destino, incluindo parte fracionária.
        """
        if base_destino > len(self.SIMBOLOS):
            raise ValueError(f'Base máxima suportada é {len(self.SIMBOLOS)}')

        if numero_decimal == 0:
            return '0'

        parte_inteira = int(numero_decimal)
        parte_fracionaria = numero_decimal - parte_inteira

        # Converte parte inteira
        restos = []
        if parte_inteira == 0:
            restos.append('0')
        else:
            while parte_inteira > 0:
                resto = parte_inteira % base_destino
                restos.append(self.SIMBOLOS[resto])
                parte_inteira = parte_inteira // base_destino
        resultado_parte_inteira = ''.join(restos[::-1])

        # Converte parte fracionária
        if parte_fracionaria == 0:
            return resultado_parte_inteira
        else:
            resultado_parte_fracionaria = []
            count = 0
            while parte_fracionaria > 0 and count < precisao:
                parte_fracionaria *= base_destino
                digito = int(parte_fracionaria)
                resultado_parte_fracionaria.append(self.SIMBOLOS[digito])
                parte_fracionaria -= digito
                count += 1
            return resultado_parte_inteira + '.' + ''.join(resultado_parte_fracionaria)


    def de_base_para_decimal(self, numero_em_string, base_de_origem):
        """
        Converte um número de uma base para decimal, incluindo parte fracionária.

        Args:
            numero_em_string (str): O número a ser convertido.
            base_de_origem (int): A base do número de entrada.

        Returns:
            float: O número convertido para decimal.
        """
        if base_de_origem < 2 or base_de_origem > 62:
            raise ValueError("A base deve estar entre 2 e 62.")

        if not numero_em_string:
            return 0

        # Normaliza letras de acordo com a base
        numero = str(numero_em_string)
        if base_de_origem <= 36:
            numero = numero.upper()

        if '.' in numero:
            parte_inteira, parte_fracionaria = numero.split('.')
        else:
            parte_inteira, parte_fracionaria = numero, ''

        resultado = 0

        # Parte inteira (da direita pra esquerda)
        for i, digito in enumerate(parte_inteira[::-1]):
            if digito not in self.SIMBOLOS[:base_de_origem]:
                raise ValueError(f"Caractere '{digito}' inválido para base {base_de_origem}")
            valor = self.SIMBOLOS.index(digito)
            resultado += valor * (base_de_origem ** i)

        # Parte fracionária (da esquerda pra direita)
        for i, digito in enumerate(parte_fracionaria, start=1):
            if digito not in self.SIMBOLOS[:base_de_origem]:
                raise ValueError(f"Caractere '{digito}' inválido para base {base_de_origem}")
            valor = self.SIMBOLOS.index(digito)
            resultado += valor * (base_de_origem ** -i)

        return resultado

    def de_base_para_base(self, numero: Union[int,str], base_origem, base_destino):
        '''
        Converte um número de uma base para outra.

        Args:
            numero (str): O número a ser convertido.
            base_origem (int): A base do número de entrada.
            base_destino (int): A base para a qual o número será convertido.

        Returns:
            str: O número convertido para a nova base.
        '''

        decimal = self.de_base_para_decimal(numero, base_origem)
        return self.de_decimal_para_base(decimal, base_destino)

    def __repr__(self):
        """Retorna uma representação legível do objeto, útil para depuração."""
        return str(self.decimal)
    