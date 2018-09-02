#Função para listagem de Coligações
#Recebe: Lista
#Retorna: Conjunto
def getColigacoes(lista_geral):
	coligacao = []
	for candidato in lista_geral[1:]:
		if(len(candidato[2].split(" - ")) > 1):
			coligacao.append(candidato[2].split(" - ")[1]) 
	coligacoes = set(coligacao)
	return sorted(coligacoes)

#Função para listagem de Partidos
#Recebe: Lista
#Retorna: Conjunto
def getPartidosUnitarios(lista_geral):
	partido = []
	for candidato in lista_geral[1:]:
		if(len(candidato[2].split(" - ")) == 1):
			partido.append(candidato[2].split(" - ")[0])
	partidos = set(partido)
	return sorted(partidos)

#Função para exibição de conteúdo de uma estrutura baseada em indexação.
#Recebe: Lista
def showSomethingListed(list_of_something):
	for something in list_of_something:
		print(something)
	print("")

#Função para contagem de votos dos Partidos.
#Recebe: Conjunto, Conjunto, Lista
#Retorna: Dicionário
def countVotes(entidades_1, entidades_2, lista_geral):
	entidades_geral = list(entidades_1) + list(entidades_2)
	countedVotes = dict.fromkeys(entidades_geral, 0)
	for candidato in lista_geral[1:]:
		if(len(candidato[2].split(" - ")) == 1):
			partido = candidato[2].split(" - ")[0]
			if(int(countedVotes[partido]) > 0):
				countedVotes[partido] += int(candidato[3])
			else:
				countedVotes[partido] = int(candidato[3])
		else:
			coligacao = candidato[2].split(" - ")[1]
			if(int(countedVotes[coligacao]) > 0):
				countedVotes[coligacao] += int(candidato[3])
			else:
				countedVotes[coligacao] = int(candidato[3])
	return countedVotes

#Função para exibição de estrutura baseada em tuplas.
#Recebe: Dicionário
def showSomethingTupled(dict_of_something):
	for something in dict_of_something:
		print(something + " -----> " + str(dict_of_something[something]))
	print("")

#Função para geração do Quoeficiente Eleitoral.
#Recebe: Dicionário, Inteiro
#Retorna: Inteiro
def generateQE(dict_votos, cadeiras):
	QE_entidades = int(sum(list(dict_votos.values()))/cadeiras)
	return QE_entidades

def generateQP(dict_votos, QE):
	pass