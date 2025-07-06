from Converso.converte import Conversor
from Converso.opera_base import OperaBase

# --- Exemplos de Uso da Classe Conversor ---
print("=" * 60)
print("EXEMPLOS COMPLETOS DE USO DAS CLASSES CONVERSOR E OPERABASE")
print("=" * 60)

print("=" * 40)
print("EXEMPLOS DA CLASSE CONVERSOR")
print("=" * 40)

# 1. Conversão a partir de um inteiro (base 10)
print("\n--- 1. Convertendo o número inteiro 255 ---")
conv_int = Conversor(255)
print(f"Número Original: {conv_int.numero_original} (base 10)")
print(f"  - Decimal:     {conv_int.decimal}")
print(f"  - Binário:     {conv_int.binario}")
print(f"  - Hexadecimal: {conv_int.hexadecimal}")
print(f"  - Octal:       {conv_int.octal}")

# 2. Conversão a partir de uma string com prefixo (detecção automática da base)
print("\n--- 2. Convertendo a string '0x1A' (Hexadecimal) ---")
conv_hex_str = Conversor('0x1A')
print(f"Número Original: '{conv_hex_str.numero_original}'")
print(f"  - Decimal:     {conv_hex_str.decimal}") # 26
print(f"  - Binário:     {conv_hex_str.binario}") # 11010

# 3. Conversão a partir de uma string sem prefixo, especificando a base
print("\n--- 3. Convertendo a string '1010' da base 2 ---")
conv_bin_str = Conversor('1010', base_origem=2)
print(f"Número Original: '{conv_bin_str.numero_original}' (base {conv_bin_str.base_original})")
print(f"  - Decimal:     {conv_bin_str.decimal}") # 10
print(f"  - Hexadecimal: {conv_bin_str.hexadecimal}") # A

# 4. Conversão de números com ponto flutuante
print("\n--- 4. Convertendo números de ponto flutuante ---")
# De decimal (float) para outras bases
conv_float = Conversor(12.75)
print(f"Número Original: {conv_float.numero_original} (base 10)")
print(f"  - Binário:     {conv_float.binario}")     # 1100.11
print(f"  - Hexadecimal: {conv_float.hexadecimal}") # C.C
print(f"  - Octal:       {conv_float.octal}")       # 14.6

# De uma string em outra base para decimal
conv_float_str = Conversor('A.4', base_origem=16)
print(f"Número Original: '{conv_float_str.numero_original}' (base 16)")
print(f"  - Decimal:     {conv_float_str.decimal}") # 10.25

# 5. Usando métodos de conversão diretamente
print("\n--- 5. Usando métodos de conversão avulsos ---")
# Não é necessário criar um objeto para conversões rápidas
c = Conversor(0) # Objeto genérico para acessar os métodos
resultado_base_para_base = c.de_base_para_base('777', base_origem=8, base_destino=10)
print(f"Conversão de '777' (base 8) para base 10: {resultado_base_para_base}") # 511

resultado_decimal_para_base = c.de_decimal_para_base(511, base_destino=16)
print(f"Conversão de 511 (decimal) para base 16: {resultado_decimal_para_base}") # 1FF


# --- Exemplos de Uso da Classe OperaBase ---
print("\n\n" + "=" * 40)
print("EXEMPLOS DA CLASSE OPERABASE")
print("=" * 40)

# 1. Operações básicas com diferentes tipos
print("\n--- 1. Operações básicas ---")
op_a = OperaBase('A', base_origem=16) # op_a tem o valor decimal 10
print(f"Objeto 'a': OperaBase('A', base_origem=16) -> Decimal: {op_a.decimal}")

# Soma com inteiro
res_soma_int = op_a + 5
print(f"a + 5 = {res_soma_int.decimal} (Decimal)")

# Subtração com string com prefixo
res_sub_str = op_a - '0b11' # 10 - 3
print(f"a - '0b11' = {res_sub_str.decimal} (Decimal)")

# Multiplicação com outro objeto OperaBase
op_b = OperaBase(20, base_origem=10)
res_mul_obj = op_a * op_b # 10 * 20
print(f"a * OperaBase(20) = {res_mul_obj.decimal} (Decimal)")

