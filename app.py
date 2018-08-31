import csv

import my_lib as ml

lista_geral = list(csv.reader(open('eleicao.csv', encoding="UTF-8"),delimiter=";"))

coligacoes = ml.getColigacoes(lista_geral)

partidos = ml.getPartidos(lista_geral)

print("Coligações: ")
for ex in sorted(coligacoes):
	print(ex)

print("Partidos: ")
print(" ")

for ex2 in sorted(partidos):
	print(ex2)

#print(partidos)
#print(coligacoes)