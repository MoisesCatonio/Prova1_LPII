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

def showSomethingListed(list_of_something):
	for something in list_of_something:
		print(something)
	print("")

def countVotes_P(entidades, lista_geral):
	countedVotes = dict.fromkeys(entidades, 0)
	for candidato in lista_geral[1:]:
		celula = candidato
		partido = celula[2].split(" - ")[0]
		if(int(countedVotes[partido]) > 0):
			countedVotes[partido] += int(celula[3])
		else:
			countedVotes[partido] = int(celula[3])
	return countedVotes

def countVotes_C(entidades, lista_geral):
	countedVotes = dict.fromkeys(entidades, 0)
	for candidato in lista_geral[1:]:
		celula = candidato
		if(len(celula[2].split(" - ")) > 1):
			coligacao = celula[2].split(" - ")[1]
			if(int(countedVotes[coligacao]) > 0):
				countedVotes[coligacao] += int(celula[3])
			else:
				countedVotes[coligacao] = int(celula[3])
	return countedVotes

def showSomethingTupled(dict_of_something):
	for something in dict_of_something:
		print(something + " -----> " + str(dict_of_something[something]))
	print("")