# 2. Usando o parâmetro 'other_base'
print("\n--- 2. Usando 'other_base' para operar com strings sem prefixo ---")
# 'other_base=8' diz para a classe tratar strings sem prefixo como Octal
op_c = OperaBase(100, base_origem=10, other_base=8)
print(f"Objeto 'c': OperaBase(100, other_base=8)")

res_other_base = op_c + '10' # 100 (decimal) + 10 (octal, que é 8 em decimal)
print(f"c + '10' = {res_other_base.decimal} (Decimal)") # Esperado: 108

# 3. Operações com ponto flutuante
print("\n--- 3. Operações com ponto flutuante ---")
op_float_a = OperaBase(10.5)
op_float_b = OperaBase('1.1', base_origem=2) # 1.5 em decimal
res_float = op_float_a * op_float_b # 10.5 * 1.5
print(f"10.5 * '1.1' (binário) = {res_float.decimal}") # Esperado: 15.75

# 4. Acessando as representações do resultado
print("\n--- 4. Acessando as representações do resultado ---")
op_d = OperaBase('F', base_origem=16) # 15
resultado_final = op_d + 1 # 16
print(f"O resultado da operação 'F' (hex) + 1 é {resultado_final.decimal}")
print(f"  - Em Hexadecimal: {resultado_final.hexadecimal}") # 10
print(f"  - Em Binário:     {resultado_final.binario}")     # 10000
print(f"  - Em Octal:       {resultado_final.octal}")       # 20

# 5. Operações encadeadas e reversas
print("\n--- 5. Operações encadeadas e reversas ---")
op_1 = OperaBase(10)
op_2 = OperaBase(5)
op_3 = OperaBase(2)
res_encadeado = op_1 + op_2 * op_3 # 10 + (5 * 2) = 20
print(f"10 + 5 * 2 = {res_encadeado.decimal}")

res_reverso = 100 - op_1 # 100 - 10
print(f"100 - OperaBase(10) = {res_reverso.decimal}")

# 6. Divisão
print("\n--- 6. Divisão ---")
op_div = OperaBase(21)
res_div_true = op_div / 2 # Divisão real
print(f"21 / 2 = {res_div_true.decimal}") # 10.5

res_div_floor = op_div // 2 # Divisão inteira
print(f"21 // 2 = {res_div_floor.decimal}") # 10

print("=== Exemplos de operações com diferentes bases ===")

# Criando objetos OperaBase a partir de strings em diferentes bases
binario = OperaBase('1010', base_origem=2)   # 10 decimal
hexadecimal = OperaBase('1F', base_origem=16) # 31 decimal
octal = OperaBase('17', base_origem=8)       # 15 decimal
decimal = OperaBase(20)                       # já é decimal

print(f"Binário '1010' -> decimal: {binario.decimal}")
print(f"Hexadecimal '1F' -> decimal: {hexadecimal.decimal}")
print(f"Octal '17' -> decimal: {octal.decimal}")
print(f"Decimal 20 -> decimal: {decimal.decimal}")

# Soma
soma = binario + hexadecimal + octal + decimal
print(f"Soma: 10 + 31 + 15 + 20 = {soma.decimal}")

# Multiplicação misturada: (binário * hexadecimal) + (octal * decimal)
mult1 = binario * hexadecimal
mult2 = octal * decimal
resultado = mult1 + mult2
print(f"Multiplicação misturada: (10 * 31) + (15 * 20) = {resultado.decimal}")

# Divisão: hexadecimal dividido por octal
divisao = hexadecimal / octal
print(f"Divisão: 31 / 15 = {divisao.decimal}")

# Operação reversa: número decimal menos número hexadecimal
rev_sub = 100 - hexadecimal
print(f"100 - 31 (hexadecimal) = {rev_sub.decimal}")

# Operação com string sem prefixo, usando 'other_base'
operacao_other_base = OperaBase(10, other_base=8) + '21'  # 10 decimal + 17 decimal (octal 21)
print(f"10 + '21' (interpreted as octal) = {operacao_other_base.decimal}")


# 1. Operações com bases variadas, incluindo decimais fracionários
print("\n--- 1. Operações com bases variadas (inteiros e decimais) ---")
bin_frac = OperaBase('101.1', base_origem=2)        # 5.5 decimal
hex_frac = OperaBase('A.C', base_origem=16)          # 10.75 decimal
resultado1 = bin_frac + hex_frac
print(f"Binário '101.1' + Hexadecimal 'A.C' = {resultado1.decimal} (decimal)")
print(f"  - Em binário: {resultado1.binario}")
print(f"  - Em hexadecimal: {resultado1.hexadecimal}")

