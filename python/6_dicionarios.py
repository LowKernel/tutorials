# Manipulação de Dicionários em Python

# --------------------------------------------------

# Dicionários em Python são coleções não ordenadas de pares chave-valor.
# Eles são mutáveis, o que significa que você pode alterar, adicionar ou remover elementos após a criação.

# 1. Criando um Dicionário
# Um dicionário é criado usando chaves {} e pares chave-valor separados por dois-pontos.
meu_dicionario = {"nome": "Pedro", "idade": 16, "altura": 1.76}
outro_dicionario = {1: "um", 2: "dois", 3: "três"}
dicionario_vazio = {}

# --------------------------------------------------

# 2. Acessando Valores em um Dicionário
# Os valores de um dicionário podem ser acessados usando suas chaves.
print(meu_dicionario["nome"])  # Saída: Pedro
print(outro_dicionario[2])  # Saída: dois

# Se você tentar acessar uma chave que não existe, ocorrerá um erro. Para evitar isso, use o método .get().
print(meu_dicionario.get("idade"))  # Saída: 16
print(meu_dicionario.get("peso", "Chave não encontrada"))  # Saída: Chave não encontrada

# --------------------------------------------------

# 3. Modificando Valores no Dicionário
# Como os dicionários são mutáveis, você pode alterar os valores associados às chaves.
meu_dicionario["idade"] = 17
print(meu_dicionario)  # Saída: {'nome': 'Pedro', 'idade': 17, 'altura': 1.76}

# --------------------------------------------------

# 4. Adicionando e Removendo Pares Chave-Valor
# Você pode adicionar novos pares chave-valor ao dicionário ou remover pares existentes.

# 4.1. Adicionando um novo par chave-valor.
meu_dicionario["peso"] = 67.3
print(meu_dicionario)  # Saída: {'nome': 'Pedro', 'idade': 17, 'altura': 1.76, 'peso': 67.3}

# 4.2. Removendo um par chave-valor usando del.
del meu_dicionario["altura"]
print(meu_dicionario)  # Saída: {'nome': 'Pedro', 'idade': 17, 'peso': 67.3}

# 4.3. Removendo e retornando o valor associado a uma chave com .pop().
idade = meu_dicionario.pop("idade")
print(idade)  # Saída: 17
print(meu_dicionario)  # Saída: {'nome': 'Pedro', 'peso': 67.3}

# 4.4. Removendo e retornando o último par chave-valor com .popitem().
ultimo_item = meu_dicionario.popitem()
print(ultimo_item)  # Saída: ('peso', 67.3)
print(meu_dicionario)  # Saída: {'nome': 'Pedro'}

# --------------------------------------------------

# 5. Verificando se uma Chave Existe no Dicionário
# Use o operador `in` para verificar se uma chave está presente no dicionário.
print("nome" in meu_dicionario)  # Saída: True
print("idade" in meu_dicionario)  # Saída: False

# --------------------------------------------------

# 6. Iterando sobre um Dicionário
# Você pode percorrer as chaves, valores ou ambos em um dicionário.

# 6.1. Iterando sobre as chaves.
for chave in meu_dicionario:
    print(chave)  # Saída: nome

# 6.2. Iterando sobre os valores.
for valor in meu_dicionario.values():
    print(valor)  # Saída: Pedro

# 6.3. Iterando sobre os pares chave-valor.
for chave, valor in meu_dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")  # Saída: Chave: nome, Valor: Pedro

# --------------------------------------------------

# 7. Dicionários Aninhados (Nested Dictionaries)
# Dicionários podem conter outros dicionários como valores, criando estruturas aninhadas.

aluno = {
    "nome": "Ana",
    "idade": 22,
    "notas": {
        "matemática": 85,
        "história": 90
    }
}

print(aluno["notas"]["matemática"])  # Saída: 85

# --------------------------------------------------

# 8. Métodos Úteis de Dicionário
# Existem vários métodos integrados para trabalhar com dicionários.

# 8.1. .keys() - Retorna uma lista de todas as chaves do dicionário.
chaves = meu_dicionario.keys()
print(chaves)  # Saída: dict_keys(['nome'])

# 8.2. .values() - Retorna uma lista de todos os valores do dicionário.
valores = meu_dicionario.values()
print(valores)  # Saída: dict_values(['Pedro'])

# 8.3. .items() - Retorna uma lista de todos os pares chave-valor do dicionário.
itens = meu_dicionario.items()
print(itens)  # Saída: dict_items([('nome', 'Pedro')])

# 8.4. .update() - Atualiza o dicionário com pares chave-valor de outro dicionário.
meu_dicionario.update({"idade": 17, "altura": 1.76})
print(meu_dicionario)  # Saída: {'nome': 'Pedro', 'idade': 17, 'altura': 1.76}

# --------------------------------------------------

# 9. Copiando um Dicionário
# Para copiar um dicionário, use o método .copy() ou a função dict().

copia_dicionario = meu_dicionario.copy()
print(copia_dicionario)  # Saída: {'nome': 'Pedro', 'idade': 17, 'altura': 1.76}

# --------------------------------------------------

# Dicionários são uma estrutura de dados extremamente versátil em Python, usados para mapear chaves a valores.
# Eles permitem acesso rápido e eficiente aos dados e são fundamentais em muitos tipos de aplicações.
