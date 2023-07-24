#if class and examples
# import the time module
import time

class if_statements():
    
    def __init__(self):
        print("My statements constructor")

    #if simple
    def statements_one(self):
        a = 33
        b = 200
        if b > a:
            print("b is greater than a")

    #if_elif
    def statements_two(self):
        a = 33
        b = 33
        if b > a:
            print("b is greater than a")
        elif a == b:
            print("a and b are equal")
    
    #if else ejemplo 
    def statements_three(self):
        a = 200
        b = 33
        if b > a:
            print("b is greater than a")
        else:
            print("b is not greater than a")


    #ejemplo con and (Y caso)
    def staments_four(self):
        a = 200
        b = 33
        c = 500
        if a > b and c > a:
            print("Both conditions are True")

    #ejemplo con or (ó caso)
    def statements_five(self):
        a = 200
        b = 33
        c = 500
        if a > b or a > c:
            print("At least one of the conditions is True")


    #ejemplo de NOT keyword; este oprador nos indica o ayuda a negar la condicion de nuestro IF  
    def statements_six(self):
        a = 33
        b = 200
        if not a > b:
            print("a is NOT greater than b")

    #if anidados ejemplo
    def statements_seven(self):
        x = 41
        if x > 10:
            print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

    #short way 
    def statements_shor_way_one(self,a,b):
        if a > b: print("a is greater than b")

    def statements_shor_way_two(self,a,b): 
        print("A") if a > b else print("B")
        # if a > b:
            #print(A)
        # else:
            # print("B")

    def statements_shor_way_three(self,a,b):
        print("A") if a > b else print("equals") if a == b else print("B")
        # if a > b : 
            # print("A")
        # elif a == b :
            # print("equals")
        # else: 
            # print("B")

    def statements_way_three(self,a,b):
        if a > b : 
            print("A")
        elif a == b :
            print("equals")
        else: 
            print("B")

    def compare_execution(self):
        # get the current time in seconds since the epoch
        proces_seconds = time.time()
        self.statements_shor_way_three(300,330)
        print("Seconds since process one =", proces_seconds)	
        self.statements_way_three(300,330)
        print("Seconds since process two =", proces_seconds)

if __name__ == "__main__":
    obj = if_statements()
    #obj.statements_one()
    #obj.statements_two()
    #obj.statements_three()
    #obj.staments_four()
    #obj.statements_five()
    #obj.statements_six()
    #obj.statements_seven()
    #obj.statements_shor_way_one(330,334)
    #obj.statements_shor_way_two(333,400)
    #obj.statements_shor_way_three(331,332)
    obj.compare_execution()

    
            

    

