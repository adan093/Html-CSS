#ecrire un prog qui permet de stocker dans un tableau 10 moyennes des eleves 
#et affiche la moyenne generale de la classe

######### declaration d'un tableau #############

classe=[]

############### saisie du nombre d'elements  ##########

for i in range (0, 10):
	moy= float(input('donner la moyenne:'))
	classe.append(moy)
	
############# afficher la moyenne generale ###############
somme=0
for element in classe:
	somme=element+somme
mg=somme/10
	
################### affiche la moyenne generale ################
print('la moyenne generale est de :'mg)
input()
	