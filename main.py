#boilerplate for PyOpenGL and GLUT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import draw

window = 0                                             # glut window number
width, height = 500, 500                               # window size

def main():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("Tubes Algeo EZ")            # create window with title
    draw.initDraw()
    glutMainLoop()

if __name__ == '__main__':
    main()
