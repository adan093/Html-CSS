#ecrire un programme qui permet de saisir une @ip compose de de 4 entier.
#le programme teste la validite des 4 entier et determine la classe d@, le masque et les @debut et fin de la plage ip

a = int (input ("entre le premier octect"))
b = int (input ("entre le second octect"))
c = int (input ("entre le troisieme octect"))
d = int (input ("entre le quatrieme octect"))

if a < 0  or a >255 :
	print ("erreur sur le premier octet")
if b < 0 or b > 255 :
	print ("erreur sur le second octet")
if c < 0 or c > 255 :
	print ("erreur sur le troisieme octet")