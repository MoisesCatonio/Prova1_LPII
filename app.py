import csv

import my_lib as ml

lista_geral = list(csv.reader(open('eleicao.csv', encoding="UTF-8"),delimiter=";"))

coligacoes = ml.getColigacoes(lista_geral)

partidos = ml.getPartidos(lista_geral)

#ml.showSomethingListed(coligacoes)

#ml.showSomethingListed(partidos)

votos_partidos = ml.countVotes_P(partidos,lista_geral)

votos_coligacoes = ml.countVotes_C(coligacoes,lista_geral)

ml.showSomethingTupled(votos_coligacoes)