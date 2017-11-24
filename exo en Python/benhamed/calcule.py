ecrire un script en python qui permet de calculer le total en seconde d'un temp exprimée en h, m et s

saisir les heure, minute, et seconde 
operation h = m 




heure = int (input("donner les heure"))
minute = int( input ("donner les minute"))
seconde = int ( input ("donner les seconde"))
heurecaculer =heure * 3600
minutecalculer = minute * 60
solution = heurecalculer + minutecalculer + seconde
print ("le nombre de seconde ",solution)

input () 