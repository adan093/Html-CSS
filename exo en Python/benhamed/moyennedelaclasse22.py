# enonce de l'exo :
#dans une matrice, on stock les moyennes de 5 classes de bts sio sur trois trimestres
#ecrire une procedure qui stock les données
#ecrire une procedure qui affiche les données
# ecrire une fonction qui detemine la classe qui a eu la plus grande moyenne
# ecrire une fonction qui affiche les moyenne annuelles des cinq classes

#######################################################

matrice = []

def stock():
	for i in range (0,5):
		ligne= []
		for j in range (0,3):
			moyenne = float(input('donner la moyenne'))
			ligne.append(moyenne)
		matrice.append(ligne)
		
##########################

def afficher ():
	for i in range (0,5):
		print(matrice[i])
		
##############################

def maxclasse ():
	max=0
	num=0
	for i in range (0,5):
		for j in range (0,3):
			if max< matrice [i][j]:
				max= matrice [i][j]
				num= i+1
	print('la moyenne max est de :',max)
	return num
	
	################################
	
stock ()
afficher ()
nb=maxclasse()
print('le numero de la classe est de :',nb)
input ()