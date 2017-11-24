#equation du seconf degres
import math
a = float (input("donner le premier coef"))
b = float (input("donner le second coef"))
c = float (input("donner le troisieme coef"))
if a == 0:
	if b == 0:
		if c == 0:
			print ("tous nb reel est solution de lequation")
		else:
			print (" aucune solution")
	else: 
		x=-c/b
		print ("la solution est :",x)
else: 
	d=b*b-4*a*c
	if d<0 :
		print ("aucune solution")
	elif d==0 :
		x =-d/(2*a)
		print ("la solutionv doucle est :",x)
	else :
		x1=(-b-math.sqrt(d)) /(2*a)
		x2=(-b+math.sqrt(d)) /(2*a)
		print ("la 1er solution est :",x1)
		print ("la 2 eme solution est :",x2)
	
print (" fin")
input()