# Sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

# Entrada
# A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, os tipos (strings) dos respectivos ativos.

# Saída
# Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for n in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)


# TODO: Ordenar os ativos em ordem alfabética.
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for i in sorted(ativos, key=lambda x:x[0]):
    print(i)
