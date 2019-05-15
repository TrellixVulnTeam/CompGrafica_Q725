from tkinter import Tk, Canvas, Frame, Button, Label, BOTH, Radiobutton
from PIL import Image, ImageTk
import math
import numpy as np
from copy import deepcopy
import os
import pathlib
import time

"""
This file is used to draw figures using the Canvas object (and its methods) from Tkinter
library. It also stores the data structures that represent these figures in vectors and matrixes.

Each figure is composed by at least one face, which in turn is composed by at least
two vertices, and these vertices are coordinates in the (x,y) or (x,y,z) systems (for 2D ands 3D,
respectively). The origin (0,0) is located at the top left corner of the screen.
The data structures are as following:

==> Figure: contains the figure's faces.
    E.g.: Line = (f1) ==> l = [f1]

==> Faces: contains the face's vertices.
    E.g.: Face 1: (v1, v2) ==> f1 = [v1,v2]

==> Vertex: contains the vertex's coordinates.
    E.g.: Vertex 1: (2,5) ==> v1 = [2,5]
          Vertex 2: (4,10) ==>  v2 = [4,10]   

"""

# Data Structures
""""
The figures can be separated by amount of vertices into categories.

The simple figures have less than 6 vertices.
The average figures have between 6 and 8 vertices.
The complex have more than 8 vertices.
"""

#For mouse event debugging
def callback(event):
    print("Clicked at", event.x, event.y)


##Vertices

### Arrow
v1_arrow = [10, 40]
v2_arrow = [30, 40]
v3_arrow = [30, 30]
v4_arrow = [50, 50]
v5_arrow = [30, 70]
v6_arrow = [30, 60]
v7_arrow = [10, 60]

### Triangle
v1_t1 = [100, 20]
v2_t1 = [140, 60]
v3_t1 = [60, 60]

### Cup
v1_cup = [160, 15]
v2_cup = [183, 33]
v3_cup = [183, 63]
v4_cup = [170, 70]
v5_cup = [200, 70]
v6_cup = [187, 63]
v7_cup = [187, 33]
v8_cup = [210, 15]

### Box
v1_box = [260, 20]
v2_box = [260, 60]
v3_box = [300, 60]
v4_box = [300, 20]

### Pentagon
v1_pent = [320, 38]
v2_pent = [330, 60]
v3_pent = [360, 60]
v4_pent = [370, 38]
v5_pent = [345, 20]

### Hexagon
v1_hexa = [400, 38]
v2_hexa = [400, 60]
v3_hexa = [425, 75]
v4_hexa = [450, 60]
v5_hexa = [450, 38]
v6_hexa = [425, 20]

#Heptagon 
v1_hep = [400, 38]
v2_hep = [395, 60]
v3_hep = [410, 75]
v4_hep = [440, 75]
v5_hep = [455, 60]
v6_hep = [450, 38]
v7_hep = [425, 20]

### Chair
v1_chair = [30, 100]
v2_chair = [30, 200]
v3_chair = [40, 200]
v4_chair = [40,170]
v5_chair = [80,170]
v6_chair = [80,200]
v7_chair = [90,200]
v8_chair = [90,160]
v9_chair = [40,160]
v10_chair = [40,100] 


### Star
v1_star = [140,115]
v2_star = [150,135]
v3_star = [170,140]
v4_star = [150,150]
v5_star = [160,170]
v6_star = [140,160]
v7_star = [120,170]
v8_star = [130,150]
v9_star = [110,140]
v10_star = [130,135]

### Bottle
v1_bottle = [190, 200, 0]
v2_bottle = [220, 200, 0]
v3_bottle = [220, 140, 0]
v4_bottle = [210, 130, 0]
v5_bottle = [210, 120, 0]
v6_bottle = [200, 120, 0]
v7_bottle = [200, 130, 0]
v8_bottle = [190, 140, 0]

# face tras
v1_bottlef2 = [190, 200, 20]
v2_bottlef2 = [220, 200, 20]
v3_bottlef2 = [220, 140, 20]
v4_bottlef2 = [210, 130, 20]
v5_bottlef2 = [210, 120, 20]
v6_bottlef2 = [200, 120, 20]
v7_bottlef2 = [200, 130, 20]
v8_bottlef2 = [190, 140, 20]


v1_bottlef3 = [190, 200, 0]
v2_bottlef3 = [190, 200, 20]
v3_bottlef3 = [190, 140, 20]
v4_bottlef3 = [200, 130, 20]
v5_bottlef3 = [200, 120, 20]
v6_bottlef3 = [200, 120, 0]
v7_bottlef3 = [200, 130, 0]
v8_bottlef3 = [190, 140, 0]

 
v1_bottlef4 = [220, 200, 0]
v2_bottlef4 = [220, 200, 20]
v3_bottlef4 = [220, 140, 20]
v4_bottlef4 = [210, 130, 20]
v5_bottlef4 = [210, 120, 20]
v6_bottlef4 = [210, 120, 0]
v7_bottlef4 = [210, 130, 0]
v8_bottlef4 = [220, 140, 0]


v1_bottle_topo = [210, 120, 0]
v2_bottle_topo = [200, 120, 0]
v3_bottle_topo = [200, 120, 20]
v4_bottle_topo = [210, 120, 20]

v1_bottle_base = [190, 200, 0]
v2_bottle_base = [220, 200, 0]
v3_bottle_base = [220, 200, 20]
v4_bottle_base = [190, 200, 20]


# lado 1 ##### (caso tenha duvida olhe o desenho enviado no grupo mais cedo)

#face maior
v1_lado1 = [220, 200, 0]
v2_lado1 = [220, 200, 20]   
v3_lado1 = [220, 140, 20]    # 3 e 4 fazem parte da face media
v4_lado1 = [220, 140, 0]

######### 
#face media
v9_lado1 = [220, 140, 0]
v10_lado1 = [220, 140, 20]
v5_lado1 =  [210, 130, 20]
v6_lado1 =  [210, 130, 0] # fazem parte da face pequena
##########
#face pequena
v11_lado1=[210, 130, 0]
v12_lado1=[210, 130, 20]
v7_lado1 = [210, 120, 20]
v8_lado1 = [210, 120, 0]
##############

#############
#lado 2#############(analogo)

