#ecrire un prog qui permet de demande un nb de ligne 
#et un nb de colonnes et realise
#la saisie de la matrice et son affiche 

######### declaration la matrice #############

matrice=[]

############### saisie du ligne et colonnes ##########

nblignes=int(input('donner le nb de ligne'))
nbcolonnes=int(input('donner le nb de colonnes'))

############# saisie de la matrice###############
print('---------------saisir la lignes-------')
for i in range (0,nblignes):
	print('saisir de la ligne:', i+1)
	ligne=[]
	for j in range (0,nbcolonnes):
		nb = int(input('donner le nb'))
		ligne.append(nb)
	matrice.append(ligne)
	
################### affiche la matrice ################
print(matrice)

somme=0
for i in range (0,nblignes):
	for j in range (0,nbcolonnes):
		somme=somme+matrice[i][j]
print(' la somme de tout les nb de la matrice est de :',somme)
input()
	