import csv

import my_lib as ml

#Caso esteja em dúvida de alguma coisa, verifique com as exibições de listas e tuplas implementadas,
#ml.showSomethingTupled(Dict), ml.showSomethingListed(List) ;)

lista_geral = list(csv.reader(open('eleicao.csv', encoding="UTF-8"),delimiter=";"))

coligacoes = ml.getColigacoes(lista_geral)

partidos = ml.getPartidosUnitarios(lista_geral)

votos_geral = ml.countVotes(partidos,coligacoes, lista_geral)

#QE usado do arquivo dado pelo professor, mas função de geração de QE implementada (ml.generateQE)!!!
QP_geral = ml.generateQP(votos_geral, 12684)