# Funções em Python

# --------------------------------------------------

# 1. O que são Funções?
# Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
# Elas ajudam a organizar o código, evitando repetição e facilitando a manutenção.

# --------------------------------------------------

# 2. Definindo uma Função
# As funções são definidas usando a palavra-chave `def`, seguida pelo nome da função e parênteses.
# O corpo da função é indentado e contém o código a ser executado.

def saudacao():
    print("Olá, bem-vindo ao Python!")

# Chamando a função
saudacao()  # Saída: Olá, bem-vindo ao Python!

# --------------------------------------------------

# 3. Funções com Parâmetros
# Funções podem receber informações na forma de parâmetros. Esses parâmetros são listados entre parênteses na definição da função.

def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Bem-vindo ao Python!")

# Chamando a função com um argumento
saudacao_personalizada("Ana")  # Saída: Olá, Ana! Bem-vindo ao Python!

# --------------------------------------------------

# 4. Funções com Retorno de Valores
# Funções podem retornar valores usando a palavra-chave `return`. O valor retornado pode ser armazenado em uma variável.

def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado
resultado = soma(5, 3)
print(resultado)  # Saída: 8

# --------------------------------------------------

# 5. Funções com Parâmetros Padrão
# Parâmetros podem ter valores padrão, que são usados se nenhum argumento correspondente for fornecido.

def saudacao_personalizada(nome="visitante"):
    print(f"Olá, {nome}! Bem-vindo ao Python!")

# Chamando a função sem argumento
saudacao_personalizada()  # Saída: Olá, visitante! Bem-vindo ao Python!

# Chamando a função com um argumento
saudacao_personalizada("João")  # Saída: Olá, João! Bem-vindo ao Python!

# --------------------------------------------------

# 6. Funções com Número Variável de Argumentos
# Você pode definir funções que aceitam um número variável de argumentos usando `*args` e `**kwargs`.

# 6.1. `*args` permite passar um número variável de argumentos posicionais.
def lista_args(*args):
    for arg in args:
        print(arg)

# Chamando a função com diferentes números de argumentos
lista_args(1, 2, 3, 4)  # Saída: 1, 2, 3, 4

# 6.2. `**kwargs` permite passar um número variável de argumentos nomeados.
def lista_kwargs(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função com argumentos nomeados
lista_kwargs(nome="Pedro", idade=17, cidade="São Paulo")
# Saída:
# nome: Pedro
# idade: 17
# cidade: São Paulo

# --------------------------------------------------

# 7. Funções Lambda
# Funções lambda são funções anônimas e pequenas definidas com a palavra-chave `lambda`. Elas são úteis para operações simples e de uma linha.

# Exemplo de função lambda que soma dois números
soma_lambda = lambda x, y: x + y
print(soma_lambda(5, 3))  # Saída: 8

# --------------------------------------------------

# 8. Escopo de Variáveis
# Variáveis definidas dentro de uma função são locais a essa função e não podem ser acessadas fora dela.
# Variáveis definidas fora de funções são globais e podem ser acessadas em qualquer lugar do código.

variavel_global = "Eu sou global"

def funcao():
    variavel_local = "Eu sou local"
    print(variavel_global)  # Saída: Eu sou global
    print(variavel_local)   # Saída: Eu sou local

funcao()
# print(variavel_local)  # Isso gerará um erro porque variavel_local não está acessível fora da função

# --------------------------------------------------

# 9. Documentação de Funções
# Você pode adicionar uma string de documentação (docstring) logo após a definição da função para descrever o que ela faz.

def multiplicacao(a, b):
    """
    Retorna o produto de a e b.
    """
    return a * b

print(multiplicacao.__doc__)  # Saída: Retorna o produto de a e b.

# --------------------------------------------------

# Funções são uma parte essencial da programação em Python, facilitando a organização, reutilização e manutenção do código.
