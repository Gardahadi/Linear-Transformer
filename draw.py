from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import transform as Tf
import time

points = []
pointsInit = []
cube = [[100,100,100],
        [100,100,-100],
        [100,-100,100],
        [100,-100,-100],
        [-100,100,-100],
        [-100,100,100],
        [-100,-100,-100],
        [-100,-100,100]]
cubeInit = []
mode = ''
rgb = [0.9,0.9,0.8]
frames = 100

def initDraw():
    global mode
    mode = input("Pilih Mode [2]D atau [3]D: ")
    if mode=='2':
        get_points()
        glutIdleFunc(idle)                                     # draw all the time
    elif mode=='3':
        glEnable(GL_DEPTH_TEST)                                # remove unseen faces
        for P in cube:
            cubeInit.append([P[0],P[1],P[2]])
        glutIdleFunc(idle)
    else:
        exit()
    glutDisplayFunc(draw)                                  # set draw function callback

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
    glVertex2f(-500,0)
    glVertex2f(500,0)

    glVertex2f(0,500)
    glVertex2f(0,-500)
    #Sb X+
    glColor3f(1,0,0)
    glVertex2f(0,0)
    glVertex2f(500,0)
    #Sb Y+
    glColor3f(0,1,0)
    glVertex2f(0,0)
    glVertex2f(0,500)
    glEnd()

def draw_axis3():
    glBegin(GL_LINES)
    glColor3f(1,1,1)
    glVertex3f(-5000,0,0)
    glVertex3f(0,0,0)

    glVertex3f(0,0,0)
    glVertex3f(0,-5000,0)

    glVertex3f(0,0,0)
    glVertex3f(0,0,-5000)
    #Sb X+
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(5000,0,0)
    #Sb Y+
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,5000,0)
    #Sb Z+
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,5000)
    glEnd()

def draw_poly():
    glBegin(GL_POLYGON)

    for point in points:
        glVertex2f(point[0],point[1])

    glEnd()

def draw_cube():
    glBegin(GL_QUADS)

    # Draw quads by cube points in CCW direction
    # Top face (y = 100)
    glColor3f(0.2, 0.6, 0.2)     # Green
    glVertex3f(cube[0][0], cube[0][1], cube[0][2])
    glVertex3f(cube[1][0], cube[1][1], cube[1][2])
    glVertex3f(cube[4][0], cube[4][1], cube[4][2])
    glVertex3f(cube[5][0], cube[5][1], cube[5][2])
    # Bottom face (y = -100)
    glColor3f(1.0, 0.5, 0.0)     # Orange
    glVertex3f(cube[2][0], cube[2][1], cube[2][2])
    glVertex3f(cube[3][0], cube[3][1], cube[3][2])
    glVertex3f(cube[6][0], cube[6][1], cube[6][2])
    glVertex3f(cube[7][0], cube[7][1], cube[7][2])
    # Front face  (x = 100)
    glColor3f(0.6, 0.2, 0.2)     # Red
    glVertex3f(cube[0][0], cube[0][1], cube[0][2])
    glVertex3f(cube[2][0], cube[2][1], cube[2][2])
    glVertex3f(cube[3][0], cube[3][1], cube[3][2])
    glVertex3f(cube[1][0], cube[1][1], cube[1][2])
    # Back face (x = -100)
    glColor3f(1.0, 1.0, 0.0)     # Yellow
    glVertex3f(cube[5][0], cube[5][1], cube[5][2])
    glVertex3f(cube[7][0], cube[7][1], cube[7][2])
    glVertex3f(cube[6][0], cube[6][1], cube[6][2])
    glVertex3f(cube[4][0], cube[4][1], cube[4][2])
    # Left face (z = 100)
    glColor3f(0.2, 0.2, 0.6)     # Blue
    glVertex3f(cube[0][0], cube[0][1], cube[0][2])
    glVertex3f(cube[5][0], cube[5][1], cube[5][2])
    glVertex3f(cube[7][0], cube[7][1], cube[7][2])
    glVertex3f(cube[2][0], cube[2][1], cube[2][2])
    # Right face (z = -100)
    glColor3f(1.0, 0.0, 1.0)     # Magenta
    glVertex3f(cube[1][0], cube[1][1], cube[1][2])
    glVertex3f(cube[3][0], cube[3][1], cube[3][2])
    glVertex3f(cube[6][0], cube[6][1], cube[6][2])
    glVertex3f(cube[4][0], cube[4][1], cube[4][2])

    glEnd()

def idle():
    global points,rgb
    #The cmd Variable will store input from user
    cmd = input("$ ")
    if cmd=="reset":
        if mode=='2':
            points = []
            for p in pointsInit:
                points.append([p[0],p[1]])
        elif mode=='3':
            cube = []
            for p in cubeInit:
                cube.append([p[0],p[1],p[2]])
    elif cmd=="color":
        rgb[0] = float(input("New R Value :"))
        rgb[1] = float(input("New G Value :"))
        rgb[2] = float(input("New B Value :"))
    elif cmd=="exit":
        exit()
    else:
        animator(cmd)
    draw()

def animator(trcommand):
    global points, frames
    trtype = trcommand.split(" ")[0]
    params = trcommand.split(" ",1)[1]
    if trtype=="reflect":
        Tf.reflect(params,points)
    elif trtype=="custom":
        a,b,c,d = params.split(" ")
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        Tf.custom(a,b,c,d,points)
    elif trtype=="multiple":
        n = int(params)
        cmdlist = []
        for i in range(n):
            cmd = input("... ")
            cmdlist.append(cmd)
        for cmddo in cmdlist:
            animator(cmddo)
            time.sleep(0.5)
    else:
        for i in range(frames):
            if trtype=="translate":
                dx,dy = params.split(" ")
                dx = float(dx)/frames
                dy = float(dy)/frames
                Tf.translate(dx,dy,points)
            elif trtype=="dilate":
                dparams = pow(float(params),1/frames)
                Tf.dilate(dparams,points)
            elif trtype=="rotate":
                deg,a,b = params.split(" ")
                ddeg = float(deg)/frames
                a = float(a)
                b = float(b)
                Tf.rotate(ddeg,a,b,points)
            elif trtype=="shear":
                sb,k = params.split(" ")
                k = float(k)/frames
                Tf.shear(sb,k,points)
            elif trtype=="stretch":
                sb,k = params.split(" ")
                k = pow(abs(float(k)),1/frames)*(float(k)/abs(float(k)))
                Tf.stretch(sb,k,points)
            time.sleep(0.01)
            draw()


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    if mode=='2':
        glOrtho(-500,500,-500,500,0,1)
        draw_axis()
        glColor3f(rgb[0], rgb[1], rgb[2])
        draw_poly()
    elif mode=='3':
        glOrtho(-500,500,-500,500,-1000,1000)
        gluLookAt(0, 0, 0, -45.0, -75.0, -100.0, 0.0,1.0,0.0)
        draw_axis3()
        draw_cube()
    glutSwapBuffers()                                  # important for double buffering
