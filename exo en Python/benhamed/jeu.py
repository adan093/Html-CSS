#ecrire un programme qui simule le jeu du nombre secret
#le programme genere un nombre aleatoire et demande a l'user de le trouver.
#A chaque essai, le programme affiche un message,plus petit, plus grand ou bravo.
#le nombre d'essais est fixe a 10.

import random

lim1 = int (input('donner le 1er limite'))
lim2 = int (input ('donner la 2eme limite'))

secret = random.randint (lim1,lim2)

i=1
gagne=0

while i<=10 and gagne==0:
	nb=int(input('donner un nombre'))
	if nb==secret:
		print('bravo')
		gagne=1
	elif nb<secret:
		print('ton nombre est le plus petit')
	else :
		print('ton nombre est le plus grand')
	i=i+1
input()