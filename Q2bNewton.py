import math

def Newton(xn, yn):
    ja = 1/(math.pow((2-xn),2) * (2-yn))-1
    jb = 1/((2-xn) * math.pow((2-yn),2))
    jc = 4/(math.pow((3-2*xn),2) * (3-yn))
    jd = 2/((3-2*xn) * math.pow((3-yn),2))-1
    fx = 1/((2-xn) * (2-yn)) - xn
    fy = 2/((3-2*xn) * (3-yn)) - yn
    
    x1 = xn - (fx*jd - jb*fy)
    y1 = yn - (-fx*jc + ja*fy)
    return (x1,y1)

def FindRoot():
    #set x0 to 0
    xn = 0.8
    yn = 0.8
    x1, y1 = Newton(xn, yn)
    #Repeat Newton's method until the difference is less than 10^-10
    while(abs(x1 - xn) >= math.pow(10, -10) and abs(y1 - yn) >= math.pow(10, -10)):
        xn = x1
        yn = y1
        x1, y1 = Newton(xn, yn)
    return x1,y1

if __name__ == '__main__':
    #Print results
    x1,y1 = FindRoot()
    print("x1: " + str(x1) + " y1: " + str(y1))

#x1: 0.36675872534366316 y1: 0.3305662135399683