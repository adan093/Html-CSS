nbh= float (input("donner le nb d'heure"))
tarif = float (input("donner le tarif"))
taux  = float (input("donner le taux"))
pht = nbh * tarif
ttc = (pht * taux)/100+ pht
tva = ttc - pht
print ("le ttc est de ",ttc)
print ("la tva est de ",tva)

