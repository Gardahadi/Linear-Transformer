import math
import quaternion as q

def translate(points,dx,dy,dz=None) :
    for P in points :
        P[0] += dx
        P[1] += dy
        if dz!=None:
            P[2] += dz

def shear(points,sb,k,k2=None) :
    if (sb == 'x') :
        for P in points :
            P[0] += k*P[1]
            if len(P) == 3:
                P[0] += k*P[2]
    elif (sb == 'y') :
        for P in points :
            P[1] +=  k*P[0]
            if len(P) == 3:
                P[1] += k*P[2]
    elif (len(points[0]) == 3):
        if k2==None:
            k2 = k
        if (sb == 'z') :
            for P in points :
                P[2] +=  k*P[0] + k*P[1]
        elif (sb == 'xy') :
            for P in points :
                P[0] += k*P[2]
                P[1] += k2*P[2]
        elif (sb == 'xz') :
            for P in points :
                P[0] += k*P[1]
                P[2] += k2*P[1]
        elif (sb == 'yz') :
            for P in points :
                P[1] += k*P[0]
                P[2] += k2*P[0]

def stretch(points,sb,k) :
    if (sb == 'x') :
        for P in points :
            P[0] *= k
    elif (sb == 'y') :
        for P in points :
            P[1] *= k
    elif (sb == 'z') :
        for P in points :
            P[2] *= k

def dilate(points,k) :
    for P in points :
        P[0] *= k
        P[1] *= k
        if len(P)==3:
            P[2] *= k

def rotate(points,deg,a,b) :
    rad = float(deg*0.0174533)
    for P in points :
        temp0 = P[0]
        temp1 = P[1]
        P[0] = math.cos(rad)*(temp0-a) - math.sin(rad)*(temp1-b) + a
        P[1] = math.sin(rad)*(temp0-a) + math.cos(rad)*(temp1-b) + b

def reflect(points,param) :
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

def custom(points,a,b,c,d) :
    for P in points :
        X = P[0]
        Y = P[1]
        P[0] = X*a + Y*b
        P[1] = X*c + Y*d


def rotate3D(points,deg,a,b,c) :
    #Make a,b,c as unit vector
    a = a/(a**2+b**2+c**2)**(1/2)
    b = b/(a**2+b**2+c**2)**(1/2)
    c = c/(a**2+b**2+c**2)**(1/2)
    Q = [math.sin(math.radians(deg/2))*a, math.sin(math.radians(deg/2))*b, math.sin(math.radians(deg/2))*c,math.cos(math.radians(deg/2))]
    InverseQ = [-math.sin(math.radians(deg/2))*a, -math.sin(math.radians(deg/2))*b, -math.sin(math.radians(deg/2))*c,math.cos(math.radians(deg/2))]
    for P in points :
        # p' = q * p * q-1
        P.append(0)
        X = q.productQ(q.productQ(Q,P),InverseQ)
        P[0] = X[0]
        P[1] = X[1]
        P[2] = X[2]

def custom3D(points,params) :
    for P in points :
        X = P[0]
        Y = P[1]
        Z = P[2]
        P[0] = X*float(params[0]) + Y*float(params[1]) + Z*float(params[2]) + float(params[3])
        P[1] = X*float(params[4]) + Y*float(params[5]) + Z*float(params[6]) + float(params[7])
        P[2] = X*float(params[8]) + Y*float(params[9]) + Z*float(params[10]) + float(params[11])

def reflect3D(points,param) :
    if param=="xy" :
        for P in points:
            temp = P[2]
            P[2] = -temp
    elif param=="yz" :
        for P in points:
            temp = P[0]
            P[0] = -temp
    elif param=="xz" :
        for P in points:
            temp = P[1]
            P[1] = -temp
    else:
        a,b,c = param[1:][:-1].split(",")
        a = float(a)
        b = float(b)
        c = float(c)
        for P in points :
            temp1 = P[0]
            temp2 = P[1]
            temp3 = P[2]
            P[0] = 2*a - temp1
            P[1] = 2*b - temp2
            P[2] = 2*c - temp3
