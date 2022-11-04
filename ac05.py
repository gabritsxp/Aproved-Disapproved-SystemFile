# abre  o arquivo notas.txt
notas_txt = open('notas.txt', 'r', encoding='UTF-8')

todos_alunos = []

for linha in notas_txt:
    alunos = linha.split(';')
    id = alunos[0]
    nome = alunos[1]
    ac1 = alunos[2]
    ac2 = alunos[3]
    ac3 = alunos[4]
    ac4 = alunos[5]
    ac5 = alunos[6]
    prova = alunos[7]
    substitutiva = alunos[8]
    faltas = alunos[9]

    # define as notas das acs
    notas_acs = []
    notas_acs.append(ac1)
    notas_acs.append(ac2)
    notas_acs.append(ac3)
    notas_acs.append(ac4)
    notas_acs.append(ac5)
    for i in range(len(notas_acs)):
        notas_acs[i] = float(notas_acs[i])
    notas_acs.remove(min(notas_acs))
    media_acs = sum(notas_acs) / len(notas_acs)

    # Define as notas das provas
    nota_da_prova = []
    nota_da_prova.append(prova)
    nota_da_prova.append(substitutiva)
    for i in range(len(nota_da_prova)):
        nota_da_prova[i] = float(nota_da_prova[i])
    maior_nota_provas = max(nota_da_prova, key=float)

    # Define media final
    media_final = (media_acs + maior_nota_provas) / 2

    # Define se o aluno reprovou por falta
    reprovou_por_faltas = True
    faltas = int(faltas)
    if (faltas <= 20):
        reprovou_por_faltas = False

    # guarda os valores em todos os alunos:
    todos_alunos.append([id, nome, media_final, reprovou_por_faltas])

    #Ordena os valores em ordem alfabética
todos_alunos.sort(key=lambda x: x[1])

# abre  o arquivo aprovados e reprovados
aprovados = open('aprovados.txt', 'w', encoding='UTF=8')
reprovados = open('reprovados.txt', 'w',encoding='UTF=8')

# verifica se o aluno foi aprovado ou não, e direciona-o para seu arquivo pertencente
for i in range(len(todos_alunos)):
    if todos_alunos[i][2] >= 6 and todos_alunos[i][3] != True:
        aprovados.write(todos_alunos[i][1] + "\n")
    else:
        reprovados.write(todos_alunos[i][1] + "\n")
    














#     notas = []
#     for nota in alunos:
#         if (nota == alunos[2] or
#             nota == alunos[3] or
#             nota == alunos[4] or
#             nota == alunos[5] or
#             nota == alunos[6] or
#             nota == alunos[7] or
#             nota == alunos[8] or
#                 nota == alunos[9]):
#             notas.append(nota)

#     converte o array de notas em float
#     for i in range(len(notas)):
#         notas[i] = float(notas[i])

#     # calcula média
#     media = sum(notas) / len(notas)

#     todos_alunos.append([id, nome, media])

# # ordena os alunos em ordem alfabética
# todos_alunos.sort(key=lambda x: x[1])
# print(todos_alunos)
