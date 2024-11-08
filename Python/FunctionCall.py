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


square = lambda x:  x + 1
print(square(3 ))  # Prints 5