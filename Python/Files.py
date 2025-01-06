ruta = "C:\_Personal\data.txt"

'''Reading Files'''
file = open(ruta, "r")
content = file.read()
print(content)
file.close()

'''Writing Files'''
file = open(ruta, "w")
file.write("Hello, world!")
file.close()

'''In this case, the file is opened using the with 
statement and is automatically closed once the with 
block is exited, even if an exception occurs.'''
with open(ruta, "r") as file:
    content = file.read()
    print(content)