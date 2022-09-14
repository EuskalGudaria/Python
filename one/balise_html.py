page_web ="<html> <head> <title> Mon Titre </title> </head> <body> Texte sur la page </body> </html>"

for i in range (len(page_web)) :
  if page_web[i] == "<" :
    close = page_web.find(">",i)
    print (page_web[(i+1) : (close)])