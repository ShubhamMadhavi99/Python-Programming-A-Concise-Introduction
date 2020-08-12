
def problem2_7():
    a = float(input("Enter length of side one: "))
    b = float(input("Enter length of side two: "))
    c = float(input("Enter length of side three: "))
    s = 0.5 *(a+b+c)
    z = s*(s-a)*(s-b)*(s-c)
    area = z**(1/2)
    print("Area of a triangle with sides " + str(a) + " " + str(b) + " " +str(c) + " " + "is " + str(area))
    


#x = problem2_7(a,b,c)