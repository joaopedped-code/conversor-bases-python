# Conversor e Calculadora de Bases Numéricas

Este projeto em Python oferece um conjunto de ferramentas para trabalhar com a conversão e a aritmética de números em diferentes bases numéricas, de 2 a 62. Ele é composto por duas classes principais: `Conversor` e `OperaBase`.

## Funcionalidades

- **Conversão Flexível**: Converte números entre qualquer base de 2 a 62.
- **Suporte a Ponto Flutuante**: Realiza conversões e operações com números inteiros e de ponto flutuante.
- **Detecção Automática de Base**: Reconhece automaticamente a base de strings com prefixos padrão (`0b` para binário, `0o` para octal, `0x` para hexadecimal).
- **Aritmética entre Bases**: Permite realizar operações matemáticas (`+`, `-`, `*`, `/`, `//`, etc.) diretamente entre números de bases diferentes.
- **Orientado a Objetos**: A lógica é encapsulada em classes fáceis de usar e estender.

---

## Como Usar

### `Conversor`: Para Conversões Diretas

A classe `Conversor` é ideal para quando você precisa apenas converter um número de uma base para outra.

#### Importando a classe
```python
from converte import Conversor
```

#### Exemplo 1: Convertendo um número inteiro (base 10)

Ao instanciar a classe com um número, você pode acessar suas representações em outras bases.

```python
conv = Conversor(26)

print(f"Decimal:     {conv.decimal}")     # Saída: 26
print(f"Hexadecimal: {conv.hexadecimal}") # Saída: 1A
print(f"Binário:     {conv.binario}")     # Saída: 11010
print(f"Octal:       {conv.octal}")       # Saída: 32
```

#### Exemplo 2: Convertendo uma string (especificando a base)

Se você tem uma string, pode especificar sua base de origem.

```python
conv_binario = Conversor('1100.11', base_origem=2)

print(f"O binário '1100.11' em decimal é: {conv_binario.decimal}") # Saída: 12.75
```

#### Exemplo 3: Usando prefixos

A classe detecta a base automaticamente se um prefixo for usado.

```python
conv_hex = Conversor('0x1A') # Base 16 detectada

print(f"O hexadecimal '0x1A' em decimal é: {conv_hex.decimal}") # Saída: 26
```

---

### `OperaBase`: Para Cálculos Aritméticos

A classe `OperaBase` herda de `Conversor` e foi projetada para realizar operações matemáticas entre números, não importando a base em que eles estão. Todas as operações (`+`, `-`, `*`, `/`, `**`, `==`, `>`, etc.) são suportadas.

#### Importando a classe
```python
from opera_base import OperaBase
```

#### Exemplo 1: Somando números de bases diferentes

Você pode somar um número hexadecimal com um binário diretamente. O resultado é um novo objeto `OperaBase` com o valor decimal correto.

```python
num_hex = OperaBase('F', base_origem=16)  # Valor decimal: 15
num_bin = OperaBase('101', base_origem=2) # Valor decimal: 5

resultado = num_hex + num_bin

print(f"O resultado da soma é: {resultado.decimal}") # Saída: 20
print(f"O resultado em hexadecimal é: {resultado.hexadecimal}") # Saída: 14
```

#### Exemplo 2: Operando com inteiros e strings

A classe é flexível e permite operar com tipos nativos do Python.

```python
num_a = OperaBase(100)

# Subtrai um inteiro
resultado1 = num_a - 25
print(f"100 - 25 = {resultado1.decimal}") # Saída: 75

# Multiplica por uma string com prefixo
resultado2 = num_a * '0b10' # 100 * 2
print(f"100 * '0b10' = {resultado2.decimal}") # Saída: 200
```

#### Exemplo 3: Usando o parâmetro `other_base`

Para operar com strings que **não** têm prefixo, você pode definir uma base padrão com o parâmetro `other_base`.

```python
# Tratar strings sem prefixo como octal (base 8)
calculadora = OperaBase(50, other_base=8)

# '10' será interpretado como octal, que é 8 em decimal
resultado = calculadora + '10' # 50 + 8

print(f"50 + '10' (octal) = {resultado.decimal}") # Saída: 58
```

## Exemplos Completos

Para ver uma lista exaustiva de exemplos, incluindo operações encadeadas, tratamento de erros e casos de uso com ponto flutuante, consulte o arquivo `exemplos.py`.