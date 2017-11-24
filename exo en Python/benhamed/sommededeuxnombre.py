#non ecrit une procedure qui affiche la somme de deux nombre 

def somme (nb1, nb2) :
	res = nb1 + nb2
	print ('le resultat est de :' ,res)
	
# programme principal

a = int (input('donner un nombre 1 :'))
b = int (input('donner un nombre 2 :'))

#appel de la procedure

somme (a, b)
input ()