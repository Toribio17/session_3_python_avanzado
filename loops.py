#loops class and examples

import random 

class loop_cases():

    def __init__(self):
        print("my constructor")
    
    #while
    # NOTAR que el numero 3 se salta
    def example_one(self):
        i = 0
        while i < 6:
            i = i + 1
            if i == 4:
                continue
            print(i)
            print("hello")

    #Notar que se imprime el mensaje cuando la condicion es false
    def example_two(self):
        i = 1
        while i < 6:
            print(i)
            i += 1
        else:
            print("i is no longer less than 6", i)   

    #No hagas esto
    #bucles infinitos 
    def example_three_error(self):
        while True:
            print("Soy siempre verdadero")

    #Do While example
    #simulando comportamiento en C 
    def example_four_do(self):
        palabra_secreta = "python"
        counter = 0

        while True:
            palabra = input("Ingresa la palabra secreta: ").lower()
            counter = counter + 1
            if palabra == palabra_secreta:
                break
            if palabra != palabra_secreta and counter > 7: 
                break
    
    #imprimiendo un list
    def example_for_one(self):
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
         print(x) 

    #ejemplo for usando continue 
    def example_for_two(self):
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
            if x == "banana":
                continue
            print(x)

    #Ejemplo for con Break
    def example_for_three(self):
        for x in range(6):
            if x == 3: 
                print(x)
                break
            else:
                print("Finally finished!")

    #Ejemplo for anidando ejemplos
    def example_for_four(self):
        adj = ["red", "big", "tasty"]
        fruits = ["apple", "banana", "cherry"]

        for x in adj:
            for y in fruits:
                print(x, y)

    #usando range y un for 
    def example_for_five(self):
        list_1 = []
        #usnado un for y list
        for i in range(1, 11):
            list_1.append(i)
            print(i)
        
        #usando range y list
        list_1 = list(range(1, 11))


if __name__ == "__main__":
    obj = loop_cases()
    #obj.example_one()
    #obj.example_two()
    #obj.example_three_error()
    #obj.example_four_do()
    #obj.example_for_one()
    #obj.example_for_two()
    #obj.example_for_three()
    #obj.example_for_four()
    obj.example_for_five()
    

    