#####
v1_lado2 = [190, 200, 0]
v2_lado2 = [190, 200, 20]
v3_lado2 = [190, 140, 20]
v4_lado2 = [190, 140, 0]
#####
v9_lado2=[190, 140, 0]
v10_lado2=[190, 140, 20]
v5_lado2 = [200, 130, 20]
v6_lado2 = [200, 130, 0]
#######
v11_lado2=[200, 130, 0]
v12_lado2= [200, 130, 20]
v7_lado2 = [200, 120, 20]
v8_lado2 = [200, 120, 0]

v1_tampa=[200, 130, 0]
v2_tampa=[200, 130, 20]
v3_tampa=[210, 130, 20]
v4_tampa=[210, 130, 0]

###
vertexes = [
    v1_arrow, v2_arrow, v3_arrow, v4_arrow, v5_arrow, v6_arrow, v7_arrow,
    v1_t1, v2_t1, v3_t1,
    v1_cup, v2_cup, v3_cup, v4_cup, v5_cup, v6_cup, v7_cup, v8_cup,
    v1_box, v2_box, v3_box, v4_box,
    v1_pent, v2_pent, v3_pent, v4_pent, v5_pent,
    v1_hexa, v2_hexa, v3_hexa, v4_hexa, v5_hexa, v6_hexa,
    v1_hep, v2_hep, v3_hep, v4_hep, v5_hep, v6_hep, v7_hep,
    v1_chair, v2_chair, v3_chair, v4_chair, v5_chair, v6_chair, v7_chair, v8_chair, v9_chair, v10_chair,
    v1_star, v2_star, v3_star, v4_star, v5_star, v6_star, v7_star, v8_star, v9_star, v10_star,
    v1_bottle, v2_bottle, v3_bottle, v4_bottle, v5_bottle, v6_bottle, v7_bottle, v8_bottle,
    v1_bottlef2, v2_bottlef2, v3_bottlef2, v4_bottlef2, v5_bottlef2, v6_bottlef2, v7_bottlef2, v8_bottlef2,
    v1_bottlef3,v2_bottlef3,v3_bottlef3,v4_bottlef3,v5_bottlef3,v6_bottlef3,v7_bottlef3,v8_bottlef3,
    v1_bottlef4,v2_bottlef4,v3_bottlef4,v4_bottlef4,v5_bottlef4,v6_bottlef4,v7_bottlef4,v8_bottlef4
    ]

## Faces
arrow_f1 = [vertexes[0], vertexes[1], vertexes[2], vertexes[3], vertexes[4], vertexes[5], vertexes[6]]
arrow_f2 = [vertexes[0], vertexes[6], vertexes[5], vertexes[4], vertexes[3], vertexes[2], vertexes[1]]

box_f1 = [vertexes[18], vertexes[19], vertexes[20], vertexes[21]]
box_f2 = [vertexes[18], vertexes[21], vertexes[20], vertexes[19]]

cup_f1 = [vertexes[10], vertexes[11], vertexes[12], vertexes[13], vertexes[14], vertexes[15], vertexes[16], vertexes[17]]
cup_f2 = [vertexes[10], vertexes[17], vertexes[16], vertexes[15], vertexes[14], vertexes[13], vertexes[12], vertexes[11]]

triangle_f1 = [vertexes[7], vertexes[8], vertexes[9]]
triangle_f2 = [vertexes[7], vertexes[9], vertexes[8]]

pentagon_f1 = [vertexes[22], vertexes[23], vertexes[24], vertexes[25], vertexes[26]]
pentagon_f2 = [vertexes[22], vertexes[26], vertexes[25], vertexes[24], vertexes[23]]

hexagon_f1 = [vertexes[27], vertexes[28], vertexes[29], vertexes[30], vertexes[31], vertexes[32]]
hexagon_f2 = [vertexes[27], vertexes[32], vertexes[31], vertexes[30], vertexes[29], vertexes[28]]

heptagon_f1 = [vertexes[33], vertexes[34], vertexes[35], vertexes[36], vertexes[37], vertexes[38], vertexes[39]]
heptagon_f2 = [vertexes[33], vertexes[39], vertexes[38], vertexes[37], vertexes[36], vertexes[35], vertexes[34]]

chair_f1 = [vertexes[40], vertexes[41], vertexes[42], vertexes[43], vertexes[44], vertexes[45], vertexes[46], vertexes[47], vertexes[48], vertexes[49]]
chair_f2 = [vertexes[40], vertexes[49], vertexes[48], vertexes[47], vertexes[46], vertexes[45], vertexes[44], vertexes[43], vertexes[42], vertexes[41]]

star_f1 = [vertexes[50], vertexes[51], vertexes[52], vertexes[53], vertexes[54], vertexes[55], vertexes[56], vertexes[57], vertexes[58], vertexes[59]]
star_f2 = [vertexes[50], vertexes[59], vertexes[58], vertexes[57], vertexes[56], vertexes[55], vertexes[54], vertexes[53], vertexes[52], vertexes[51]]

bottle_f1 = [vertexes[60], vertexes[61], vertexes[62], vertexes[63], vertexes[64], vertexes[65], vertexes[66], vertexes[67]]
bottle_f2 = [vertexes[68], vertexes[75], vertexes[74], vertexes[73], vertexes[72], vertexes[71], vertexes[70], vertexes[69]]
bottle_f3 = [vertexes[76], vertexes[77], vertexes[78], vertexes[79], vertexes[80], vertexes[81], vertexes[82], vertexes[83]]
bottle_f4 = [vertexes[84], vertexes[91], vertexes[90], vertexes[89], vertexes[88], vertexes[87], vertexes[86], vertexes[85]]
bottle_topo = [v1_bottle_topo, v2_bottle_topo, v3_bottle_topo, v4_bottle_topo]
bottle_base = [v1_bottle_base, v2_bottle_base, v3_bottle_base, v4_bottle_base]
bottle_tampa=[v1_tampa,v2_tampa,v3_tampa,v4_tampa]

#faces laterais
bottle_f5 = [v1_lado1,v2_lado1,v3_lado1,v4_lado1]
bottle_f6 = [v9_lado1,v10_lado1,v5_lado1,v6_lado1]
bottle_f7 = [v11_lado1,v12_lado1,v7_lado1,v8_lado1]

