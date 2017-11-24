#ecrire un programme qui permet de genere un nombre
#aleatoire compris entre deux limites
#entieres saisies par l'utilisateur
#le programmeaffiche si le nombre est pair ou impair

import random

lim1 = int (input('donner le 1er limite'))
lim2 = int (input ('donner la 2eme limite'))

nb = random.randint (lim1,lim2)

if nb%2==0:
	print('le nb est pair',nb)
else :
	print('le nb est impair',nb)
input ()