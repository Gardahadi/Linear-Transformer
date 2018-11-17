from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import transform as Tf
import time

points = []
pointsInit = []
cubeInit = [[100,100,100],
        [100,100,-100],
        [100,-100,100],
        [100,-100,-100],
        [-100,100,-100],
        [-100,100,100],
        [-100,-100,-100],
        [-100,-100,100]]
mode = ''
rgb = [0.9,0.9,0.8]
validCmd = ["reflect","custom","multiple","translate","dilate","rotate","shear","stretch"]
frames = 100

def initDraw():
    global mode
    mode = input("Pilih Mode [2]D atau [3]D: ")
    while mode!='2' and mode!='3' and mode!='exit':
        mode = input("Input tidak valid! Pilih Mode [2]D atau [3]D: ")

    if mode=='2':
        get_points()                                           # 2D Points initialization
        glutIdleFunc(idle)
    elif mode=='3':
        glEnable(GL_DEPTH_TEST)                                # Remove unseen faces
        for P in cubeInit:
            points.append([P[0],P[1],P[2]])                    # 3D Points initialization
        glutIdleFunc(idle)
    elif mode=='exit':
        exit()

    glutDisplayFunc(draw)                                  # Set draw function callback

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
    glVertex3f(points[0][0], points[0][1], points[0][2])
    glVertex3f(points[1][0], points[1][1], points[1][2])
    glVertex3f(points[4][0], points[4][1], points[4][2])
    glVertex3f(points[5][0], points[5][1], points[5][2])
    # Bottom face (y = -100)
    glColor3f(1.0, 0.5, 0.0)     # Orange
    glVertex3f(points[2][0], points[2][1], points[2][2])
    glVertex3f(points[3][0], points[3][1], points[3][2])
    glVertex3f(points[6][0], points[6][1], points[6][2])
    glVertex3f(points[7][0], points[7][1], points[7][2])
    # Front face  (x = 100)
    glColor3f(0.6, 0.2, 0.2)     # Red
    glVertex3f(points[0][0], points[0][1], points[0][2])
    glVertex3f(points[2][0], points[2][1], points[2][2])
    glVertex3f(points[3][0], points[3][1], points[3][2])
    glVertex3f(points[1][0], points[1][1], points[1][2])
    # Back face (x = -100)
    glColor3f(1.0, 1.0, 0.0)     # Yellow
    glVertex3f(points[5][0], points[5][1], points[5][2])
    glVertex3f(points[7][0], points[7][1], points[7][2])
    glVertex3f(points[6][0], points[6][1], points[6][2])
    glVertex3f(points[4][0], points[4][1], points[4][2])
    # Left face (z = 100)
    glColor3f(0.2, 0.2, 0.6)     # Blue
    glVertex3f(points[0][0], points[0][1], points[0][2])
    glVertex3f(points[5][0], points[5][1], points[5][2])
    glVertex3f(points[7][0], points[7][1], points[7][2])
    glVertex3f(points[2][0], points[2][1], points[2][2])
    # Right face (z = -100)
    glColor3f(1.0, 0.0, 1.0)     # Magenta
    glVertex3f(points[1][0], points[1][1], points[1][2])
    glVertex3f(points[3][0], points[3][1], points[3][2])
    glVertex3f(points[6][0], points[6][1], points[6][2])
    glVertex3f(points[4][0], points[4][1], points[4][2])

    glEnd()

def displayHelp():
    print("\nSumbu merah : X+")
    print("Sumbu hijau : Y+")
    if mode=='3':
        print("Sumbu biru : Z+")
    print("\nList Command :")
    if mode=='2':
        print("    translate <dx> <dy>	  ")
        print("    dilate <k>		      ")
        print("    rotate <deg> <a> <b>	  ")
        print("    reflect <x|y|x=y|x=-y|(<a>,<b>)>")
        print("    shear <x|y> <k>		  ")
        print("    stretch <x|y> <k>	  ")
        print("    custom <a> <b> <c> <d> ")
        print("    color                  ")
    elif mode=='3':
        print("    translate <dx> <dy> <dz> ")
        print("    dilate <k>		        ")
        print("    rotate <deg> <a> <b> <c> ")
        print("    reflect <xy | yz | xz | (<a>,<b>,<c>)>      ")
        print("    shear <x | y | z | xy | yz | xz> <k> [<k2>] ")
        print("    stretch <x|y|z> <k>	      ")
        print("    custom <a b c d e f g h i> ")
    print("    multiple <n>	")
    print("    reset		")
    print("    exit			\n")