bottle_f8 = [v1_lado2,v2_lado2,v3_lado2,v4_lado2]
bottle_f9 = [v9_lado2,v10_lado2,v5_lado2,v6_lado2]
bottle_f10 =[v11_lado2,v12_lado2,v7_lado2,v8_lado2]

#bottle_f11 =[v5_lado1,v5_lado2]

faces = [
         arrow_f1, arrow_f2, box_f1, box_f2, cup_f1, cup_f2, triangle_f1, triangle_f2,
         pentagon_f1, pentagon_f2, hexagon_f1, hexagon_f2, heptagon_f1, heptagon_f2,
         chair_f1, chair_f2, star_f1, star_f2, bottle_f1, bottle_f2,bottle_f3,bottle_f4
        ]
      
# Figures

### Arrow
arrow_image = [faces[0], faces[1]]

### Box
box_image = [faces[2], faces[3]]

### Cup
cup_image = [faces[4], faces[5]]

### Triangle
triangle_image = [faces[6], faces[7]]

### Pentagon
pentagon_image = [faces[8], faces[9]]

### Hexagon
hexagon_image = [faces[10], faces[11]]

#Heptagon
heptagon_image = [faces[12],faces[13]]

### Chair
chair_image = [faces[14], faces[15]]

### Star 
star_image = [faces[16], faces[17]]

### Bottle
# testes:

#lado1 com as faces
#bottle_image = [faces[18],faces[19], faces[20], faces[21], bottle_base, bottle_topo,bottle_f5,bottle_f6,bottle_f7]
#lado 2 com as faces
#bottle_image = [faces[18],faces[19], faces[20], faces[21], bottle_base, bottle_topo,bottle_f8,bottle_f9,bottle_f10]

#face da parte da frente
#bottle_image = [faces[18],faces[19], faces[20], faces[21], bottle_base, bottle_topo,bottle_f11]

#tudo
bottle_image = [faces[18],faces[19], faces[20], faces[21], bottle_base, bottle_topo,bottle_f5,bottle_f6,bottle_f7,bottle_f8,bottle_f9,bottle_f10,bottle_tampa]

# Transformations 

## Scale
def scale_2D(image, k):
    position=translateOrigin(image)
    if(len(image) > 2):
        for face in image:
            for vertex in face:
                matrixScale=np.array([[k[0], 0, 0],
                                        [0, k[1], 0],
                                        [0, 0, 1]])
                matrixPosition=np.array([vertex[0],vertex[1],1])
                result=np.matmul(matrixScale,matrixPosition)
                vertex[0] = result[0]
                vertex[1] = result[1]
    else:
        face = image[0]
        for vertex in face:
                matrixScale=np.array([[k[0], 0, 0],
                                        [0, k[1], 0],
                                        [0, 0, 1]])
                matrixPosition=np.array([vertex[0],vertex[1],1])
                result=np.matmul(matrixScale,matrixPosition)
                vertex[0] = result[0]
                vertex[1] = result[1]
    translate_2D(image,position[0],position[1])
    return image

## Shear
def cisa_2D(image, k):
    position=translateOrigin(image)
    if(len(image) > 2):
        for face in image:
            for vertex in face:
                matrixScale=np.array([[1, k[0], 0],
                                        [k[1], 1, 0],
                                        [0, 0, 1]])
                matrixPosition=np.array([vertex[0],vertex[1],1])
                result=np.matmul(matrixScale,matrixPosition)
                vertex[0] = result[0]
                vertex[1] = result[1]
    else:
        face = image[0]
        for vertex in face:
                matrixScale=np.array([[1, k[0], 0],
                                        [k[1], 1, 0],
                                        [0, 0, 1]])
                matrixPosition=np.array([vertex[0],vertex[1],1])
                result=np.matmul(matrixScale,matrixPosition)
                vertex[0] = result[0]
                vertex[1] = result[1]
    translate_2D(image,position[0],position[1])
    return image

def translate_2D(image, x_amount, y_amount):
    if(len(image) <= 2):
        face = image[0]
        for vertex in face:
            matrixTranslate=np.array([[1, 0, x_amount],
                                [0, 1, y_amount],
                                [0, 0, 1]])
            matrixPosition=np.array([vertex[0],vertex[1],1])
            result=np.matmul(matrixTranslate,matrixPosition)
            vertex[0] = result[0]
            vertex[1] = result[1]
    else:
        for face in image:
            for vertex in face:
                matrixTranslate=np.array([[1, 0, x_amount],
                                    [0, 1, y_amount],
                                    [0, 0, 1]])
                matrixPosition=np.array([vertex[0],vertex[1],1])
                result=np.matmul(matrixTranslate,matrixPosition)
                vertex[0] = result[0]
                vertex[1] = result[1]
    return image

## Translate image midpoint to (0,0)
def translateOrigin(image):
    # Procurando os extremos para calcular o ponto medio
    esquerda = None
    direita = None
    cima = None
    baixo = None
    for face in image:
        for vertex in face:
            if ((esquerda == None) or (esquerda < vertex[0])):
                esquerda = vertex[0]
            if ((direita == None) or (direita > vertex[0])):
                direita = vertex[0]
            if ((cima == None) or (cima < vertex[1])):
                cima = vertex[1]
            if ((baixo == None) or (baixo > vertex[1])):
                baixo = vertex[1]
        # Calculando o ponto medio em relação  x e y e transladando a imagem para a origem
        medio_x = (direita - esquerda) / 2
        medio_y = (baixo - cima) / 2
        position=[esquerda + medio_x,cima + medio_y]
    image = translate_2D(image, -position[0], -position[1])
    return position

## Rotation
def rotation_2D(image, angle=90):
    radian = angle * (math.pi / 180)
    position=translateOrigin(image)
    if(len(image) > 2):
        # Fazendo a rotação
        for face in image:
            for vertex in face:
                matrixRotation=np.array([[math.cos(radian), (math.sin(radian))],[-(math.sin(radian)), math.cos(radian)]])

                vetorPosition=np.array([vertex[0],vertex[1]])
                result=np.matmul(matrixRotation,vetorPosition)
                vertex[0] = result[0]
                vertex[1] = result[1]
    else:
        face = image[0]
        for vertex in face:
            matrixRotation=np.array([[math.cos(radian), (math.sin(radian))],[-(math.sin(radian)), math.cos(radian)]])
            vetorPosition=np.array([vertex[0],vertex[1]])
            result=np.matmul(matrixRotation,vetorPosition)
            vertex[0] = result[0]
            vertex[1] = result[1]
        # Transladando a imagem pro ponto original
    image = translate_2D(image, position[0], position[1])
    return image


