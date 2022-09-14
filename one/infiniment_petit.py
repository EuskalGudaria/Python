nbr_iteration = 50
chiffre_a_diviser = 1
print("XX" + ("0123456789" *5))
for i in range(nbr_iteration) :
  chiffre_a_diviser = chiffre_a_diviser / 2
  print("{0:51.50f}".format(chiffre_a_diviser))
  