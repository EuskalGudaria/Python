liste = [1,2,3,5,7,2]
pair = []
impair = []
for i in liste:
  if i%2 != 0 :
    impair.append(i)
  else :
    pair.append(i)

print ("liste pair : ",pair,"\nliste impair : ",impair)