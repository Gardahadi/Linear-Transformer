#boilerplate for PyOpenGL and GLUT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

window = 0                                             # glut window number
width, height = 500, 400                               # window size
points = [[0,0.5],[0.5,0],[0,-0.5],[-0.5,0]]
pointsInit = [[0,0.5],[0.5,0],[0,-0.5],[-0.5,0]]
rgb = [0.3,0.5,0.7]

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
    global points, rgb
    cmd = input("$")
    if cmd[0]=="e":
        print(cmd)
    elif cmd[0]=="a":
        x,y = cmd.split(" ")[1].split(",")
        x = float(x)
        y = float(y)
        points.append([x,y])
    elif cmd[0]=="c":
        r,g,b = cmd.split(" ")[1].split(",")
        rgb[0] = float(r)
        rgb[1] = float(g)
        rgb[2] = float(b)
    elif cmd[0]=="t":
        dx,dy = cmd.split(" ")[1].split(",")
        dx = float(dx)
        dy = float(dy)
        frames = 60
        for i in range(frames):
            for p in points:
                p[0] += dx/frames
                p[1] += dy/frames
            time.sleep(0.01)
            draw()
    elif cmd[0]=="r":
        points = pointsInit
    elif cmd[0]=="x":
        exit()
    draw()

def draw():                                            # ondraw is called all the time
    global anglePyramid
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    glColor3f(rgb[0],rgb[1],rgb[2])
    draw_poly()
    draw_axis()
    glutSwapBuffers()                                  # important for double buffering

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Boilerplate OpenGL")        # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(idle)                                     # draw all the time
glutMainLoop()
