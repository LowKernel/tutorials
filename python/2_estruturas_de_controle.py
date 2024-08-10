# Operadores Aritméticos
a = 20
b = 8

# Adição
adicao = a + b  # Resultado: 28
print(f"Adição: {adicao}")

# Subtração
subtracao = a - b  # Resultado: 12
print(f"Subtração: {subtracao}")

# Multiplicação
multiplicacao = a * b  # Resultado: 160
print(f"Multiplicação: {multiplicacao}")

# Divisão
divisao = a / b  # Resultado: 2.5
print(f"Divisão: {divisao}")

# Divisão inteira
divisao_inteira = a // b  # Resultado: 2
print(f"Divisão inteira: {divisao_inteira}")

# Módulo
modulo = a % b  # Resultado: 4
print(f"Módulo: {modulo}")

# --------------------------------------------------

# Operadores de Comparação
numero1 = 12
numero2 = 15
numero3 = 10

igual = numero1 == numero2  # False
diferente = numero1 != numero3  # True
maior = numero2 > numero3  # True
menor = numero3 < numero1  # True
maior_ou_igual = numero1 >= numero3  # True
menor_ou_igual = numero2 <= numero1  # False

print(f"Igual: {igual}")
print(f"Diferente: {diferente}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Maior ou igual: {maior_ou_igual}")
print(f"Menor ou igual: {menor_ou_igual}")

# --------------------------------------------------

# Operadores Lógicos
x = True
y = False

# AND lógico
and_resultado = x and y  # False
print(f"AND lógico: {and_resultado}")

# OR lógico
or_resultado = x or y  # True
print(f"OR lógico: {or_resultado}")

# NOT lógico
not_resultado = not x  # False
print(f"NOT lógico: {not_resultado}")

# --------------------------------------------------

# Estrutura condicional

# Exemplo 1
numero = 7

if numero % 2 == 0:
    print("O número é par")

# Exemplo 2

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# Exemplo 3

numero = 0

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")

# Exemplo 4

idade = 20
renda = 4000

if idade >= 18 and renda >= 3000:
    print("Você é elegível para o empréstimo")
elif idade >= 18 and renda < 3000:
    print("Você precisa de uma renda maior para ser elegível")
else:
    print("Você não é elegível para o empréstimo")

# Exemplo 5

nota1 = 85
nota2 = 90
media = (nota1 + nota2) / 2

if media >= 70:
    print("Aprovado")
elif 50 <= media < 70:
    print("Recuperação")
else:
    print("Reprovado")