def isometric(image, angle_x=30, angle_y = 45):
    radian_x = angle_x * (math.pi / 180)
    radian_y = angle_y * (math.pi / 180)
    position=translateOrigin(image)
    # Fazendo a rotação
    for face in image:
        for vertex in face:
            # Cada vetor do array é uma linha da matriz            
            matrixRotation = np.array([ [math.cos(radian_y), math.sin(radian_y) * math.sin(radian_y), 0, 0],
                                        [0, math.cos(radian_x),0 ,0],
                                        [math.sin(radian_y), -(math.sin(radian_x) * math.cos(radian_y)), 0, 0],
                                        [0,0,0,1]]                                                             )                                           

            vetorPosition = np.array([vertex[0],vertex[1], vertex[2], 1])
            result=np.matmul(vetorPosition,matrixRotation)
            vertex[0] = result[0]
            vertex[1] = result[1]
            vertex[2] = result[2]
    # Transladando a imagem pro ponto original
    image = translate_2D(image, position[0], position[1])
    return image



#radio button
#valor = IntVar()
valor = 1
#valor.set(1)
total = 0

#Auxiliary functions
#Converte uma imagem para o SRD
def map_coords(image, width, height, screen_w, screen_h):
    for face in image:
        for vertex in face:
            vertex[0] = round((vertex[0] * width)/screen_w)
            vertex[1] = round((vertex[1] * height)/screen_h)
            #print(vertex[0], vertex[1])
    return image

#Converte as páginas para SRD
def map_pages(page_list, width, height, screen_w, screen_h):
    for i_page in page_list:
        for image in i_page:
            image = map_coords(image, width, height, screen_w, screen_h)

#Desenha uma imagem bidimensional face por face
def draw_image(image, canvas):
    image_pointer = []
    for face in image:
        polygon = canvas.create_polygon(face, fill='', outline='black')
        image_pointer.append(polygon)
    return image_pointer

#Transforma uma imagem 3D em 2D
def convert3D_to_2D(image):
    image_2D = []
    for face in range(0,len(image)):
        newFace=[]
        for vertex in range(0,len(image[face])):
            newFace.append(image[face][vertex][0:2])
        image_2D.append(newFace)
    return image_2D


# Inicialização da tela base (root)
root = Tk()                 #265,32   e 181,2    
canvas = Canvas(root, width=800, height=600)
canvas.bind("<Button-1>", callback)
canvas.pack()
root.update()

canvas_width = canvas.winfo_width()
canvas_height = canvas.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
font_size = int(min(canvas_width, screen_width) / 20)
print("Canvas %d x %d ======= Screen %d x %d" % (canvas_width, canvas_height, screen_width, screen_height))

# passa as coordenadas do bottle para 2d e ao mesmo tempo fazendo uma copia
bottle_2D = convert3D_to_2D(bottle_image)
# aplica transformação isométrica no bottle
isometric_bottle = isometric(bottle_image,30,45)
# converte para 2d para poder ser desenhado no tkinter
bottle = convert3D_to_2D(isometric_bottle)
#copia que será usada
bottle_copy = deepcopy(bottle)
bottle_coverpage = map_coords(bottle_copy, canvas_width, canvas_height, screen_width, screen_height)
translate_2D(bottle_coverpage, canvas_width * 0.33, canvas_height * 0.3)
scale_2D(bottle_coverpage, [2,2])
draw_image(bottle_coverpage, canvas)
canvas.create_text(canvas_width * 0.48, canvas_height * 0.65, font=("Helvetica", 10,"bold","italic"), text="Beba Água")

root.pages = []
root.answers = []
root.current_page = 0
root.start = 0
answers = root.answers
pages = root.pages


""" arrow = canvas.create_polygon(arrow_image, fill='', outline='black')
triangle = canvas.create_polygon(triangle_image, fill='', outline='black')
cup = canvas.create_polygon(cup_image, fill='', outline='black')
box = canvas.create_polygon(box_image, fill='', outline='black')
pentagon = canvas.create_polygon(pentagon_image, fill='', outline='black')
hexagon = canvas.create_polygon(hexagon_image, fill='', outline='black')
chair = canvas.create_polygon(chair_image, fill='', outline='black')
star = canvas.create_polygon(star_image, fill='', outline='black')
bottle = canvas.create_polygon(bottle_image, fill='', outline='black')
house = translate_2D(house_image, 50, 0)
house = canvas.create_polygon(house_image, fill='', outline='black') """


#Botões
# The method 'create_polygon' will decapsulate the structure by itself, no need to iterate through it.
# Removes fill(polygon is filled by default) and draws outline(invisible by default).
# Gets the pages from the root object and draw each page's images.
def exit_game():
    print("You spent %s seconds taking the test!" % (time.time() - root.start))
    return exit()

def back_menu():
    print("You spent %s seconds taking the test!" % (time.time() - root.start))
    root.start = 0
    menu_button.place_forget()
    exit_button.place_forget()
    next_button.place_forget()
    root.current_page = 0
    start_button.place(x=canvas.winfo_width()*0.42, y=canvas.winfo_height()*0.70)
    exit_button.place(x=canvas.winfo_width()*0.43, y=canvas.winfo_height()*0.80)
    canvas.create_image(canvas.winfo_width()*0.50, canvas.winfo_height()*0.25, image = img)
    draw_image(bottle_coverpage, canvas)
    canvas.create_text(canvas_width * 0.48, canvas_height * 0.65, font=("Helvetica", 10,"bold","italic"), text="Beba Água")

