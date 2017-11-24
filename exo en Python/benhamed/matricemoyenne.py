# Dans une matrice en stocke les chiffres d'affaires des 5 annes
# d'une entreprise manuellement. ce qui fait 60 chiffres
# ecrire une procedure qui stocke les chiffres
#ecrire une procedure qui affiche les moyennes des anne
#ecrire une procedure qui determine le plus grands chiffre d'affaire
# ecrire une procedure qui determine l'anne la plus rentable
# ecrire une procedure qui determine le mois ou le chiffre est le plus faible.

###########################################################
matrice = []

def saisie():
	for i in range (0,5):
		ligne=[]
		for j in range (0,12):
			chiffre=float(input("donnez le chiffre d'affaire"))
			ligne.append(chiffre)
		matrice.append(ligne)
		

############################# afficher matrice #############

def afficher ():
	for i in range (0,5):
	print(matrice[i])
	
######################################

def moyenne ():
	for i in range (0,5):
	somme= 0
	for j in range (0,12):
		somme = somme + matrice[i][j]
	moyenne = somme / 12
	print ('la moyenne est de :', moyenne)
	
########################################

def maxmatrice ():
	max = matrice[0][0]
	for i in range (0,5):
		for j in range (0,12):
			if max < matrice [i][j]:
	print('le chiffre daffaire max est de' :)
	
################################################


	