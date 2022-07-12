print("PARA USAR O PROGRAMA UTILIZE AS SEGUINTES TECLAS:\nOBS: VALORIZE A DIFERENÇA ENTRE LETRAS MAIÚSCULAS E MINÚSCULAS")
print("w - PARA CIMA")
print("s - PARA BAIXO")
print("Espaço - PARA PAUSAR O JOGO")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

tran_x = 0
tran_y = 0
tran_xas = 0
tran_yas = 0
teste = 0
x = 0.10
tempo = 0
contador_de_vidas = 0
vitoria = 0





def display():

    # Nave 
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-15,15,-15,15)
    glTranslatef(tran_x, tran_y, 0)
    glBegin(GL_POLYGON)
    glColor3f(255,0,0)
    glVertex2f(-14,2)
    glColor3f(0,0,255)
    glVertex2f(-11,2)
    glVertex2f(-10,1)
    glVertex2f(-11,0)
    glColor3f(255,0,0)
    glVertex2f(-14,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0,0,255)
    glVertex2f(-14,4)
    glVertex2f(-12,2)
    glVertex2f(-14,2)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0,0,255)
    glVertex2f(-14,-2)
    glVertex2f(-12,0)
    glVertex2f(-14,0)
    glEnd()

    glFlush()

    #Obstaculos 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-15,15,-15,15)
    glTranslatef(tran_xas, tran_yas, 0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0,0)
    glVertex2f(0,15)
    glColor3f (0.0, 0.0, 0.0)
    glVertex2f(3,15)
    glVertex2f(3,0)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(20, 0)
    glVertex2f(20, -20)
    glColor3f (0.0, 0.0, 0.0)
    glVertex2f(17, -20)
    glVertex2f(17, 0)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(35, 0)
    glVertex2f(35, 20)
    glColor3f (0.0, 0.0, 0.0)
    glVertex2f(32, 20)
    glVertex2f(32, 0)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(50, 0)
    glVertex2f(50, -20)
    glColor3f (0.0, 0.0, 0.0)
    glVertex2f(47, -20)
    glVertex2f(47, 0)

    glEnd()

    glFlush()


def temporizador(value):

    global tran_yas, tran_xas, teste, x, tempo, tran_y, tran_x, contador_de_vidas, vitoria
    
    if teste == 1:
        tran_xas = tran_xas - x
        tempo+=1


        #print("Seu tempo atual é:", tempo)

        if ( -20 < tran_y < 0):
            if ( -35 < tran_xas < -31):
                contador_de_vidas += 1

        if ( 0 < tran_y < 20):
            if ( -16 < tran_xas < -12):
                contador_de_vidas  += 1

        if ( 0 < tran_y < 20):
            if ( -47 < tran_xas < -43):
                contador_de_vidas  += 1
        
        if ( -20 < tran_y < 0):
            if ( -65 < tran_xas < -60):
                contador_de_vidas  += 1

        if (tran_xas < -70):
            tran_xas = 20 
            x += 0.0050
            vitoria += 1
            print(vitoria)

        if (vitoria > 7):
            import vitoria
            glutDestroyWindow(display)


        if (contador_de_vidas == 60):
            import gameover 
            glutDestroyWindow(display)




    glutTimerFunc(10,temporizador, 1)
    display()


def teclado(key, x, y):
    global escala, tran_y, tran_x, rotacao, ang, teste

    if ord(key) == 119:
        tran_y = tran_y + 1
        teste = 1

    elif ord(key) == 115:
        tran_y = tran_y - 1
        teste = 1

    elif ord(key) == 32:
        teste = 2
    
    display()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(1000, 1000)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("SpaceX - Explorando Mundos")
glClearColor(1, 1, 1, 1)
glutTimerFunc(10,temporizador, 1)
glutKeyboardFunc(teclado)
glutDisplayFunc(display)
glutMainLoop()