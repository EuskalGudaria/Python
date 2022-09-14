liste_horizon = [1,15,18,55,60]
liste_vertical = [5,15,20,77]

for i in liste_horizon:
  print("{0:3}".format(i),end = " ")

print()

for i in liste_vertical:
  nombre_vertical = i
  print(nombre_vertical,end=" ")
  for j in liste_horizon:
    nombre_horizontal = j
    if nombre_vertical > nombre_horizontal :
      print(">",end="   ")
    elif nombre_vertical == nombre_horizontal :
      print("=",end="   ")
    else : 
      print("<", end="   ")
  print(" ")