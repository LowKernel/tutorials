# Manipulação de Listas em Python

# --------------------------------------------------

# Listas em Python são coleções ordenadas de elementos que podem ser de tipos diferentes.
# Listas são mutáveis, o que significa que você pode alterar os elementos depois que a lista é criada.

# 1. Criando uma Lista
# Você pode criar uma lista usando colchetes [] e separando os elementos por vírgulas.
minha_lista = [1, 2, 3, 4, 5]
outra_lista = ["Python", 3.14, True]
lista_vazia = []

# --------------------------------------------------

# 2. Acessando Elementos da Lista
# Os elementos de uma lista podem ser acessados usando índices, começando em 0.
print(minha_lista[0])  # Saída: 1 (primeiro elemento)
print(outra_lista[1])  # Saída: 3.14 (segundo elemento)
print(minha_lista[-1])  # Saída: 5 (último elemento)

# --------------------------------------------------

# 3. Modificando Elementos da Lista
# Como as listas são mutáveis, você pode alterar os valores dos elementos após a criação da lista.
minha_lista[0] = 10  # Alterando o primeiro elemento
print(minha_lista)  # Saída: [10, 2, 3, 4, 5]

# --------------------------------------------------

# 4. Adicionando Elementos à Lista
# Você pode adicionar elementos a uma lista existente usando os métodos .append(), .insert(), ou .extend().

# 4.1. .append() - Adiciona um elemento ao final da lista.
minha_lista.append(6)
print(minha_lista)  # Saída: [10, 2, 3, 4, 5, 6]

# 4.2. .insert() - Insere um elemento em uma posição específica.
minha_lista.insert(1, 20)  # Insere 20 na posição 1
print(minha_lista)  # Saída: [10, 20, 2, 3, 4, 5, 6]

# 4.3. .extend() - Adiciona múltiplos elementos ao final da lista.
minha_lista.extend([7, 8, 9])
print(minha_lista)  # Saída: [10, 20, 2, 3, 4, 5, 6, 7, 8, 9]

# --------------------------------------------------

# 5. Removendo Elementos da Lista
# Você pode remover elementos usando os métodos .remove(), .pop(), ou del.

# 5.1. .remove() - Remove a primeira ocorrência de um valor específico.
minha_lista.remove(20)
print(minha_lista)  # Saída: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# 5.2. .pop() - Remove e retorna o elemento na posição especificada (ou o último elemento se nenhum índice for dado).
ultimo_elemento = minha_lista.pop()
print(ultimo_elemento)  # Saída: 9
print(minha_lista)  # Saída: [10, 2, 3, 4, 5, 6, 7, 8]

# 5.3. del - Remove um elemento ou um fatiamento específico da lista.
del minha_lista[0]  # Remove o primeiro elemento
print(minha_lista)  # Saída: [2, 3, 4, 5, 6, 7, 8]

# --------------------------------------------------

# 6. Fatiamento de Listas (Slicing)
# Assim como em strings, você pode usar fatiamento para acessar partes de uma lista.
# Sintaxe: lista[início:fim:passo]

fatia = minha_lista[1:4]  # Pega elementos do índice 1 ao 3
print(fatia)  # Saída: [3, 4, 5]

fatia_com_passo = minha_lista[::2]  # Pega elementos de 2 em 2
print(fatia_com_passo)  # Saída: [2, 4, 6, 8]

# --------------------------------------------------

# 7. Encontrando o Comprimento da Lista
# Use a função len() para obter o número de elementos em uma lista.
tamanho = len(minha_lista)
print(tamanho)  # Saída: 7

# --------------------------------------------------

# 8. Ordenando Listas
# Você pode ordenar os elementos de uma lista em ordem crescente ou decrescente usando o método .sort() ou a função sorted().

# 8.1. .sort() - Ordena a lista no lugar (in-place).
minha_lista.sort()
print(minha_lista)  # Saída: [2, 3, 4, 5, 6, 7, 8]

# 8.2. .sort(reverse=True) - Ordena a lista em ordem decrescente.
minha_lista.sort(reverse=True)
print(minha_lista)  # Saída: [8, 7, 6, 5, 4, 3, 2]

# 8.3. sorted() - Retorna uma nova lista ordenada sem alterar a original.
lista_ordenada = sorted(minha_lista)
print(lista_ordenada)  # Saída: [2, 3, 4, 5, 6, 7, 8]
print(minha_lista)  # Saída: [8, 7, 6, 5, 4, 3, 2]

# --------------------------------------------------

# 9. Compreensão de Listas (List Comprehension)
# A compreensão de listas oferece uma maneira concisa de criar listas. 
# A sintaxe básica é: [expressão for item in iterable if condição].

quadrados = [x**2 for x in range(1, 6)]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

pares = [x for x in minha_lista if x % 2 == 0]
print(pares)  # Saída: [8, 6, 4, 2]

# --------------------------------------------------

# 10. Outras Operações com Listas
# Existem várias outras operações úteis que você pode realizar com listas.

# 10.1. .index() - Retorna o índice da primeira ocorrência de um valor.
indice = minha_lista.index(6)
print(indice)  # Saída: 2

# 10.2. .count() - Retorna o número de vezes que um valor aparece na lista.
contagem = minha_lista.count(4)
print(contagem)  # Saída: 1

# 10.3. .reverse() - Inverte a ordem dos elementos da lista.
minha_lista.reverse()
print(minha_lista)  # Saída: [2, 3, 4, 5, 6, 7, 8]

# --------------------------------------------------

# As listas são uma estrutura de dados extremamente poderosa e flexível em Python.
# Elas são fundamentais para muitos tipos de programas e permitem uma variedade de manipulações eficientes.
