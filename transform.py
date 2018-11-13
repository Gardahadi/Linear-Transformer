def translate(dx,dy,points) :
    for P in points :
        P[0] += dx
        P[1] += dy

def shear(sb,k,points) :
    if (sb == 'x') :
        for P in points :
            P[0] += k*P[1]
    elif (sb == 'y') :
        for P in points :
            P[1] +=  k*P[0]

def stretch(sb,k,points) :
    if (sb == 'x') :
        for P in points :
            P[0] = k*P[0]
    elif (sb == 'y') :
        for P in points :
            P[1] = k*P[1]

def custom (a,b,c,d,points) :

    for P in points :
        X = P[0]
        Y = P[1]
        P[0] = X*a + Y*b
        P[1] = X*c + Y*d
