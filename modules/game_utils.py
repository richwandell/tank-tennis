import math

def addVectors((m1, a1), (m2, a2)):
    """Adds 2 vectors and returns the new vector"""
    x1 = m1 * math.cos(a1)
    y1 = m1 * math.sin(a1)
    
    x2 = m2 * math.cos(a2)
    y2 = m2 * math.sin(a2)
    
    x = x1+x2
    y = y1+y2
    
    ma = math.sqrt(x**2 + y**2)
    
    angle = math.atan2(y, x)
    
    return (ma, angle)

def cmpdst((x1, y1), (x2, y2)):
    """Returns the component distance for 2 points"""
    return math.sqrt(((x1-x2)**2) + ((y1-y2)**2))


    