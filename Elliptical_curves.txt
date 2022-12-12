# -*- coding: utf-8 -*-

#Adding points to a curve when not in field of Fp
def EllipticCurvePointAdditionReal(a_1, a_2, a_3, a_4, a_6, p, q):
    x_1 = p[0]
    x_2 = q[0]
    y_1 = p[1]
    y_2 = q[1]

    if x_1 == x_2:
        #Slope of the Tangent line using implicit differentiation method
        l = (3*x_1**2 + 2*a_2*x_1 + a_4 - a_1*y_1)/(2*y_1 + a_1*x_1 + a_3)
        v = (-x_1**3 + a_4*x_1 + 2*a_6 - a_3*y_1)/(2*y_1 + a_1*x_1 + a_3)
        #print(l)
    elif ((x_1 == x_2) and ((y_1 + y_2 + a_1*x_2 + a_3) == 0)):
        return None
        #print("p + q = O")
    else:
        l = (y_2 - y_1)/(x_2 - x_1)             #Lambda
        v = (y_1*x_2 - y_2*x_1)/(x_2 - x_1)     #V
        
    #Calculate new point (p+q)
    x_3 = l**2 - a_1*l - a_2 - x_1 - x_2
    y_3 = -(l + a_1)*(x_3) -v -a_3
    return [x_3, y_3]
    print("New real point (p+q):", [x_3, y_3])
    
    """
    #Calculate new point (-p)
    p_neg = [x_1, (-y_1 - a_1*x_1 - a_3)]
    print("-p:", p_neg)
    """
#Adding points on elliptic curve when field Fp
def EllipticCurvePointAdditionMod(a_4, a_6, p, q, n):
    #Importing points to variables
    x_1 = p[0]
    x_2 = q[0]
    y_1 = p[1]
    y_2 = q[1]

    if equalModn(x_1, x_2, n) and equalModn(y_1, y_2, n):
        #Dividing by 2*y is the same as multiplying with inverse mod of (2y)
        l = reduceModn((3*x_1**2 + a_4, n) * inverseModn(2 * y_1, n)) #lambda
    else:
        l = reduceModn(((y_1 - y_2) * inverseModn(x_1 - x_2, n)), n)


    v = reduceModn(y_1 - l*x_1, n)  
    x_3 = reduceModn(l**2 - x_1 - x_2, n)
    y_3 = reduceModn(-l*x_3 - v, n)
    return (x_3, y_3) #new point

#Find all points on the curve within the field
def findPoints(n, a_4, a_6):
    points =[]
    for x in range(n):
        for y in range(n):
            if equalModn(x**3 + a_4*x + a_6, y**2, n):
                points.append((x, y))
    return points
    print(points)

#Reduce an integer mod n
def reduceModn(x, n):
    return x % n

#If two integers are equal mod n
def equalModn(x, y, n):
    return reduceModn(x - y, n) == 0

#Find discriminant, if return is non-zero it is an elliptical curve
def Discriminant(a_4, a_6, n):
    D = -16*(4 * a_4**3 + 27*a_6**2)
    return reduceModn(D, n)

#Find multiplicative inverse of mod n
def inverseModn(x, n):
    for y in range(n):
        if equalModn(x*y, 1, n):
            return y
            #break
    return None


"""
#Find points (not for mod)
def find_y_mod_p(a_1, a_2, a_3, a_4, a_6, x, n):
    mod = (x**3 + a_6*x + a_6) % n
    print("y^2: ", mod)
"""

#Driver code

#Remember: y^2 + a_1*xy + a_3*y = x^3 + a_2*x^2 + a_4*x + a_6 = 0
#Elliptic curve: "y^2 = x^3 - 3x + 1"
a_1 = 0
a_2 = 0
a_3 = 0
a_4 = -3
a_6 = 1
"""
p=[1,1]
q=[1,1]
"""
n = 97          #This shall be large prime
x = 0

points = findPoints(n, a_4, a_6)            #Finding all the integer points on the curve.
print(points)                               
print("number of points:", len(points))     #Total number of points
print("Discriminant:", Discriminant(a_4, a_6, n))   #Disciriminant
print("New points(x,y):",EllipticCurvePointAdditionMod(a_4, a_6, points[2], points[5], n)) #New point after addition