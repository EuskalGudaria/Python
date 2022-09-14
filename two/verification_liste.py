liste = [1,5,11,19,8,50,77,8]
nombre_courant = liste[0]

for i in liste:
  if i >= nombre_courant:
    nombre_courant=i
  else:
    print("les nombres : ",nombre_courant," et ", i,"ne sont pas trié")