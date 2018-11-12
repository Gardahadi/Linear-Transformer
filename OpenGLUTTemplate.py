#boilerplate for PyOpenGL and GLUT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 400                               # window size
anglePyramid = 0

def draw_axis():
    glBegin(GL_LINES)

    glColor3f(10.0, 10.0, 10.0)    # White
    glVertex3f(-10.0, 0.0, 0.0)    # Sb X
    glVertex3f(10.0, 0.0, 0.0)    # Sb X

    glColor3f(10.0, 10.0, 10.0)    # White
    glVertex3f(0.0, -10.0, 0.0)    # Sb Y
    glVertex3f(0.0, 10.0, 0.0)    # Sb Y

    glColor3f(10.0, 10.0, 10.0)    # White
    glVertex3f(0.0, 0.0, -10.0)    # Sb Z
    glVertex3f(0.0, 0.0, 10.0)    # Sb Z

    glEnd()

def draw_cube():
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    # Top face (y = 0.5)
    # Define vertices in counter-clockwise (CCW) order with normal pointing out
    glColor3f(0.0, 1.0, 0.0)     # Green
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5,  0.5)
    glVertex3f( 0.5, 0.5,  0.5)

    # Bottom face (y = -0.5)
    glColor3f(1.0, 0.5, 0.0)     # Orange
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)

    # Front face  (z = 0.5)
    glColor3f(1.0, 0.0, 0.0)     # Red
    glVertex3f( 0.5,  0.5, 0.5)
    glVertex3f(-0.5,  0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f( 0.5, -0.5, 0.5)

    # Back face (z = -0.5)
    glColor3f(1.0, 1.0, 0.0)     # Yellow
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)

    # Left face (x = -0.5)
    glColor3f(0.0, 0.0, 1.0)     # Blue
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    # Right face (x = 0.5)
    glColor3f(1.0, 0.0, 1.0)     # Magenta
    glVertex3f(0.5,  0.5, -0.5)
    glVertex3f(0.5,  0.5,  0.5)
    glVertex3f(0.5, -0.5,  0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glEnd()

def draw():                                            # ondraw is called all the time
    global anglePyramid
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    gluLookAt(0, 0, 0, -100.0, -100.0, -100.0, 0.0,-1.0,0.0)
    draw_cube()
    glRotatef(anglePyramid, 0.0, 0.0, 1.0)

    anglePyramid += 99

    glutSwapBuffers()                                  # important for double buffering

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Boilerplate OpenGL")                  # create window with title
glEnable(GL_DEPTH_TEST)                                # remove unseen faces
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()
