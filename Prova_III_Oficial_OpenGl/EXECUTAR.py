from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL._bytes import as_8_bit

PROMPT = ("COMPUTAÇÃO GRÁFICA")
PROMPT_1 = ("UFMA - ENGENHARIA DA COMPUTAÇÃO")
PROMPT_2 = ("SpaceX - EXPLORANDO OS MUNDOS ")
PROMPT_3 = ("Pressione a Tecla -c- para continuar ...")


x = 65
y = 250

z = 43
w = 230

g = 23
h = 150

n = 23
m = 130






def display():
    global x, y, z, w, g, h, n, m, l, k, Q, A, T, V, B, X, S, Z
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        x += 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

    glRasterPos2d(z,w)
    for d in PROMPT_1:
        glRasterPos(z, w)
        z += 7.0
        for e in d:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(e))

    glRasterPos2d(g,h)
    for i in PROMPT_2:
        glRasterPos(g, h)
        g += 7.0
        for j in i:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(j))

    glRasterPos2d(n,m)
    for u in PROMPT_3:
        glRasterPos(n, m)
        n += 7.0
        for U in u:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(U))

    glFlush()

def teclado(key, x, y):
    if ord(key) == 99:
        import versao3

    display()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(1000, 1000)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("_MENU_INICIAL_")
glClearColor(0, 0, 0, 1)
glutKeyboardFunc(teclado)
glutDisplayFunc(display) 
glutMainLoop()