def idle():
    global points,rgb
    #The cmd variable will store input from user
    cmd = input("$ ")

    if cmd=="reset":
        if mode=='2':
            points = []
            for p in pointsInit:
                points.append([p[0],p[1]])
        elif mode=='3':
            points = []
            for p in cubeInit:
                points.append([p[0],p[1],p[2]])

    elif cmd=="color":
        rgb[0] = float(input("New R Value :"))
        rgb[1] = float(input("New G Value :"))
        rgb[2] = float(input("New B Value :"))

    elif cmd=="help" or cmd=="?":
        displayHelp()

    elif cmd=="exit":
        exit()

    else:
        animator(cmd)
    draw()

def animator(trcommand):
    global points, frames
    try:
        trtype = trcommand.split(" ")[0]
        params = trcommand.split(" ",1)[1]
        if trtype=="reflect":
            if mode=='2':
                Tf.reflect(points,params)
            elif mode=='3' :
                Tf.reflect3D(points,params)

        elif trtype=="custom":
            if mode=='2':
                a,b,c,d = params.split(" ")
                a = float(a)
                b = float(b)
                c = float(c)
                d = float(d)
                Tf.custom(points,a,b,c,d)
            elif mode=='3' :
                a,b,c,d,e,f,g,h,i = params.split(" ")
                a = float(a)
                b = float(b)
                c = float(c)
                d = float(d)
                e = float(e)
                f = float(f)
                g = float(g)
                h = float(h)
                i = float(i)
                Tf.custom3D(points,a,b,c,d,e,f,g,h,i)

        elif trtype=="multiple":
            n = int(params)
            cmdlist = []
            for i in range(n):          #Put all command in list
                cmd = input("... ")
                cmdlist.append(cmd)
            for cmddo in cmdlist:       #Run all command from list
                animator(cmddo)
                time.sleep(0.5)
        else:
            for i in range(frames):                 #Animate by splitting single transformation into <frames> transformation
                if trtype=="translate":
                    deltas = params.split(" ")
                    dx = float(deltas[0])/frames
                    dy = float(deltas[1])/frames
                    if mode=='3':
                        dz = float(deltas[2])/frames
                        Tf.translate(points,dx,dy,dz)
                    elif mode=='2':
                        Tf.translate(points,dx,dy)

                elif trtype=="dilate":
                    dparams = pow(float(params),1/frames)
                    Tf.dilate(points,dparams)

                elif trtype=="rotate":
                    if mode=='2':
                        deg,a,b = params.split(" ")
                        ddeg = float(deg)/frames
                        a = float(a)
                        b = float(b)
                        Tf.rotate(points,ddeg,a,b)
                    elif mode=='3':
                        deg,a,b,c = params.split(" ")
                        ddeg = float(deg)/frames
                        a = float(a)
                        b = float(b)
                        c = float(c)
                        Tf.rotate3D(points,ddeg,a,b,c)

                elif trtype=="shear":
                    sb = params.split(" ")[0]
                    k = params.split(" ")[1]
                    k = float(k)/frames
                    if mode=='3':
                        try:
                            k2 = float(params.split(" ")[2])/frames
                            Tf.shear(points,sb,k,k2)
                        except:
                            Tf.shear(points,sb,k)
                    elif mode=='2':
                        Tf.shear(points,sb,k)

                elif trtype=="stretch":
                    sb,k = params.split(" ")
                    k = pow(abs(float(k)),1/frames)*(float(k)/abs(float(k)))
                    Tf.stretch(points,sb,k)

                time.sleep(0.01)                #Frame-to-frame delay time
                draw()                          #Redraw canvas
    except:
        print("Unknown command. Type '?' or 'help' for help")


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the screen
    glLoadIdentity()                                   # Reset position
    if mode=='2':                                      # 2D Mode
        glOrtho(-500,500,-500,500,0,1)
        draw_axis()
        glColor3f(rgb[0], rgb[1], rgb[2])
        draw_poly()
    elif mode=='3':                                    # 3D Mode, hardcoded shape
        glOrtho(-500,500,-500,500,-1000,1000)
        gluLookAt(0, 0, 0, -45.0, -75.0, -100.0, 0.0,1.0,0.0)
        draw_axis3()
        draw_cube()
    glutSwapBuffers()
