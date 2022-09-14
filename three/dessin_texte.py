liste_31 = ["."]*31
liste = [liste_31]*31
print(len(liste_31))

def Affichage():
  for i in range(len(liste_31)) :
    for j in range(len(liste_31)) :
      print(liste[i][j]+liste[i][j],end=" ")
  print()    

def SetPixel(x,y,carac):
  if  x<0 : return
  if  y<0 : return
  if  x>=31 : return
  if  y>=31 : return
  liste[x][y] = carac

def LigneHoriz(x1,y,x2,carac):
  nombre = x2-x1
  for i in range (nombre + 1):
    SetPixel(x1+i,y,carac)

def LigneVert(x,y1,y2,carac):
  nombre = y2-y1
  for i in range (nombre + 1):
    SetPixel(x,y1+i,carac)
    
def Disque(x1,y1,r,carac):
  for x in range (x1-r,x1+r+1):
    for y in range(y1-r,y1+r+1):
      if((x-x1)**2 + (y-y1)**2 )<= r**2:
        SetPixel(x,y,carac)

for x in range (0,31,3):
  LigneVert(x,0,30,"#")    

for y in range (0,30,3):
  LigneHoriz(0,y,30,"=")


Disque(0,0,5,"O")
Affichage()
