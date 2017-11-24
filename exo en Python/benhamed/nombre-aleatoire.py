# ecrire une fonction qui genere un nombre aleatoire compris entre deux limites
#ecrire une procedure qui remplie un tableau de 10 entiers aleatoire
#ecrire une procedure qui tri le tableau dans le sens croissant
#realiser le prog principal
table =[]
import random


def genere (lim1,lim2):
	nb = random.randint(lim1,lim2)
	
	return nb
	
def remplir (lim1,lim2):
	for i in range (0,10):
		nb =genere(lim1,lim2)
		table.append(nb)
	
def trier ():
	for i in range (0,10):
		for j in range (i,10):
			if table [i]>table[j]:
				temp=table[i]
				table[i]=table[j]
				table[j]=temp
			
			
lim1= int (input('donner la limite 1:'))
lim2= int (input('donner la limite 2:'))
remplir(lim1,lim2)
print ('voici le tables')
print(table)
trier()
print('voici le tableau ')
print(table)
input()