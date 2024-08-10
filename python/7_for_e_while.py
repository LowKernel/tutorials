# Laços de Repetição em Python

# --------------------------------------------------

# 1. O que são Laços de Repetição?
# Laços de repetição permitem que você execute um bloco de código várias vezes.
# Existem dois tipos principais de laços de repetição em Python: `for` e `while`.

# --------------------------------------------------

# 2. O Laço `for`
# O laço `for` é usado para iterar sobre uma sequência (como uma lista, tupla, string, ou range).

# Exemplo básico com uma lista:
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)  # Saída: maçã, banana, cereja

# --------------------------------------------------

# 3. A Função `range()`
# A função `range()` gera uma sequência de números e é frequentemente usada com `for`.

# Exemplo 1: Iterando de 0 a 4
for i in range(5):
    print(i)  # Saída: 0, 1, 2, 3, 4

# Exemplo 2: Iterando de 2 a 6
for i in range(2, 7):
    print(i)  # Saída: 2, 3, 4, 5, 6

# Exemplo 3: Iterando de 0 a 10 com um passo de 2
for i in range(0, 11, 2):
    print(i)  # Saída: 0, 2, 4, 6, 8, 10

# --------------------------------------------------

# 4. O Laço `while`
# O laço `while` executa um bloco de código enquanto uma condição for verdadeira.

# Exemplo básico:
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Saída: 0, 1, 2, 3, 4

# --------------------------------------------------

# 5. Interrompendo Laços: `break` e `continue`
# O `break` e o `continue` são usados para controlar o fluxo dos laços.

# 5.1. O `break` é usado para sair do laço imediatamente.
for i in range(10):
    if i == 5:
        break  # Sai do laço quando `i` é 5
    print(i)  # Saída: 0, 1, 2, 3, 4

# 5.2. O `continue` é usado para pular a iteração atual e continuar com a próxima.
for i in range(10):
    if i % 2 == 0:
        continue  # Pula a iteração se `i` for par
    print(i)  # Saída: 1, 3, 5, 7, 9

# --------------------------------------------------

# 6. O Comando `else` com Laços
# Em Python, o laço `for` ou `while` pode ter um bloco `else`, que será executado quando o laço terminar normalmente (sem que um `break` seja chamado).

# Exemplo:
for i in range(3):
    print(i)
else:
    print("Laço for terminou normalmente")  # Este `else` será executado

# Exemplo com `break`:
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Este else não será executado, pois o laço foi interrompido por um break")

# --------------------------------------------------

# 7. Laços Aninhados
# Você pode usar laços dentro de outros laços, conhecidos como laços aninhados.

# Exemplo de laços aninhados:
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
        # Saída:
        # i = 0, j = 0
        # i = 0, j = 1
        # i = 1, j = 0
        # i = 1, j = 1
        # i = 2, j = 0
        # i = 2, j = 1

# --------------------------------------------------

# 8. Iterando sobre Dicionários com `for`
# Você pode usar o laço `for` para iterar sobre as chaves, valores ou ambos em um dicionário.

# Exemplo de iteração sobre as chaves:
meu_dicionario = {"nome": "Pedro", "idade": 17, "cidade": "São Paulo"}
for chave in meu_dicionario:
    print(chave)  # Saída: nome, idade, cidade

# Exemplo de iteração sobre os valores:
for valor in meu_dicionario.values():
    print(valor)  # Saída: Pedro, 17, São Paulo

# Exemplo de iteração sobre os pares chave-valor:
for chave, valor in meu_dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")
    # Saída:
    # Chave: nome, Valor: Pedro
    # Chave: idade, Valor: 17
    # Chave: cidade, Valor: São Paulo

# --------------------------------------------------

# 9. Compreensão de Listas (List Comprehension)
# É uma forma concisa de criar listas usando laços `for`.

# Exemplo:
quadrados = [x**2 for x in range(5)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16]

# --------------------------------------------------

# Laços de repetição são essenciais para a programação, permitindo que você execute operações repetitivas de maneira eficiente e elegante.