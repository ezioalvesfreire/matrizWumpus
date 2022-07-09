from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL import Image
import numpy



def create_square(color, position):
    glColor3d(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    glVertex2d(position[0][0], position[0][1])
    glVertex2d(position[1][0], position[1][1])
    glVertex2d(position[2][0], position[2][1])
    glVertex2d(position[3][0], position[3][1])

    glEnd()
    glFlush()


def re_create():
    glClearColor(0.4, 0.4, 0.4, 1.0)  # cor de fundo
    glClear(GL_COLOR_BUFFER_BIT)

    # primeira coluna
    create_square((0.75, 0.56, 0), ((1, 1), (6, 1), (6, 6), (1, 6)))  # amarelo Stench
    create_square((0.47, 0.24, 0.015), ((1, 7), (6, 7), (6, 12), (1, 12)))  # Wumpus
    create_square((0.75, 0.56, 0), ((1, 13), (6, 13), (6, 18), (1, 18)))  # amarelo Stench
    create_square((0.5, 0.5, 0.5), ((1, 19), (6, 19), (6, 24), (1, 24)))  # Cinza Agent
    # segunda coluna
    create_square((1, 1, 1), ((7, 1), (12, 1), (12, 6), (7, 6)))  # Branco
    create_square((0.83, 0.91, 0.82), ((7, 7), (12, 7), (12, 12), (7, 12)))  # Ouro, Stench, Breeze
    create_square((1, 1, 1), ((7, 13), (12, 13), (12, 18), (7, 18)))  # Branco
    create_square((0.64, 0.76, 0.95), ((7, 19), (12, 19), (12, 24), (7, 24)))  # Azul breeze
    # terceira coluna
    create_square((0.64, 0.76, 0.95), ((13, 1), (18, 1), (18, 6), (13, 6)))  # Azul Breeze
    create_square((0, 0, 0), ((13, 7), (18, 7), (18, 12), (13, 12)))  # preto pit
    create_square((0.64, 0.76, 0.95), ((13, 13), (18, 13), (18, 18), (13, 18)))  # Azul Breeze
    create_square((0, 0, 0), ((13, 19), (18, 19), (18, 24), (13, 24)))  # Preto Pit
    # Quarta coluna
    create_square((0, 0, 0), ((19, 1), (24, 1), (24, 6), (19, 6)))  # Preto Pit
    create_square((0.64, 0.76, 0.95), ((19, 7), (24, 7), (24, 12), (19, 12)))  # Azul Breeze
    create_square((1, 1, 1), ((19, 13), (24, 13), (24, 18), (19, 18)))  # Branco
    create_square((0.64, 0.76, 0.95), ((19, 19), (24, 19), (24, 24), (19, 24)))  # Azul Breeza



   # agente = Image.open("imagens/agente/arqueiro.png")
   # img_data = numpy.array(list(agente.getdata()), numpy.uint8)
   # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, agente.width, agente.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
   # glEnable(GL_TEXTURE_2D)


def tecle(key, x=0, y=0):
    if ord(key) == 27:
        exit()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(520, 400)
glutCreateWindow(b'WOLRD WUMPUS')
glutDisplayFunc(re_create)
glutKeyboardFunc(tecle)
glOrtho(-2, 27, -2, 27, -1, 1)
glutMainLoop()
