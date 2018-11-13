def translate(dx,dy,points) :
    for P in points :
        P[0] += dx
        P[1] += dy

def shear(param,k,points) :
    if (param == 'x') :
        for P in points :
            P[1] += k*P[0]
    elif (param == 'y') :
        for P in points :
            P[0] +=  k*P[1]

def stretch(param,k,points) :
    if (param == 'x') :
        for P in points :
            points[1] = k*points[1]
