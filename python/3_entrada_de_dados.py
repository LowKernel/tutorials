# Input
# Com input podemos fazer com que seja possível receber dados do usuário pelo terminal. Isso abre muitas portas!
# Mas antes, vamos aprender a converter tipos de dados.
# --------------------------------------------------
# Conversão de tipos de dados
strVariavel = "324"  # Perceba que esta string tem apenas números, com isso podemos convertê-la para tipo inteiro ou float.

# int(): Converte para inteiro se possível.
# float(): Converte para float se possível.
# str(): Converte para string.
# bool(): Retorna True ou False.

# Mais sobre bool() (Importante):
# Quando você tenta converter uma string com bool(), retornará False se ela estiver vazia; caso contrário, retorna True.
# Quando você tenta converter um valor numérico com bool(), retornará False apenas se o valor for zero ou None; caso contrário, retorna True.

intVariavel = int(strVariavel)
print(type(intVariavel))  # <class 'int'>
floatVariavel = float(strVariavel)
print(type(floatVariavel))  # <class 'float'>

# Agora, vamos interagir com o usuário utilizando input.
nome = input("Qual seu nome?: ")
print(f"Olá, {nome}!")

numero = input("Digite um número: ")
print(f"Você digitou: {numero}")
numero2 = input("Digite outro número: ")
print(f"Você digitou: {numero2}")

# Aqui ocorre uma concatenação de strings, não uma soma.
soma = numero + numero2
print(f"A soma desses dois números resulta em: {soma}")

# Para somar corretamente, convertemos as entradas para inteiros.
numero3 = int(input("Digite um número: "))
numero4 = int(input("Digite outro número: "))
soma2 = numero3 + numero4
print(f"A soma desses dois números resulta em: {soma2}")

# Exemplo de uso de input com condição.
idade = int(input("Qual sua idade? "))

if idade < 0:
    print("Digite uma idade válida.")
elif idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
