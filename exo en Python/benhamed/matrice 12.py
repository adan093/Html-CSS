####################  les notices #############################
# enonce : ecrire une procedure qui permet de remplir
#une matrice d'entier avec un nb lignes et un nb colonnes
#ecrire une procedure qui permet d'afficher la matrice
#ecrire une fonction qui permet de calculer la somme de tous les nombres de la matrice
#et retourne le nombre d'apparition de la valeur dans la matrice
# ecrire un prog qui appelle ces procedure et ces fonction

import random
matrice = []

############### remplissage du ligne et colonnes ##########

def remplir (nbligne,nbcolonne):
	for i in range (0,nbligne):
		ligne=[]
		for j in range(0,nbcolonne):
			nb=nb=random.randint(1,100)
			ligne.append(nb)
		matrice.append(ligne)
		
############### procedure afficher matrice $################

def afficher(nbligne, nbcolonne):
	for i in range(0,nbligne):
		for j in range (0,nbcolonne):
			print(matrice[i])
			print ("\n")
			
################ fonction somme #####################

def somme(nbligne,nbcolonne):
	somme=0
	for i in range(0,nbligne):

		
##############program$me principal #####################

a=int(input('donner le nb de ligne'))
b=int(input('donner le nb de colonne'))
remplir (a,b)
print (matrice)
input()