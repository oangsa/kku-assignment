#Name : 66_สุธางค์_สุขเรืองกูล_นครราชสีมา

'''
Class
'''
class circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circle_area(self):
        cal = float((22/7)*(self.radius**2))
        print("Area of Circle:", ("%.2f" % cal))
        
class rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    
    def rec_area(self):
        cal = float(self.width * self.height)
        print("Area of Rectangle:", ("%.2f" % cal))
        
    
class triangle:
    def __init__ (self, base, height) :
        self.base = base
        self.height = height
        
    def tri_area(self):
        cal = float(0.5 * self.base * self.height)
        print("Area of Triagle:", ("%.2f" % cal))
        
class trapezoid:
    def __init__ (self, b1, b2, height):
        self.m = b1
        self.n = b2
        self.h = height
        
    def trapezoid_area(self):
        cal = float(0.5*(self.m + self.n) * self.h)
        print("Area of Trapezoid:", ("%.2f" % cal))

class ellipse:
    def __init__ (self, width, length):
        self.w = width
        self.l = length
        
    def ellipse_area(self):
        cal = float((22/7)* self.w * self.l)
        print("Area of Ellipse:", ("%.2f" % cal))

'''       
While Loop Condition.
'''
        
while True:
    print("******** Area Calculator *******")
    print("**     (1)Circle Area         **")
    print("**     (2)Rectangle Area      **")
    print("**     (3)Triangle Area       **")
    print("**     (4)Trapezoid Area      **")
    print("**     (5)Ellipse Area        **")
    print("**     (6)EXIT                **")
    print("********************************")
    select = input("Select: ")
    
    if select == "1":
        r = float(input("Enter the Radius(r) of Circle: "))
        area = circle(r)
        area.circle_area()
    elif select == "2":
        w = float(input("Enter the Width(w) of Rectangle: "))
        h = float(input("Enter the Height(h) of Rectangle: "))
        area = rectangle(w, h)
        area.rec_area()
    elif select == "3":
        b = float(input("Enter the Base(b) of Triangle: "))
        h = float(input("Enter the Height(h) of Triangle: "))
        area = triangle(b, h)
        area.tri_area()
    elif select == "4":
        b1 = float(input("Enter the 1st Base(b1) of Trapezoid: "))
        b2 = float(input("Enter the 2st Base(b2) of Trapezoid: "))
        h = float(input("Enter the Height of Trapezoid: "))
        area = trapezoid(b1, b2, h)
        area.trapezoid_area()
    elif select == "5":
        a = float(input("Enter the Width(w) of Ellipse: "))
        b = float(input("Enter the Length(l) of Ellipse: "))
        area = ellipse(a, b)
        area.ellipse_area()
    elif select == "6":
        print("Exit...")
        exit()
    
    input("Press Enter to return...")