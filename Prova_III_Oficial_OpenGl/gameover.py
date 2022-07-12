from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL._bytes import as_8_bit

PROMPT = ("Game Over")



x = 100
y = 150





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


    glFlush()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(1000, 1000)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("_MENU_INICIAL_")
glClearColor(0, 0, 0, 1)
glutDisplayFunc(display) 
glutMainLoop()