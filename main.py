
# variables till "o" are occupied
def distance():
    a = input("Input the number for x1: ")
    b = input("Input the number for y1: ")
    c = input("Input the number for x2: ")
    d = input("Input the number for y2: ")
    
    distance = ((float(c) - float(a)) ** 2 + (float(d) - float(b)) ** 2) ** 0.5
    print(distance)


def midpoint():
    e = input("Input the number for x1: ")
    f = input("Input the number for y1: ")
    g = input("Input the number for x2: ")
    h = input("Input the number for y2: ")
    
    midpointX = ((float(e) + float(g)) / 2)
    midpointY = ((float(f) + float(h)) / 2)
    
    print("(" + str(midpointX) + "," + str(midpointY) + ")")


def numroot():
    j = float(input("Input the value of a (the coefficient of x square): "))
    i = float(input("Input the value of b (the coefficient of x): "))
    k = float(input("Input the value c (the constant): "))
    l = i ** 2 - (4 * j * k)
    if l < 0:
        print("This equation has no real roots.")
    elif l > 0:
        print("This equation has 2 distinct real roots.")
    elif l == 0:
        print("This equation has 2 equal roots.")


def quadratic():
    n = float(input("Input value of a (the coefficient of x square): "))
    m = float(input("Input the value of b (the coefficient of x): "))
    o = float(input("Input value of c (the constant): "))
   
    root1 = (-(m) + ((m) ** 2 - (4 * n * o)) ** 0.5) / (2 * n)
    root2 = (-(m) - ((m) ** 2 - (4 * n * o)) ** 0.5) / (2 * n)
    
    print("x=" + str(root1) + " or, x=" + str(root2))

def addition() :
    num1 = input("Enter a number")
    num2 = input ("Enter a number to add")
    ans_add = float(num1) + float(num2)
    
    print(ans_add)

def subtraction() :
    num3 = input("Enter a number")
    num4 = input ( "Enter another numbe to subtract")
    ans_subtract = float(num3) - float(num4)
    
    print(ans_subtract)

def multiplication ():
    num5 = input("Enter a number")
    num6 = input("Enter another number to multiply")
    ans_multiply = float(num5) *float(num6)
    
    print(ans_multiply)

def division ():
    num7 = input("Enter a number")
    num8 = input("Enter another number to divide")
    ans_divide = float(num7) / float(num8)
    
    print(ans_divide)

def exponents () :
    num9 = input("Enter a number")
    num10 = input("Enter another number as the exponentyesadd")
    ans_expo = float(num9) ** float(num10)
   
    print(ans_expo)


Question = input(
    "Which operation would you like to perform? Distance, Midpoint,Solve a quadratic equation(quadratic), find the number of roots(numroot) or do simple calculations like addition, subtraction, division, multiplication or find powers ? ")

Question = Question.lower()

if Question == "distance":
    distance()


elif Question == "midpoint":
    midpoint()


elif Question == "numroot":
    numroot()


elif Question == "quadratic":
    quadratic()

elif Question == "addition":
    addition()

elif Question == "subtraction":
    subtraction()

elif Question == "division":
    division()

elif Question == "multiplication":
    multiplication()

elif Question == "exponent":
    exponents()

else:
    print("That is not an operation")

input("the program will end once input is received")
print("See ya!")
