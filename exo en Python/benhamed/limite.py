# exo1 : ecrire un prog en python qui affiche les nombres compris entre deux limites saisie par l'utilisateur. utiliser la boucle while.

limite1 = int ( input ("donner la 1er limite"))
limite2 = int ( input ("donner la 2eme limite"))
i=limite1

while i<=limite2:
	print (i)
	i=i+1
print ("fin-du-programme")
input()