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
    while is_finished() == True:
        x = random.randint(1, len(pixel) - 2)
        print("X=",x)
        y = 0
        if (x % 2 == 0):
            y = random.randint(1, len(pixel) - 2) 
            print("Y=",y)
        else:
            y = random.randint(1, len(pixel) - 2) 
            print("Y=",y)


        cell_1=0
        cell_2=0
        if pixel[y][x-1] == -1:
            cell_1= pixel[y-1][x]
            #print("Cell1-1=",cell_1)
            cell_2= pixel[y+1][x]
            #print("Cell2-1=",cell_2)
        else:
            cell_1= pixel[y][x-1]
            #print("Cell1=",cell_1)
            cell_2= pixel [y][x+1]
            #print("Cell2=",cell_2)
                        
        if cell_1 != cell_2:
            pixel[y][x] = 0
            for i in range(1,maze_size-1,2):
                for j in range(1,maze_size-1,2):
                    if pixel[i][j] == cell_2:
                        pixel[i][j] = cell_1        
    pixel[0][1] = 1 
    pixel[maze_size-1][maze_size-2] = nb


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
    
def dessiner():
    for y in range(maze_size):
        for x in range(maze_size):
            if pixel[x][y] >= 0:
                coul = "white"
            elif pixel[x][y] == -1:
                coul = "black"
            canvas.itemconfig(case[x][y], fill=coul)


def score_boxes(pixel):
    color = 1
    temp = pixel
    distance = 1
    pixel[maze_size - 1][maze_size - 2] = 1
    canvas.itemconfig(case[maze_size - 1][maze_size - 2], fill=rgb((255,255,0)))
    while pixel[1][1] == 0:
        distance += 1
        for i in range (0,maze_size - 2,-1):
            for j in range (0,maze_size - 2,-1):
                if pixel[i][j] == 0 : 
                    if pixel[i][j - 1]  > 0 or pixel[i][j + 1] > 0 or pixel[i - 1][j] >  0 or pixel[i + 1][j] > 0:
                        temp[i][j] = distance
                        color += 1
                        canvas.itemconfig(case[i][j], fill=rgb((color * 1.5,color * 1.5,color * 1.5)))
    pixel = temp
                        


def maze_solver():
    x = 1 
    y = 1
    while x != maze_size - 2 or y != maze_size - 2: 
        up = pixel[y-1][x]
        down = pixel[y+1][x]
        left = pixel[y][x-1]
        right = pixel[y][x+1]
        if up <= down and up <= left and up <= right:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            y = y - 1
        elif down <= up and down <= left and down <= right:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            y = y + 1
        elif left <= up and left <= down and left <= right:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            x = x - 1
        elif right <= up and right <= down and right <= left:
            canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))
            x = x + 1
        canvas.itemconfig(case[x][y], fill=rgb((0,255,0)))


# Lancement du programme
fenetre = Tk()
fenetre.title("Labyrinth")
canvas = Canvas(fenetre, width=cote*maze_size, height=cote*maze_size, highlightthickness=0)
fenetre.minsize(cote*maze_size,cote*maze_size)
fenetre.maxsize(cote*maze_size,cote*maze_size)
canvas.pack()
init()
dessiner()
score_boxes(pixel)
maze_solver()
print(""" 
    ======================
        maze generator
    ======================
    """)
fenetre.mainloop()