# 2. Operações reversas e other_base
print("\n--- 2. Operações reversas e uso de other_base ---")
rev_sub = 100 - OperaBase('1F', base_origem=16)      # 100 - 31
print(f"100 - '1F' (hex) = {rev_sub.decimal}")

op_with_other_base = OperaBase(10, other_base=8) + '21' # 10 + 17 (octal '21')
print(f"10 + '21' (interpretado como octal) = {op_with_other_base.decimal}")

# 3. Bases altas: 36 e 62
print("\n--- 3. Trabalhando com bases maiores ---")
base36_a = OperaBase('Z', base_origem=36)            # 35 decimal
base62_b = OperaBase('1z', base_origem=62)           # 123 decimal
print(f"Base 36 'Z' -> decimal: {base36_a.decimal}")
print(f"Base 62 '1z' -> decimal: {base62_b.decimal}")
print(f"Soma base36 + base62 = {base36_a + base62_b}")

# 4. Strings com e sem prefixos
print("\n--- 4. Strings com prefixo e other_base ---")
pref_bin = OperaBase('0b1010')                        # detecta base 2
pref_hex = OperaBase('0x1F')                          # detecta base 16
no_pref_oct = OperaBase('21', other_base=8)           # base 8
print(f"'0b1010' = {pref_bin.decimal}")
print(f"'0x1F' = {pref_hex.decimal}")
print(f"'21' sem prefixo com other_base=8 = {no_pref_oct.decimal}")

# 5. Encadeamento e combinações complexas
print("\n--- 5. Operações encadeadas complexas ---")
op_encadeado = (OperaBase('F', 16) + '11' + OperaBase('1001', 2)) * OperaBase(2.5)
print(f"(F_hex + '11' + 1001_bin) * 2.5 = {op_encadeado.decimal}")

# 6. Tratamento de erros
print("\n--- 6. Tratamento de erros ---")
try:
    OperaBase('G', base_origem=16)  # G não é válido em hex
except ValueError as e:
    print(f"Erro ao criar OperaBase: {e}")

try:
    OperaBase('101') / 0
except ZeroDivisionError as e:
    print(f"Erro de divisão: {e}")

try:
    OperaBase('123', base_origem=70)  # base inválida
except ValueError as e:
    print(f"Erro de base inválida: {e}")

# 7. Comparações (se implementadas)
print("\n--- 7. Comparações ---")
a = OperaBase('A', 16)  # 10
b = OperaBase('9', 10)  # 9
print(f"a ({a.decimal}) > b ({b.decimal}): {a > b}")
print(f"a ({a.decimal}) == 10: {a == 10}")
print(f"b ({b.decimal}) < 15: {b < 15}")

# 8. Conversão direta base-a-base (ponto flutuante)
print("\n--- 8. Conversão direta base-a-base ---")
c = Conversor(10.5, base_origem=10)
num_base16 = '1A.3F'
conv_16_2 = c.de_base_para_base(num_base16, base_origem=16, base_destino=2)
print(f"'{num_base16}' base 16 para base 2: {conv_16_2}")

# 9. Operações com números negativos
print("\n--- 9. Operações com números negativos ---")
neg = OperaBase(-15)
pos = OperaBase('F', 16)
resultado_neg = neg + pos
print(f"-15 + 'F' (15) = {resultado_neg.decimal}")

# 10. Exibir passo a passo da conversão (se disponível)
# Supondo que sua classe Conversor tenha um modo verbose (mostrar_processo)
print("\n--- 10. Passo a passo (modo mostrar_processo) ---")
try:
    c_verbose = Conversor('1A.4', base_origem=16)
    # Imagine que há um método mostrar_processo ou parâmetro para imprimir passos:
    # c_verbose.mostrar_processo = True
    # Para exemplo, só mostrando o valor:
    print(f"Decimal de '1A.4' (hex): {c_verbose.decimal}")
except AttributeError:
    print("Modo mostrar_processo não implementado nesta versão.")

print("\n" + "=" * 60)
print("FIM DOS EXEMPLOS COMPLETOS")
print("=" * 60)
