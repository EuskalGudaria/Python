from tkinter import Tk, Canvas
import random
TAILLE = 500

flocon=[]
for i in range(100):
  x = random.randint(0,500)
  y = random.randint(0,500)
  r = random.randint(0,5)
  flocon.append((x,y,r))


def PROG():
  canvas.create_rectangle(100,200,400,400,width=3,fill='wheat')
  canvas.create_rectangle(150,300,250,350,width=5,fill='blue')
  canvas.create_rectangle(300,300,350,400,width=3,fill='red')
  canvas.create_polygon((200,100,300,100,400,200,100,200),width=5,fill='black')
  canvas.create_oval(200,125,300,175,width=4,fill='yellow')


Mafenetre = Tk()
Mafenetre.geometry(str(TAILLE) + "x" + str(TAILLE))
canvas = Canvas(Mafenetre, width=TAILLE,height=TAILLE,borderwidth=0,highlightthickness=0,bg="lightgray")
canvas.pack()
Mafenetre.after(100,PROG)
Mafenetre.mainloop()
