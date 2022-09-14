liste_1 = [1,5,9,65,90,100]
liste_2 = [4,6,8,50,60]
liste = []
x = 0
y = 0
while (x < len(liste_1)) and (y < len(liste_2)) :
  if liste_1[x] >= liste_2[y]:
    liste.append(liste_2[y])
    y +=1
  elif liste_2[y] > liste_1[x] :
   liste.append(liste_1[x])
   x +=1

if x < len(liste_1) :
  while x < len(liste_1):
    liste.append(liste_1[x])
    x+=1

if y < len(liste_2) :
  while y < len(liste_2):
    liste.append(liste_2[y])
    y+=1

print("x : ",x, "y : ",y)
print(liste)
  