def next_page():
    if(root.current_page < 0):
        return  
    if(root.start == 0):
        root.start = time.time()
    start_button.place_forget()
    exit_button.place_forget()
    if(root.current_page >= 0 and root.current_page < len(pages) ):
        next_button.place(x=canvas.winfo_width()*0.40, y=canvas.winfo_height()*0.60)
    else:
        canvas.delete('all')
        next_button.place_forget()
        exit_button.place(x=canvas.winfo_width()*0.65, y=canvas.winfo_height()*0.70)
        menu_button.place(x=canvas.winfo_width()*0.25, y=canvas.winfo_height()*0.70)
        return
    
    canvas.delete('all')
    
    page_list = pages[root.current_page]
    
    
    for image in page_list:
        draw_image(image, canvas)
    position = midpoint(page_list[-1])
    question_mark = canvas.create_text(position[0] * 1.25, position[1], font=("Times New Roman", font_size), text="?")
    
    i = 0
    if(root.current_page < 6):
        answer_list = answers[root.current_page]
        for image in answer_list:
            #i+= 1
            #b = Radiobutton(options, text=i, variable=v, value=i) 
            draw_image(image, canvas)
    root.current_page += 1
    #total += valor
    #valor = 1



# Gets the midpoint of an image
def midpoint(image):
    esquerda = None
    direita = None
    cima = None
    baixo = None
    face = image[0]
    for vertex in face:
        if ((esquerda == None) or (esquerda < vertex[0])):
            esquerda = vertex[0]
        if ((direita == None) or (direita > vertex[0])):
            direita = vertex[0]
        if ((cima == None) or (cima < vertex[1])):
            cima = vertex[1]
        if ((baixo == None) or (baixo > vertex[1])):
            baixo = vertex[1]
    medio_x = (direita - esquerda) / 2
    medio_y = (baixo - cima) / 2
    position=[esquerda + medio_x,cima + medio_y]
    return position

# Creating the question's images

##First question 
arrow_origin = translateOrigin(arrow_image)


arrow1_pos = translate_2D(deepcopy(arrow_image),270,150)
#b = Radiobutton(canvas, text=1, variable=valor, value=1)
#b.place(x=270 , y=150)
arrow2_pos = translate_2D(deepcopy(arrow_image), 370, 150)
arrow3_pos = translate_2D(deepcopy(arrow_image), 470, 150)

arrow4_pos = translate_2D(deepcopy(arrow_image), 270, 250)
arrow5_pos = translate_2D(deepcopy(arrow_image), 370, 250)
arrow6_pos = translate_2D(deepcopy(arrow_image), 470, 250)

arrow7_pos = translate_2D(deepcopy(arrow_image), 270, 350)
arrow8_pos = translate_2D(deepcopy(arrow_image), 370, 350)

arrow2_pos = rotation_2D(arrow2_pos, 90)
arrow3_pos = rotation_2D(arrow3_pos, 180)

arrow4_pos = rotation_2D(arrow4_pos, 90)
arrow6_pos = rotation_2D(arrow6_pos, -90)

arrow7_pos = rotation_2D(arrow7_pos, 180)
arrow8_pos = rotation_2D(arrow8_pos, -90)

page1=[arrow1_pos, arrow2_pos, arrow3_pos, arrow4_pos, arrow5_pos, arrow6_pos, arrow7_pos, arrow8_pos]
pages.append(page1)


arrow9_pos = translate_2D(deepcopy(arrow_image),  770,200)
arrow10_pos = translate_2D(deepcopy(arrow_image), 870, 200)
arrow11_pos = translate_2D(deepcopy(arrow_image), 970, 200)

arrow12_pos = translate_2D(deepcopy(arrow_image), 770, 300)
arrow13_pos = translate_2D(deepcopy(arrow_image), 870, 300)
arrow14_pos = translate_2D(deepcopy(arrow_image), 970, 300)



arrow10_pos = rotation_2D(arrow10_pos, 90)
arrow11_pos = rotation_2D(arrow11_pos, 180)

arrow12_pos = rotation_2D(arrow12_pos, -90)
arrow13_pos = rotation_2D(arrow13_pos, -180)
arrow14_pos = rotation_2D(arrow14_pos, 270)


answers1=[arrow9_pos, arrow10_pos, arrow11_pos, arrow12_pos, arrow13_pos, arrow14_pos]
answers.append(answers1)

## Second question
triangle_position = translateOrigin(triangle_image)

triangle1_pos = translate_2D(deepcopy(triangle_image), 270, 150)
triangle2_pos = translate_2D(deepcopy(triangle_image), 370, 150)
triangle3_pos = translate_2D(deepcopy(triangle_image), 470, 150)

triangle4_pos = translate_2D(deepcopy(triangle_image), 270, 250)
triangle5_pos = translate_2D(deepcopy(triangle_image), 370, 250)
triangle6_pos = translate_2D(deepcopy(triangle_image), 470, 250)

triangle7_pos = translate_2D(deepcopy(triangle_image), 270, 350)
triangle8_pos = translate_2D(deepcopy(triangle_image), 370, 350)

triangle2_pos = scale_2D(triangle2_pos, [1,2])
triangle2_pos = translate_2D(triangle2_pos, 0, -20)

triangle3_pos = scale_2D(triangle3_pos, [0.5,0.5])
triangle3_pos = translate_2D(triangle3_pos, -20, 10)

triangle4_pos = scale_2D(triangle4_pos, [1,2])
triangle4_pos = translate_2D(triangle4_pos, 0, -20)

triangle6_pos = scale_2D(triangle6_pos, [0.5,0.5])
triangle6_pos = translate_2D(triangle6_pos, -20, 10)
triangle7_pos = scale_2D(triangle7_pos, [0.5,0.5])
triangle7_pos = translate_2D(triangle7_pos, 5, 10) 



triangle9_pos = scale_2D(translate_2D(deepcopy(triangle_image), 770,200),[1,3])
triangle10_pos = scale_2D(translate_2D(deepcopy(triangle_image), 870, 200),[1,2])
triangle10_pos = translate_2D(triangle10_pos,0,20)
triangle11_pos = scale_2D(translate_2D(deepcopy(triangle_image),970, 200),[1,0.5])
triangle11_pos = translate_2D(triangle11_pos,0,50)
triangle12_pos = translate_2D(deepcopy(triangle_image), 770, 300)
triangle13_pos = scale_2D(translate_2D(deepcopy(triangle_image), 870, 300),[0.5,1])
triangle14_pos = scale_2D(translate_2D(deepcopy(triangle_image), 970, 300),[0.5,0.5])
triangle14_pos = translate_2D(triangle14_pos,0,10)

