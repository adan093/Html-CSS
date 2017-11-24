#declarer un tableau et demander les elements 
# à l'utilisateur et afficher le tableau

######### declaration d'un tableau #############

tableau=[]

############### saisie du nombre d'elements  ##########

nb= int (input('entre le nombre elements'))


############ stockage des elements #############

for i in range (0, nb):
	e=int (input('donner un element'))
	tableau.append(e)
	

############# afficher les elements ###############


for element in tableau:
	print ('valeur:',element)
	
################### fin ################
input()
	