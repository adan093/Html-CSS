#enonce matrice d'affichage
#ecrire une procedure qui permet de genere une matrice carre
#avec un nombre de ligne recu entre (0 affecte a chaque element)
#ecrire une procedure qui affiche la matrice
#ecrire une procedure qui affiche x avec des 1.
#ecrire une procedure qui affiche 0 avec des 1.
#ecrire une procedure qui affiche L avec des 1.
#ecrire un programme principal qui demande la taille de la matrice
# et qui appelle les procedure

#################################################################
matrice = []
############################################################

def generer(taille):
	for i in range(0,taille):
		ligne = []
		for j in range(0, taille):
			ligne.append(0)
		matrice.append (ligne)
	
########################################################

def afficher(taille):
	for i in range (0, taille):
		print (matrice[i])
		
####################################
def afficherL (taille):
	for i in range (0, taille):
		matrice [i][0]=1
	for j in range (0, taille):
		matrice [taille-1][j]=1
#########################################
def afficher0 (taille):
	afficherL (taille)
	for j in range (0, taille):
		matrice [0][j]=1
	for i in range (0, taille):
		matrice [i][taille-1]=1
	
############################################
taille = int(input("donnez la taille de la matrice:"))
generer(taille)
afficherL(taille)
afficher(taille) 
generer(taille)
print('\n')
afficher0(taille)
afficher(taille)
input()