# Ecrire une fonction qui recoit en entree deux limite entieres 
# et qui genere un nombre aleatoire entre les deux limites. 
# La fonction verifie si la premiere limite est inferieure a la deuxieme. Sinon 
# elle les permute
# Ecrire une procedure qui recoit deux limites entieres et un nombre nb 
# elle genere nb nombres aleatoires et calcule leur moyenne et l'affiche 
# ecrire le programme principal qui appelle la procedure 

#########la fonction generation #############
import random
def generernb (lim1, lim2):
	if lim1>lim2:
		x=lim1
		lim1=lim2
		lim2=x
	nb=random.randint(lim1, lim2)
	return nb 

######## la procedure calculMoyenne ##########

def calculMoyenne (lim1, lim2, nb):
	somme=0
	i=1
	while i<=nb:
		aleatoire=generernb (lim1, lim2)
		print('nb aleatoire', aleatoire)
		somme=aleatoire + somme
		i=i+1
	moyenne = somme / nb 	
	print ('la moyenne des nb aleatoires est de',moyenne)
#######le programme principal ###############

lim1=int(input('donner la limite1:'))
lim2=int(input('donner la limite2:'))
nb=int(input('donner le nb aleatoire'))
calculMoyenne (lim1, lim2, nb)
input()	