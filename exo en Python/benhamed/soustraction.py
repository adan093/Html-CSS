# ecrire une fonction qui fait la soustration de deux nombre

def soustraction (nb1, nb2) :
	res = nb1 -nb2
	return res

# programme principal

a = int (input('donner un nombre 1 :'))
b = int (input('donner un nombre 2 :'))

c = soustraction (a, b)
print('le resultat est de :',c)

input ()