liste = [0,1,2,3,4,5]
nombre_a_deplacer=0
nombre_decalage = len(liste)
print(liste)
for i in range(nombre_decalage):
  nombre_a_deplacer = liste[5]
  liste.pop()
  liste.insert(0,nombre_a_deplacer)
  print("décalage numéro : ",i,"la liste est : ",liste)