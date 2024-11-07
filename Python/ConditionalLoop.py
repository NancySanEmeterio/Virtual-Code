## Conditional Structures 

##IF-ELSE 
age = 15
if age >= 18:
   print ("You are an adult.")

else:
   print ("You are a minor.")
   

##IF-ELIF-ELSE   
grade = 85


if grade >= 90:
   print ("Excellent")

elif grade >= 80:
   print ("Very good")

elif grade >= 70:
   print ("Good")

else:
   print ("Needs improvement")
   
"""
   For 
   for variable in sequence: 
    # Block of code to repeat
    instructions
"""
fruits = ["apple", "banana", "orange"] 
for fruit in fruits:
    print(fruit)
    
"""
    while condition:

    # Block of code to repeat
    instructions
"""
#BREAK
counter = 0 
while True:

    print(counter)
    counter += 1 
    
    if counter == 5:
        break

#CONTINUE
for i in range(10):

    if i % 2 == 0: #Multipros de 2
        continue
    print(i)