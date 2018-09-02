import csv

import my_lib as ml

lista_geral = list(csv.reader(open('eleicao.csv', encoding="UTF-8"),delimiter=";"))

coligacoes = ml.getColigacoes(lista_geral)

partidos = ml.getPartidosUnitarios(lista_geral)

votos_geral = ml.countVotes(partidos,coligacoes, lista_geral)

ml.showSomethingTupled(votos_geral)

QE = ml.generateQE(votos_geral, 29)