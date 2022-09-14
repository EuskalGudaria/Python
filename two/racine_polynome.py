import math

print("entrer trois coefficient : a , b , c ")
coefs = input()
coef = coefs.split(" ")
a = float(coef[0])
b = float(coef[1])
c = float(coef[2])

delta = (b**2)-(4*a*c)
print(delta)

if delta > 0 :
  print("solution  1 : ",(-b-(math.sqrt(delta)))/(2*a))
  print("solution  2 : ",(-b+(math.sqrt(delta)))/(2*a))
elif delta == 0 :
  print("solution unique : ", (-b)/(2*a))
else : 
  print("pas de solution le sang")  
