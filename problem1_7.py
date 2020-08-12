#PROBLEM STATEMENT 7
def problem1_7():
    base_1 = float(input("Enter the length of one of the bases: "))
    base_2 = float(input("Enter the length of the other base: "))
    height = float(input("Enter the height: "))
    area = ((base_1 + base_2)/2) * height
    print("The area of a trapezoid with bases " + str(base_1)+" and "+ str(base_2) +
          " and height "+str(height) + " is " + str(area))