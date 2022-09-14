a=0
for i in range (1,101):
  premier = True
  for k in range (2,i):
    if i%k == 0 :
      premier = False
  if premier : 
    print(i,end=" ")