# Tuplas em Python

# --------------------------------------------------

# 1. O que são Tuplas?
# Tuplas são estruturas de dados imutáveis em Python que permitem armazenar uma sequência de elementos.
# Uma vez criadas, as tuplas não podem ser modificadas.

# --------------------------------------------------

# 2. Criando Tuplas
# Tuplas são criadas usando parênteses `()` e os elementos são separados por vírgulas.

# Exemplo de criação de uma tupla
tupla = (1, 2, 3, "Python", 3.14)
print(tupla)  # Saída: (1, 2, 3, 'Python', 3.14)

# --------------------------------------------------

# 3. Acessando Elementos de uma Tupla
# Os elementos de uma tupla podem ser acessados usando índices, começando do 0.

# Exemplo de acesso a elementos
print(tupla[0])  # Saída: 1
print(tupla[3])  # Saída: Python

# --------------------------------------------------

# 4. Tuplas e Desempacotamento
# Tuplas podem ser usadas para desempacotar valores em variáveis individuais.

# Exemplo de desempacotamento
a, b, c, d, e = tupla
print(a)  # Saída: 1
print(d)  # Saída: Python

# --------------------------------------------------

# 5. Operações com Tuplas
# Tuplas suportam várias operações, como concatenação e repetição.

# Exemplo de concatenação e repetição
tupla1 = (1, 2, 3)
tupla2 = ("a", "b", "c")

tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Saída: (1, 2, 3, 'a', 'b', 'c')

tupla_repetida = tupla1 * 3
print(tupla_repetida)  # Saída: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# --------------------------------------------------

# 6. Imutabilidade das Tuplas
# Tuplas são imutáveis, o que significa que seus elementos não podem ser alterados após a criação. 
# Tentativas de modificar uma tupla gerarão um erro.

# Exemplo de tentativa de alteração (vai gerar um erro)
# tupla[0] = 10  # Isso gerará um erro: TypeError: 'tuple' object does not support item assignment

# --------------------------------------------------

# 7. Tuplas com um Único Elemento
# Para criar uma tupla com um único elemento, é necessário adicionar uma vírgula após o elemento.

# Exemplo de tupla com um único elemento
tupla_unica = (5,)
print(tupla_unica)  # Saída: (5,)

# --------------------------------------------------

# 8. Tuplas Aninhadas
# Tuplas podem conter outras tuplas como elementos.

# Exemplo de tuplas aninhadas
tupla_aninhada = ((1, 2), (3, 4), (5, 6))
print(tupla_aninhada)  # Saída: ((1, 2), (3, 4), (5, 6))

# --------------------------------------------------

# 9. Métodos de Tupla
# Tuplas possuem alguns métodos úteis, como `count()` e `index()`.

# Exemplo do método `count()`
contagem = tupla.count(1)
print(contagem)  # Saída: 1

# Exemplo do método `index()`
indice = tupla.index("Python")
print(indice)  # Saída: 3

# --------------------------------------------------

# 10. Usos Comuns de Tuplas
# Tuplas são frequentemente usadas para armazenar dados que não devem ser alterados e como chaves em dicionários devido à sua imutabilidade.

# Exemplo de uso como chave em um dicionário
dicionario = {("chave1",): "valor1", ("chave2",): "valor2"}
print(dicionario)  # Saída: {('chave1',): 'valor1', ('chave2',): 'valor2'}

# --------------------------------------------------

# Tuplas são uma estrutura de dados essencial em Python, oferecendo uma maneira eficiente e segura para armazenar e manipular dados imutáveis.
