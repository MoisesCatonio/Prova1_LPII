
coligacao = []

partido = []

def getColigacoes(lista_geral):
	for candidato in lista_geral[1:]:
		celula = candidato
		if(len(celula[2].split(" - ")) > 1):
			coligacao.append(celula[2].split(" - ")[1]) 
	coligacoes = set(coligacao)
	return sorted(coligacoes)

def getPartidos(lista_geral):
	for candidato in lista_geral[1:]:
		celula = candidato
		if(len(celula[2].split(" - ")) > 0):
			partido.append(celula[2].split(" - ")[0])
	partidos = set(partido)
	return sorted(partidos)