page2 = [triangle1_pos, triangle2_pos, triangle3_pos, triangle4_pos, triangle5_pos, triangle6_pos, triangle7_pos, triangle8_pos]
pages.append(page2)

answers2=[triangle9_pos, triangle10_pos, triangle11_pos, triangle12_pos, triangle13_pos, triangle14_pos]
answers.append(answers2)


### Third question

chair_origin = translateOrigin(chair_image)

chair1_pos = translate_2D(deepcopy(chair_image), 320, 160)
chair2_pos = translate_2D(deepcopy(chair_image), 420, 160)

chair3_pos = translate_2D(deepcopy(chair_image), 320, 280)

chair1_pos = scale_2D(chair1_pos, [-1, 1])
chair3_pos = scale_2D(chair3_pos, [-1, -1])
page3 = [chair1_pos, chair2_pos, chair3_pos]
pages.append(page3)

chair4_pos = translate_2D(deepcopy(chair_image), 820, 160)
chair4_pos = scale_2D(chair4_pos,[-1,1])
chair5_pos = translate_2D(deepcopy(chair_image), 920, 160)
chair5_pos = scale_2D(chair5_pos,[-1,-1])
chair6_pos = rotation_2D(deepcopy(chair_image),270)
chair6_pos = translate_2D(chair6_pos, 1020, 160)

chair7_pos = scale_2D(translate_2D(deepcopy(chair_image), 820, 280),[1,-1])
chair8_pos = translate_2D(deepcopy(chair_image), 920, 280)
chair9_pos = rotation_2D(deepcopy(chair_image),270)
chair9_pos = scale_2D(translate_2D(chair9_pos, 1020, 280),[-1,1])

answers3=[chair4_pos, chair5_pos, chair6_pos, chair7_pos, chair8_pos, chair9_pos]
answers.append(answers3)

##fourth question
box_origin = translateOrigin(box_image)

box1_pos = translate_2D(deepcopy(box_image),270,150)

box2_pos = translate_2D(deepcopy(box_image), 350, 150)
box3_pos = translate_2D(deepcopy(box_image), 390, 150)

box4_pos = translate_2D(deepcopy(box_image), 470, 150)
box5_pos = translate_2D(deepcopy(box_image), 510, 150)
box6_pos = translate_2D(deepcopy(box_image), 550, 150)

box7_pos = translate_2D(deepcopy(box_image), 270, 250)
box8_pos = translate_2D(deepcopy(box_image), 310, 250)
box9_pos = translate_2D(deepcopy(box_image), 350, 250)
box10_pos = translate_2D(deepcopy(box_image), 390, 250)

box11_pos = translate_2D(deepcopy(box_image), 470, 250)
box12_pos = translate_2D(deepcopy(box_image), 510, 250)
box13_pos = translate_2D(deepcopy(box_image), 550, 250)
box14_pos = translate_2D(deepcopy(box_image), 590, 250)
box15_pos = translate_2D(deepcopy(box_image), 630, 250)


box16_pos = translate_2D(deepcopy(box_image), 270, 350)
box17_pos = translate_2D(deepcopy(box_image), 310, 350)
box18_pos = translate_2D(deepcopy(box_image), 350, 350)
box19_pos = translate_2D(deepcopy(box_image), 390, 350)
box20_pos = translate_2D(deepcopy(box_image), 430, 350)
box21_pos = translate_2D(deepcopy(box_image), 470, 350)


page4=[box1_pos, box2_pos, box3_pos,box4_pos,box5_pos,box6_pos,box7_pos,box8_pos,box9_pos,box10_pos,box11_pos,box12_pos,box13_pos,box14_pos,box15_pos
,box16_pos,box17_pos,box18_pos,box19_pos,box20_pos,box21_pos]
pages.append(page4)


box22_pos = translate_2D(deepcopy(box_image), 970, 150)
box23_pos = translate_2D(deepcopy(box_image), 1010, 150)
box24_pos = translate_2D(deepcopy(box_image), 1050, 150)
box25_pos = translate_2D(deepcopy(box_image), 1090, 150)
box26_pos = translate_2D(deepcopy(box_image), 1130, 150)
box27_pos = translate_2D(deepcopy(box_image), 1170, 150)


box28_pos = translate_2D(deepcopy(box_image), 970, 250)
box29_pos = translate_2D(deepcopy(box_image), 1010, 250)
box30_pos = translate_2D(deepcopy(box_image), 1050, 250)
box31_pos = translate_2D(deepcopy(box_image), 1090, 250)
box32_pos = translate_2D(deepcopy(box_image), 1130, 250)
box33_pos = translate_2D(deepcopy(box_image), 1170, 250)
box34_pos = translate_2D(deepcopy(box_image), 1210, 250)


box35_pos = translate_2D(deepcopy(box_image), 1290, 250)
box36_pos = translate_2D(deepcopy(box_image), 1330, 250)
box37_pos = translate_2D(deepcopy(box_image), 1370, 250)

box38_pos = translate_2D(deepcopy(box_image), 1290, 150)
box39_pos = translate_2D(deepcopy(box_image), 1330, 150)
box40_pos = translate_2D(deepcopy(box_image), 1370, 150)
box41_pos = translate_2D(deepcopy(box_image), 1410, 150)



box41_pos = translate_2D(deepcopy(box_image), 970, 350)
box42_pos = translate_2D(deepcopy(box_image), 1010, 350)
box43_pos = translate_2D(deepcopy(box_image), 1050, 350)
box44_pos = translate_2D(deepcopy(box_image), 1090, 350)
box45_pos = translate_2D(deepcopy(box_image), 1130, 350)
box46_pos = translate_2D(deepcopy(box_image), 1170, 350)
box47_pos = translate_2D(deepcopy(box_image), 1210, 350)
box48_pos = translate_2D(deepcopy(box_image), 1250, 350)
box49_pos = translate_2D(deepcopy(box_image), 1330, 350)

