# Conjuntos em Python

# --------------------------------------------------

# 1. O que são Conjuntos?
# Conjuntos (sets) são coleções de elementos únicos e não ordenados em Python.
# Eles são úteis para operações de matemática e manipulação de dados onde a unicidade dos elementos é importante.

# --------------------------------------------------

# 2. Criando Conjuntos
# Conjuntos são criados usando a função `set()` ou usando chaves `{}`. 
# Lembre-se de que, ao criar um conjunto vazio, você deve usar `set()`, não `{}`.

# Exemplo de criação de um conjunto
conjunto1 = {1, 2, 3, 4, 5}
print(conjunto1)  # Saída: {1, 2, 3, 4, 5}

# Exemplo de criação de um conjunto vazio
conjunto_vazio = set()
print(conjunto_vazio)  # Saída: set()

# --------------------------------------------------

# 3. Adicionando e Removendo Elementos
# Use o método `add()` para adicionar elementos e o método `remove()` para remover elementos de um conjunto.

# Exemplo de adicionar e remover elementos
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Saída: {1, 2, 3, 4}

conjunto.remove(2)
print(conjunto)  # Saída: {1, 3, 4}

# --------------------------------------------------

# 4. Conjuntos e Elementos Únicos
# Conjuntos automaticamente removem elementos duplicados e não garantem a ordem dos elementos.

# Exemplo com elementos duplicados
conjunto_com_duplicados = {1, 2, 2, 3, 4, 4, 5}
print(conjunto_com_duplicados)  # Saída: {1, 2, 3, 4, 5}

# --------------------------------------------------

# 5. Operações Básicas com Conjuntos
# Conjuntos suportam operações como união, interseção e diferença.

# Exemplo de operações básicas
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

uniao = conjunto_a | conjunto_b  # União
print(uniao)  # Saída: {1, 2, 3, 4, 5}

interseccao = conjunto_a & conjunto_b  # Interseção
print(interseccao)  # Saída: {3}

diferenca = conjunto_a - conjunto_b  # Diferença
print(diferenca)  # Saída: {1, 2}

diferenca_simetrica = conjunto_a ^ conjunto_b  # Diferença Simétrica
print(diferenca_simetrica)  # Saída: {1, 2, 4, 5}

# --------------------------------------------------

# 6. Verificação de Pertinência e Subconjuntos
# Você pode verificar se um elemento pertence a um conjunto e se um conjunto é subconjunto ou superconjunto de outro.

# Exemplo de verificação
print(1 in conjunto_a)  # Saída: True
print(6 in conjunto_a)  # Saída: False

print(conjunto_a.issubset({1, 2, 3, 4}))  # Saída: True
print(conjunto_a.issuperset({1, 2}))  # Saída: True

# --------------------------------------------------

# 7. Métodos Adicionais de Conjunto
# Conjuntos também oferecem métodos adicionais como `discard()`, `pop()` e `clear()`.

# Exemplo dos métodos adicionais
conjunto = {1, 2, 3, 4, 5}

conjunto.discard(3)  # Remove o elemento 3, mas não gera erro se o elemento não existir
print(conjunto)  # Saída: {1, 2, 4, 5}

conjunto.pop()  # Remove e retorna um elemento arbitrário
print(conjunto)

conjunto.clear()  # Remove todos os elementos do conjunto
print(conjunto)  # Saída: set()

# --------------------------------------------------

# 8. Conjuntos e Imutabilidade
# Conjuntos são mutáveis, mas há um tipo de conjunto imutável chamado `frozenset`, que não pode ser alterado após sua criação.

# Exemplo de uso do frozenset
frozenset_exemplo = frozenset([1, 2, 3, 4])
print(frozenset_exemplo)  # Saída: frozenset({1, 2, 3, 4})

# --------------------------------------------------

# Conjuntos são uma estrutura de dados útil para armazenar e manipular coleções de itens únicos. Eles são eficientes para operações que envolvem unicidade e matemática de conjuntos.
