# ecrire une fonction qui permet de calculer la puissance d'un nombre par 
#un exposant, la fonction recoit le nombre et l"exposant.
# ecrire un programme qui appelle la fonction

##################################################
##############la procedure#######################

def puissance ( nb, exp):
	i=1
	p=1
	while i<=exp:
		p=nb*p
		i=i+1
	return p
	

#############################################
##################programme principal########

x=int(input('donner la nombre'))
y=int(input('donner la puissance'))
resultat= puissance (x, y)
print('le resultat est de ',resultat)
input ()

	