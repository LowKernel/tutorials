# O programa para imprimir "Hello, World!" é o mais básico.
print("Hello, World!")
print(3)
print("I love " + "Python!")  # Use o + para concatenar strings.
print(10 + 3)  # Aqui, o + está somando porque os dois valores são números.
print("Tenho ", 18, " anos.")  # Passagem de múltiplos argumentos com tipos diferentes.
print(10, " Bananas " + "e ", 7, " maçãs")  # Passagem de múltiplos argumentos, com ',' e '+'.

# --------------------------------------------------

# Para descobrir o tipo de um dado, use type().
print(type(5))       # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type("João"))  # <class 'str'>
print(type(True))    # <class 'bool'>

# --------------------------------------------------

# Aprender sobre variáveis é fundamental em programação. Existem regras para nomear variáveis:
# --------------------------------------------------
# Permitido: As variáveis devem começar com uma letra (a-z, A-Z) ou um sublinhado (_).
# Não Permitido: Não podem começar com números (0-9) ou caracteres especiais (%, &, etc.).
# Permitido: Após o primeiro caractere, as variáveis podem conter letras, números e sublinhados.
# Não Permitido: Não podem conter espaços ou caracteres especiais.
# Não Permitido: Não podem ser palavras reservadas da linguagem Python (e.g., class, for, if, while, else, import, etc.).
# --------------------------------------------------
# Permitido:
variavel = ""
_variavel = ""
variavel123 = ""
variavel_exemplo = ""
# Não Permitido:
# 123variavel = ""
# variavel-exemplo = ""
# variavel exemplo = ""
# class = ""

# Para uma lista de palavras reservadas do Python, acesse:
# https://www.inf.pucrs.br/flash/progbio/aulas/seq/build/progbio/VariableNamesandKeywords.html

nome = "Pedro"
idade = 16
altura = 1.76
peso = 67.3
materia_preferida = "matemática"
numero_favorito = "pi"
PI = 3.14  # Maiúsculas geralmente usadas para variáveis constantes
maior_de_idade = False

print("Nome: " + nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Peso: ", peso)
print("É maior de idade?: ", maior_de_idade)
print("Número favorito: ", numero_favorito)
print("Valor do pi: ", PI)

# --------------------------------------------------

# Com f-strings em Python, você não precisa se preocupar com concatenação ou tipos de dados.
# Existem duas formas de usar f-strings:

print(f"Meu nome é {nome}, tenho {idade} anos.")  # Usando f-strings
print("Gosto de {} e meu número favorito é o {}: {}".format(materia_preferida, numero_favorito, PI))  # Usando format()

# Nota: As f-strings são recomendadas por serem mais simples e legíveis.
