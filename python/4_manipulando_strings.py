# Manipulação de Strings em Python

# --------------------------------------------------

# 1. Repetição de Strings
# Você pode repetir uma string usando o operador '*'.
repetir = "Python! " * 3
print(repetir)  # Saída: Python! Python! Python!

# --------------------------------------------------

# 2. Acessando Caracteres em Strings
# Você pode acessar caracteres individuais em uma string usando índices. O índice começa em 0.
palavra = "Python"
print(palavra[0])  # Saída: P (primeiro caractere)
print(palavra[-1])  # Saída: n (último caractere)

# --------------------------------------------------

# 3. Fatiamento (Slicing) de Strings
# Você pode extrair uma parte de uma string usando fatiamento (slicing).
# Sintaxe: string[início:fim:passo]
fatia = palavra[0:3]  # Extrai do índice 0 até 2 (o índice final não é incluído)
print(fatia)  # Saída: Pyt
fatia_com_passo = palavra[0:6:2]  # Extrai do índice 0 ao 5, pulando de 2 em 2
print(fatia_com_passo)  # Saída: Pto

# --------------------------------------------------

# 4. Tamanho da String
# Para saber o tamanho (número de caracteres) de uma string, use a função len().
tamanho = len(palavra)
print(tamanho)  # Saída: 6

# --------------------------------------------------

# 5. Métodos de String
# Strings em Python têm vários métodos que podem ser usados para manipular ou consultar as strings.

# 5.1. .upper() e .lower() - Converter para maiúsculas ou minúsculas
print(palavra.upper())  # Saída: PYTHON
print(palavra.lower())  # Saída: python

# 5.2. .strip() - Remover espaços em branco do início e fim da string
espacos = "   Espaços em branco   "
print(espacos.strip())  # Saída: "Espaços em branco"

# 5.3. .replace() - Substituir partes da string
frase = "Eu gosto de Python"
nova_frase = frase.replace("Python", "programar")
print(nova_frase)  # Saída: Eu gosto de programar

# 5.4. .split() - Dividir uma string em uma lista de substrings
lista_palavras = frase.split()  # Divide por espaços por padrão
print(lista_palavras)  # Saída: ['Eu', 'gosto', 'de', 'Python']

# 5.5. .join() - Unir elementos de uma lista em uma string
unido = " ".join(lista_palavras)
print(unido)  # Saída: Eu gosto de Python

# --------------------------------------------------

# 6. Verificação de Substrings
# Você pode verificar se uma string contém outra string usando o operador `in`.
print("Python" in frase)  # Saída: True
print("Java" in frase)  # Saída: False

# --------------------------------------------------

# 7. Formatação de Strings
# Além das f-strings, existem outras maneiras de formatar strings, como vimos antes.

# 7.1. Usando o método .format()
frase_formatada = "Eu amo {}!".format("Python")
print(frase_formatada)  # Saída: Eu amo Python!

# 7.2. Usando f-strings
linguagem = "Python"
print(f"Eu amo {linguagem}!")  # Saída: Eu amo Python!

# --------------------------------------------------

# 8. Substituição de Caractere
# Para substituir um caractere específico em uma string, você pode combinar fatiamento com concatenação.
texto = "Pythn"
texto_corrigido = texto[:4] + "o" + texto[4:]
print(texto_corrigido)  # Saída: Python

# --------------------------------------------------

# 9. Strings Imutáveis
# Em Python, as strings são imutáveis, o que significa que você não pode alterar os caracteres individuais em uma string existente.
# No entanto, você pode criar novas strings a partir de manipulações.

exemplo = "Python"
# exemplo[0] = "J"  # Isso causaria um erro
novo_exemplo = "J" + exemplo[1:]  # Criar uma nova string com a alteração
print(novo_exemplo)  # Saída: Jython

# --------------------------------------------------

# A manipulação de strings é uma habilidade essencial em Python, e há muitas outras funções e métodos disponíveis.
# Continue explorando e experimentando para aprofundar seu conhecimento.