from tkinter import *
import random

maze_size = 35  # taille du labyrinth
cote = 25  # coté d'une cellule

# Créer les matrices
case = [[0 for lig in range(maze_size)] for col in range(maze_size)]
pixel = [[ 0  for lig in range(maze_size)] for col in range(maze_size)]

# Données initiales
def init():
    for y in range(maze_size):
        for x in range(maze_size):
            case[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), fill="white")
    #placer les pixels et créer le labyrinthe
    init_pixel()
    create_maze()

def init_pixel(): #placer les pixels
    global nb
    nb = 0 
    for i in range(maze_size):
        pixel[0][i] = -1
        for j in range(1,maze_size):
            if j % 2 == 0:
                pixel[j][i] = -1
            elif i % 2 == 1:
                pixel[j][i] = 0
            else:
                pixel[j][i] = -1

    for x in range(maze_size):
        for y in range(maze_size):
            if pixel[x][y] == 0:
                nb += 1
                pixel[x][y]= nb
    #print(pixel)

def create_maze(): #Kruskal's algorithm
    pixel[0][1] = 0 
    while is_finished() == True:
        x = random.randint(0, len(pixel)-2)
        y = random.randint(0, len(pixel)-2)
        if pixel[x][y] == -1:
            check(x,y)
            draw()
    pixel[maze_size-1][maze_size-2] = nb


def check(x,y):
    div = x % 2
    if div == 0:
        if pixel[x-1][y] >= 0 and pixel[x+1][y]>= 0 and pixel[x-1][y] != pixel[x+1][y]:
            if pixel[x+1][y] > pixel[x-1][y]:
                pixel[x][y] = pixel[x-1][y]
                pixel[x+1][y] = pixel[x-1][y]
            else:
                pixel[x][y] = pixel[x+1][y]
                pixel[x-1][y] = pixel[x+1][y]
    else:
        if pixel[x][y-1] >= 0 and pixel[x][y+1] >= 0 and pixel[x][y-1] != pixel[x][y+1]:
            if pixel[x][y-1] > pixel[x][y+1]:
                pixel[x][y] = pixel[x][y+1]
                pixel[x][y-1] = pixel[x][y+1]
            else:
                pixel[x][y] = pixel[x][y-1]
                pixel[x][y+1] = pixel[x][y-1]







def is_finished():
    for ligne in pixel:
        for colonne in ligne:
            #print("Colonne",colonne) 
            if colonne >= 1:
                return True
    return False

# Dessiner tous les pixels
def rgb(rgb):
    return "#%02x%02x%02x" % rgb
    
def draw():
    fenetre.update()
    for y in range(maze_size):
        for x in range(maze_size):
            if pixel[x][y] >= 0:
                coul = "white"
            elif pixel[x][y] == -1:
                coul = "black"
            canvas.itemconfig(case[x][y], fill=coul)
                        


# Lancement du programme
fenetre = Tk()
fenetre.title("Labyrinth")
canvas = Canvas(fenetre, width=cote*maze_size, height=cote*maze_size, highlightthickness=0)
fenetre.minsize(cote*maze_size,cote*maze_size)
fenetre.maxsize(cote*maze_size,cote*maze_size)
canvas.pack()
init()
draw()
print(""" 
    ======================
        maze generator
    ======================
    """)
fenetre.mainloop()