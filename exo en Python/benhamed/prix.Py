nbh= float (input("donner le nb d'heure:"))
tarif = float (input("donner le tarif:"))
taux  = float (input("donner le taux:"))
pht = nbh * tarif
ttc = (pht * taux)/100+ pht
tva = ttc - pht
print ("le ttc est de :"ttc)
print ("la tva est de :"tva)

a = int(input("donner le nombre a"))
b = int (input("donner le nombre b"))
if a > b :
	print(a,"superieur a ",b) 
elif a==b :
	print (a,"est egal à ",b)
else : 
	print (a,"inferieur à ";b)
print("fin du programme")
input ()














