from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import draw

"""
Command Usage:
    translate <dx> <dy>	    : Translasi objek sebesar dx pada sumbu x dan dy pada sumbu y
    dilate <k>		        : Dilatasi objek dengan skala k
    rotate <deg> <a> <b>	: Rotasi objek berlawanan arah jarum jam (CCW) sebesar deg terhadap titik a,b
    reflect <param>		    : Pencerminan objek terhadap sumbu atau titik a,b pada parameter
    			              Parameter valid : x | y | x=y | x=-y | (<a>,<b>)
    shear <x|y> <k>		    : Shear pada objek dengan skala k, relatif terhadap sumbu x atau y
    stretch <x|y> <k>	    : Stretch pada objek dengan skala k, relatif terhadap sumbu x atau y
    custom <a> <b> <c> <d>	: Transformasi linier pada objek dengan matriks transformasi berikut
    			              |a b|
    			              |c d|
    multiple <n>		    : Melakukan transformasi linear pada objek sebanyak n kali secara berurutan
    color                   : Recolor shape
    reset			        : Mengembalikan objek ke kondisi awal
    exit			        : Exit program"""

window = 0                                             # GLUT window number
width, height = 500, 500                               # Window size

def main():
    glutInit()                                             # Initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # Set window size
    glutInitWindowPosition(0, 0)                           # Set window position
    window = glutCreateWindow("Skidipapkuy's Tubes Algeo")  # Create window with title
    draw.initDraw()
    glutMainLoop()

if __name__ == '__main__':
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X

    print("")
    print("  ███████╗██╗  ██╗██████╗ ██████╗  █████╗ ██████╗ ")
    print("  ██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
    print("  ███████╗█████╔╝ ██████╔╝██████╔╝███████║██████╔╝")
    print("  ╚════██║██╔═██╗ ██╔═══╝ ██╔═══╝ ██╔══██║██╔═══╝ ")
    print("  ███████║██║  ██╗██║     ██║     ██║  ██║██║     ")
    print("  ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝     ")
    print("  ========Linear Transformation Visualizer========")
    print("")
    main()
