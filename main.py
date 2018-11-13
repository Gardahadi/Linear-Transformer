#boilerplate for PyOpenGL and GLUT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import draw

window = 0                                             # glut window number
width, height = 500, 400                               # window size

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Tubes Algeo EZ")            # create window with title
draw.get_points()
glutDisplayFunc(draw.draw)                                  # set draw function callback
glutIdleFunc(draw.idle)                                     # draw all the time
glutMainLoop()
