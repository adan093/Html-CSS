# ecrire une procedure qui permet de recevoir un nombre entier 
#et affiche tous ses diviseurs
#ecrire un programme principal qui utiliser cette procedure

##################################################
##############la procedure#######################

def affichediviseurs ( nb ):
	d=1
	while d<=nb:
		if  nb % d ==0:
			print ('diviseur:',d)
		d=d+1

#############################################
##################programme principal########

x=int(input('donnez un nombre entier:'))
affichediviseurs (x)
input ()

	