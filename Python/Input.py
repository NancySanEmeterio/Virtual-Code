name = input("Enter your name: ")
age = input("Enter your age: ")


print("Hello, " + name + "!")
print("You are " + age + " years old.")

'''The input() function always returns a string. If you 
want to work with other data types, such as integers or 
floats, you must perform an explicit conversion using 
functions like int() or float().'''

age = int(input("Enter your age: "))


if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")