answers4=[box22_pos, box23_pos, box24_pos,box25_pos,box26_pos,box27_pos,box28_pos,box29_pos,box30_pos,box31_pos,box32_pos,box33_pos
,box34_pos,box35_pos,box36_pos,box37_pos,box38_pos,box39_pos,box40_pos,box41_pos,box42_pos,box43_pos,box44_pos,box45_pos,box46_pos
,box47_pos,box48_pos,box49_pos]
answers.append(answers4)

# Fifth question
penta_origin = translateOrigin(pentagon_image)
penta1_pos = translate_2D(deepcopy(pentagon_image),270,150)

penta2_pos = translate_2D(deepcopy(pentagon_image),390,150)
penta2_pos = rotation_2D(penta2_pos, 90)
penta2_pos = scale_2D(penta2_pos,[0.75,0.75])

penta3_pos = translate_2D(deepcopy(pentagon_image),510,150)
penta3_pos = rotation_2D(penta3_pos, 180)
penta3_pos = scale_2D(penta3_pos,[0.50,0.50])


penta4_pos = translate_2D(deepcopy(pentagon_image),270,250)
penta4_pos = rotation_2D(penta4_pos, 270)
penta4_pos = scale_2D(penta4_pos,[0.25,0.25])

penta5_pos = translate_2D(deepcopy(pentagon_image),390,250)
penta5_pos = rotation_2D(penta5_pos,360)
penta5_pos = scale_2D(penta5_pos,[1.25,1.25])

page5 = [penta1_pos,penta2_pos,penta3_pos,penta4_pos,penta5_pos]
pages.append(page5)

penta6_pos = scale_2D(translate_2D(deepcopy(pentagon_image),770,150),[1.5,1.5])
penta7_pos = rotation_2D(scale_2D(translate_2D(deepcopy(pentagon_image),890,150),[1.25,1.25]),270)
penta8_pos = rotation_2D(scale_2D(translate_2D(deepcopy(pentagon_image),1010,150),[1.25,1.25]),180)
penta9_pos = rotation_2D(scale_2D(translate_2D(deepcopy(pentagon_image),770,250),[1.5,1.5]),90)
penta10_pos = rotation_2D(scale_2D(translate_2D(deepcopy(pentagon_image),1010,250),[1.5,1.5]),270)
penta11_pos = rotation_2D(scale_2D(translate_2D(deepcopy(pentagon_image),890,250),[1.75,1.75]),90)
answers5 = [penta6_pos,penta7_pos,penta8_pos,penta9_pos,penta10_pos,penta11_pos]
answers.append(answers5)

## Sixth question

cup_origin = translateOrigin(cup_image)
star_origin = translateOrigin(star_image)
box_origin = translateOrigin(box_image)

cup1_pos = translate_2D(deepcopy(cup_image), 270, 150)
star1_pos = translate_2D(deepcopy(star_image), 270, 130)
star1_pos = scale_2D(star1_pos, [0.3, 0.3])

box19_pos = translate_2D(deepcopy(box_image), 370, 150)
arrow9_pos = translate_2D(deepcopy(arrow_image),370, 150)
arrow9_pos = scale_2D(arrow9_pos, [0.65,0.65])
arrow9_pos = rotation_2D(arrow9_pos, 90)

cup2_pos = translate_2D(deepcopy(cup_image), 470, 100)
star2_pos = translate_2D(deepcopy(star_image), 470, 70)
cup2_pos = scale_2D(cup2_pos, [1.5, 1.5])
star2_pos = scale_2D(star2_pos, [0.5,0.5])


cup3_pos = translate_2D(deepcopy(cup_image), 270, 250)
star3_pos = translate_2D(deepcopy(star_image), 270, 230)
star3_pos = scale_2D(star3_pos, [0.3,0.3])

arrow10_pos = translate_2D(deepcopy(arrow_image), 370, 250)
arrow10_pos = rotation_2D(arrow10_pos, 90)

cup4_pos = translate_2D(deepcopy(cup_image), 470, 200)
star4_pos = translate_2D(deepcopy(star_image), 470, 180)
star4_pos = scale_2D(star4_pos, [0.3,0.3])

cup5_pos = translate_2D(deepcopy(cup_image),270,350)
star5_pos = translate_2D(deepcopy(star_image), 270, 330)
star5_pos = scale_2D(star5_pos, [0.3,0.3])

box20_pos = translate_2D(deepcopy(box_image), 370, 350)
arrow11_pos = translate_2D(deepcopy(arrow_image), 370, 350)
arrow11_pos = scale_2D(arrow11_pos, [0.65,0.65])
arrow11_pos = rotation_2D(arrow11_pos, -90)

page6 = [cup1_pos, star1_pos, box19_pos, arrow9_pos, cup2_pos, star2_pos, cup3_pos, star3_pos, arrow10_pos,
        cup4_pos, star4_pos, cup5_pos, star5_pos, box20_pos, arrow11_pos]
pages.append(page6)


cup6_pos = translate_2D(deepcopy(cup_image), 770, 200)
star6_pos = translate_2D(deepcopy(star_image), 770, 170)
cup6_pos = scale_2D(cup6_pos, [1.5, 1.5])
star6_pos = scale_2D(star6_pos, [0.5,0.5])


cup7_pos = translate_2D(deepcopy(cup_image), 870, 200)
cup7_pos = translate_2D(deepcopy(cup_image), 870, 210)
star7_pos = translate_2D(deepcopy(star_image), 870, 190)
star7_pos = scale_2D(star7_pos, [0.3,0.3])

cup8_pos = translate_2D(deepcopy(cup_image), 970, 150)
star8_pos = translate_2D(deepcopy(star_image), 970, 120)
cup8_pos = scale_2D(cup8_pos, [1.5, 1.5])
star8_pos = scale_2D(star8_pos, [0.5,0.5])

cup9_pos = translate_2D(deepcopy(cup_image), 770, 300)
star9_pos = translate_2D(deepcopy(star_image), 770, 270)
cup9_pos = scale_2D(cup9_pos, [1.5, 1.5])
star9_pos = scale_2D(star9_pos, [0.5,0.5])

cup10_pos = translate_2D(deepcopy(cup_image), 870, 350)
star10_pos = translate_2D(deepcopy(star_image), 870, 320)
cup10_pos = scale_2D(cup10_pos, [1.75, 1.75])
star10_pos = scale_2D(star10_pos, [0.5,0.5])

