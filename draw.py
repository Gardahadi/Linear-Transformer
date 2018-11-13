from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import transform as Tf
import time

points = []
pointsInit = []
rgb = [0.9,0.9,0.8]
frames = 100

def get_points():
    global pointsInit, points
    n = int(input("Masukkan jumlah titik : "))
    for i in range(n):
        x,y = input(">> ").split(",")
        x = float(x)
        y = float(y)
        pointsInit.append([x,y])
        points.append([x,y])

def draw_axis():
    glBegin(GL_LINES)
    glColor3f(1,1,1)
    glVertex2f(-10,0)
    glVertex2f(10,0)
    glVertex2f(0,10)
    glVertex2f(0,-10)
    glEnd()

def draw_poly():
    glBegin(GL_POLYGON)

    for point in points:
        glVertex2f(point[0],point[1])

    glEnd()

def idle():
    global points
    cmd = input("$")
    if cmd=="reset":
        points = pointsInit
    elif cmd=="exit":
        exit()
    else:
        animator(cmd)
    draw()

## UNCOMMENT FUNGSI YANG SUDAH DIIMPLEMENTASIKAN
def animator(trcommand):
    global points, frames
    trtype = trcommand.split(" ")[0]
    params = trcommand.split(" ",1)[1]
    if trcommand!="multiple":
        for i in range(frames):
            if trtype=="translate":
                dx,dy = params.split(" ")
                dx = float(dx)/frames
                dy = float(dy)/frames
                Tf.translate(dx,dy,points)
            elif trtype=="dilate":
                dparams = pow(float(params),1/frames)
                #Tf.dilate(dparams,points)
            elif trtype=="rotate":
                deg,a,b = params.split(" ")
                ddeg = float(deg)/frames
                a = float(a)
                b = float(b)
                #Tf.rotate(ddeg,a,b,points)
            #elif trtype=="reflect":
                # TODO: Tentuin parameter refleksi untuk 5 jenis
                #Tf.reflect()
            elif trtype=="shear":
                sb,k = params.split(" ")
                k = pow(float(k),1/frames)
                #Tf.shear(sb,k,points)
            elif trtype=="stretch":
                sb,k = params.split(" ")
                k = pow(float(k),1/frames)
                #Tf.stretch(sb,k,points)
            elif trtype=="custom":
                a,b,c,d = params.split(" ")
                #Tf.custom(a,b,c,d,points)
            time.sleep(0.01)
            draw()
    elif trtype=="multiple":
        n = int(params)
        for i in range(n):
            cmd = input("...")
            animator(cmd)

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    glColor3f(rgb[0],rgb[1],rgb[2])
    draw_poly()
    draw_axis()
    glutSwapBuffers()                                  # important for double buffering
