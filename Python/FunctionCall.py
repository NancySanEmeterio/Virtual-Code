#Definition and Function Call
def greeting():
    print("Hello, world!")  
greeting()  # Prints "Hello, world!"

def greeting(name):
    print(f"Hello, {name}!")
greeting("John")  # Prints "Hello, John!"


def suma(a, b):
    return a + b 
result = suma(3, 4) * suma(1, 1)
print(result)  # Prints 14


"""
Anonymous Functions (lambda)
Python allows the creation of anonymous functions or 
lambda functions, which are unnamed functions defined in a single line. 
They are commonly used for small and concise functions.
"""
square = lambda x:  x + 1
print(square(3 ))  # Prints 5


''' cuando pones un * en los parametros
significa que puedes mandar n  cantidad de parametros y
tomaran el valor de la variable , en este caso mandas
10,20 y 30 como valor de numeros'''
def calcular_media(*numeros):
        suma = sum(numeros)
        cantidad = len(numeros)
        media = suma / cantidad
        return media
print("Media: " , calcular_media(10,20,30,40))