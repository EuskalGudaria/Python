def minimum_liste(liste):
  minimum = liste[0]
  print(minimum)
  for i in liste:
    if i < minimum :
       minimum = i
  return minimum


Yo= [-8,-9,5,20,0,-9,48]
print(minimum_liste(Yo))
