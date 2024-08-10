# Compreensão de Listas em Python

# --------------------------------------------------

# 1. O que é Compreensão de Listas?
# A Compreensão de Listas é uma maneira concisa e eficiente de criar listas em Python.
# Ela permite gerar uma nova lista aplicando uma expressão a cada item de uma sequência existente.

# --------------------------------------------------

# 2. Sintaxe Básica
# A sintaxe básica de uma compreensão de lista é:
# [expressão for item in iterável]

# Exemplo: Criar uma lista de quadrados dos números de 0 a 4
quadrados = [x**2 for x in range(5)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16]

# --------------------------------------------------

# 3. Compreensão de Listas com Condição
# Você pode adicionar uma condição à compreensão de lista para filtrar os itens.

# Exemplo: Criar uma lista de quadrados apenas dos números pares
quadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrados_pares)  # Saída: [0, 4, 16, 36, 64]

# --------------------------------------------------

# 4. Compreensão de Listas com Múltiplas Expressões
# É possível usar compreensões de lista com múltiplas expressões.

# Exemplo: Criar uma lista de tuplas (x, y) onde x e y vão de 0 a 2
pares = [(x, y) for x in range(3) for y in range(3)]
print(pares)
# Saída:
# [(0, 0), (0, 1), (0, 2),
#  (1, 0), (1, 1), (1, 2),
#  (2, 0), (2, 1), (2, 2)]

# --------------------------------------------------

# 5. Aplicando Funções em Compreensão de Listas
# Você pode aplicar funções diretamente na expressão da compreensão de lista.

# Exemplo: Converter uma lista de strings para maiúsculas
nomes = ["ana", "maria", "joão"]
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)  # Saída: ['ANA', 'MARIA', 'JOÃO']

# --------------------------------------------------

# 6. Aninhamento de Compreensões de Listas
# Compreensões de listas podem ser aninhadas, ou seja, você pode usar uma compreensão de lista dentro de outra.

# Exemplo: Criar uma lista de listas onde cada sublista contém quadrados de números
lista_de_listas = [[x**2 for x in range(3)] for _ in range(3)]
print(lista_de_listas)
# Saída:
# [[0, 1, 4],
#  [0, 1, 4],
#  [0, 1, 4]]

# --------------------------------------------------

# 7. Compreensão de Listas vs. Laços `for`
# Compreensões de listas podem ser mais concisas do que usar laços `for` para criar listas, mas às vezes o código pode ser menos legível se for muito complexo.

# Exemplo com laço `for`:
lista = []
for x in range(5):
    lista.append(x**2)
print(lista)  # Saída: [0, 1, 4, 9, 16]

# Exemplo com compreensão de lista:
lista = [x**2 for x in range(5)]
print(lista)  # Saída: [0, 1, 4, 9, 16]

# --------------------------------------------------

# 8. Cuidados com a Compreensão de Listas
# Embora as compreensões de listas sejam poderosas, você deve usá-las com cuidado. Se forem muito complexas, podem tornar o código mais difícil de entender.

# Exemplo de uma compreensão de lista complexa (evite quando possível):
lista_complexa = [x**2 for x in range(10) if x % 2 == 0 if x > 2]
print(lista_complexa)  # Saída: [16, 36, 64]

# --------------------------------------------------

# Compreensão de listas é uma ferramenta poderosa para criar e manipular listas de maneira concisa e eficiente. No entanto, é importante usá-la de forma equilibrada para manter a legibilidade do código.
