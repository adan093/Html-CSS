#ecrire un programme qui permet d'additionner tous les nombre compris entre deux limite sasie par l'utilisateur. utiliser la boucle for

limite1 = int ( input ("donner la 1er limite"))
limite2 = int ( input ("donner la 2eme limite"))

somme =0
for i in range( limite1, limite2 ):
	somme = i+ somme
print ("somme des nombres =",somme)
input ()