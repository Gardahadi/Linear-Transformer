import math

def translate(dx,dy,points) :
    for P in points :
        P[0] += dx
        P[1] += dy

def shear(sb,k,points) :
    if (sb == 'x') :
        for P in points :
            points[1] += k*points[0]
    elif (param == 'y') :
            P[0] += k*P[1]
    elif (sb == 'y') :
        for P in points :
            P[1] +=  k*P[0]

def stretch(sb,k,points) :
    if (sb == 'x') :
        for P in points :
            points[1] = k*points[1]

def dilate(k,points) :
    for P in points :
        P[0] *= k
        P[1] *= k

def rotate(deg,a,b,points) :
    rad = float(deg*0.0174533)
    for P in points :
        temp0 = P[0]
        temp1 = P[1]
        P[0] = math.cos(rad)*(temp0-a) - math.sin(rad)*(temp1-b) + a
        P[1] = math.sin(rad)*(temp0-a) + math.cos(rad)*(temp1-b) + b

def reflect(param,points) :
    if param=="x":
        for P in points :
            temp = P[1]
            P[1] = -temp
    elif param=="y":
        for P in points :
            temp = P[0]
            P[0] = -temp
    elif param=="x=y" or param=="y=x":
        for P in points :
            temp = P[0]
            P[0] = P[1]
            P[1] = temp
    elif param=="y=-x" or param=="-y=x" or param=="x=-y" or param=="-x=y":
        for P in points :
            temp = P[0]
            P[0] = -P[1]
            P[1] = -temp
    else:
        a,b = param[1:][:-1].split(",")
        a = float(a)
        b = float(b)
        for P in points :
            temp0 = P[0]
            temp1 = P[1]
            P[0] = 2*a - temp0
            P[1] = 2*b - temp1

def custom(a,b,c,d,points) :
    for P in points :
        X = P[0]
        Y = P[1]
        P[0] = X*a + Y*b
        P[1] = X*c + Y*d
