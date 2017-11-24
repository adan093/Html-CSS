a = float (input("donner le nombre a"))
b = float (input("donner le nombre b"))
if a == 0:
	if b == 0:
		print ("tous nb reel est solution")
	else:
		print(" aucune solution ")
else :
	x = -b/a
	print ("la solution est de : ", x)
print (" fin")
input() 