cup11_pos = translate_2D(deepcopy(cup_image), 970, 370)
star11_pos = translate_2D(deepcopy(star_image), 970, 350)
star11_pos = scale_2D(star11_pos, [0.3,0.3])



answers6 = [cup6_pos, star6_pos,cup7_pos, star7_pos,cup8_pos, star8_pos,cup9_pos, star9_pos,cup10_pos, star10_pos,cup11_pos, star11_pos]
answers.append(answers6)

## Seventh question

hexagon_origin = translateOrigin(hexagon_image)
bottle_2D_image = [deepcopy(bottle_2D[0])]
bottle_img = scale_2D(bottle_2D_image, [0.7,0.7])
bottle_img = translateOrigin(bottle_2D_image)
pentagon_origin = translateOrigin(pentagon_image)

hex1_pos = translate_2D(deepcopy(hexagon_image), 270, 150)
box21_pos = translate_2D(deepcopy(box_image), 370, 150)
star6_pos = translate_2D(deepcopy(star_image), 470, 150 )

pent1_pos = translate_2D(deepcopy(pentagon_image), 270, 250)
triangle9_pos = translate_2D(deepcopy(triangle_image), 370, 250)
bottle1_pos = translate_2D(deepcopy(bottle_2D_image), 280, 200)

pent2_pos = translate_2D(deepcopy(pentagon_image), 270, 350)
triangle10_pos = translate_2D(deepcopy(triangle_image), 370, 350)

hex1_pos = cisa_2D(hex1_pos, [-0.225, 0])
box21_pos = cisa_2D(box21_pos, [-0.225, 0])
star6_pos = scale_2D(star6_pos, [1.5, 1.5])

pent1_pos = cisa_2D(pent1_pos, [-0.225, 0])
triangle9_pos = cisa_2D(triangle9_pos, [-0.225, 0])
bottle1_pos = scale_2D(bottle1_pos, [1.5, 1.5])

pent2_pos = cisa_2D(pent2_pos, [0.225, 0])
triangle10_pos = cisa_2D(triangle10_pos, [0.225, 0])

page7 = [hex1_pos, box21_pos, star6_pos, pent1_pos, triangle9_pos, bottle1_pos, pent2_pos, triangle10_pos]
pages.append(page7)



# eighth question
hep_origin = translateOrigin(heptagon_image)
star_origin = translateOrigin(star_image)

hep1_pos = translate_2D(deepcopy(heptagon_image),240,150)
star_pos1 = translate_2D(deepcopy(star_image),230,165)
starzinha1 = scale_2D(star_pos1,[0.15,0.15])

hep2_pos = translate_2D(deepcopy(heptagon_image),340,150)
starzinha2 = scale_2D(translate_2D(deepcopy(star_image),330,145),[0.15,0.15])

hep3_pos = scale_2D(translate_2D(deepcopy(heptagon_image),440,150),[1,-1])
starzinha3 = scale_2D(translate_2D(deepcopy(star_image),430,155),[0.15,0.15])

hep4_pos = scale_2D(translate_2D(deepcopy(heptagon_image),540,150),[1,-1])
starzinha4 = scale_2D(translate_2D(deepcopy(star_image),530,135),[0.15,0.15])

page8 = [hep1_pos,starzinha1,starzinha2,hep2_pos,starzinha3,hep3_pos,starzinha4,hep4_pos]
pages.append(page8)


## Ninth question
triangle11_pos = translate_2D(deepcopy(triangle_image), 270, 150)
box22_pos = translate_2D(deepcopy(box_image), 370, 150)
pent3_pos = translate_2D(deepcopy(pentagon_image), 460, 150)

page10 = [triangle11_pos, box22_pos, pent3_pos]
pages.append(page10)


#x question

box_origin = translateOrigin(deepcopy(box_image))

box1_pos = translate_2D(deepcopy(box_image),270,150)

box2_pos = translate_2D(deepcopy(box_image),370,150)
disto2_pos = cisa_2D(deepcopy(box2_pos), [1, 0])
box3_pos = translate_2D(deepcopy(box_image),470,150)
disto3_pos = cisa_2D(deepcopy(box3_pos), [2, 0])


box4_pos = translate_2D(deepcopy(box_image),270,230)

box5_pos = translate_2D(deepcopy(box_image),370,230)
disto5_pos = cisa_2D(deepcopy(box5_pos), [0, 1])
box6_pos = translate_2D(deepcopy(box_image),470,230)
disto6_pos = cisa_2D(deepcopy(box6_pos), [0, 2])


box7_pos = translate_2D(deepcopy(box_image),270,330)
box8_pos = translate_2D(deepcopy(box_image),370,330)
disto8_pos = cisa_2D(deepcopy(box8_pos), [1, 1])

pageX = [box1_pos,box2_pos,disto2_pos,box3_pos,disto3_pos,box4_pos,box5_pos,disto5_pos,box6_pos,disto6_pos,box7_pos,box8_pos,disto8_pos]
pages.append(pageX)

canvas.pack()
root.update()

map_pages(pages, canvas_width, canvas_height, screen_width, screen_height)
map_pages(answers, canvas_width, canvas_height, screen_width, screen_height)

start_button = Button(canvas, text="Começar o jogo!", command=next_page)
next_button = Button(canvas, text="Próxima página", command=next_page)

exit_button = Button(canvas, text="Sair do jogo!", command=exit_game)
menu_button = Button(canvas, text="Ir para o menu!", command=back_menu)

start_button.place(x=canvas.winfo_width()*0.42, y=canvas.winfo_height()*0.70)
exit_button.place(x=canvas.winfo_width()*0.43, y=canvas.winfo_height()*0.80)


file_path = "images/velosem-logo.png"


# logo = Image.open(file_path)
# logo_width, logo_height = logo.size
# logo_w_resize = round((logo_width * canvas_width)/screen_width)
# logo_h_resize = round((logo_height * canvas_height)/screen_height)
# logo.resize((logo_w_resize, logo_h_resize))
# img = ImageTk.PhotoImage(logo)
# canvas.create_image(canvas.winfo_width()*0.50, canvas.winfo_height()*0.25, image = img)


root.mainloop()