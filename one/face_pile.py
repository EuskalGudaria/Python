import random

print("nombre de tirage face ou pile : ")
nbr_tirages = int(input())
pile = 0
face = 0

for i in range(nbr_tirages) :
  pileface = random.randint(0,1)
  if pileface == 1 :
    face += 1
  else :
    pile += 1
  
pourcentage_face = round(face/nbr_tirages*100,5)
pourcentage_pile = round(pile/nbr_tirages *100,5)

print("pourcentage de face : ",pourcentage_face,"%")
print("pourcentage de pile : ", pourcentage_pile,"%")