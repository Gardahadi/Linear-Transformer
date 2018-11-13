def translate(dx,dy,points) :
    for P in points :
        P[0] += dx
        P[1] += dy

def shear(param,k,points) :
    if (param == 'x') :
        for P in points :
            points[1] += k*points[0]
    else if (param == 'y') :
        for P in points :
            points[0] +=  k*points[1]

def stretch(param,k,points) :
    if (param == 'x') :
        for P in points :
            points[1] = k*points[1]
    else if (param)
