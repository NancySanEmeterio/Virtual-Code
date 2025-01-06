
#Lists
#--------------------------------------
fruits = ["apple", "banana", "orange"]

print(fruits[0])  # Prints "apple"
print(fruits[1])  # Prints "banana"
print(fruits[2])  # Prints "orange"

print(fruits[-1])  # Prints "orange"
print(fruits[-2])  # Prints "banana"
print(fruits[-3])  # Prints "apple"

#append(element): adds an element to the end of the list.
fruits.append("pear")
print(fruits)  # Prints ["apple", "banana", "orange", "pear"]

#insert(index, element): inserts an element at a specific position in the list.
fruits.insert(1, "grape")
print(fruits)  # Prints ["apple", "grape", "banana", "orange", "pear"]

#remove(element): removes the first occurrence of an element in the list.
fruits.remove("banana")
print(fruits)  # Prints ["apple", "grape", "orange", "pear"]

#pop(index): removes and returns the element at a specific position in the list.
removed_fruit = fruits.pop(2)
print(fruits)  # Prints ["apple", "grape", "pear"]
print(removed_fruit)  # Prints "orange"

#sort(): sorts the elements of the list in ascending order.
fruits.sort()
print(fruits)  # Prints ["apple", "pear", "grape"]

#reverse(): reverses the order of the elements in the list.
fruits.reverse()
print(fruits)  # Prints ["grape", "pear", "apple"]


numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers if x % 2 == 0] #x ** 3 = 3x3
print(squares)  # Prints [4, 16] x % 2 se trae multiplos de dos 


#Tuples
#--------------------------------------
# La tupla es con () y el arreglo con [])
# La tupla solo se declara una vez y ya no se pueden alterar el tamaño
point = (3, 4)
print(point[0])  # Prints 3


my_tuple = (1, 2, 3, 2, 4, 2) 
print (my_tuple.index(2))   # Output: 1 
print (my_tuple.index(2, 2))   #Output: 3 
print (my_tuple.index(2, 2, 4))   #Output: 3
 

#Dictionaries
#--------------------------------------
person = {"name": "Juan", "age": 25, "city": "Madrid"}
print(person["name"])  # Prints "Juan"
print(person["age"])   # Prints 25
print(person["city"])  # Prints "Madrid"

#keys(): returns a view of all the keys in the dictionary.
print(person.keys())    # Prints dict_keys(["name", "age", "city"])

#values(): returns a view of all the values in the dictionary.
print(person.values())  # Prints dict_values(["Juan", 25, "Madrid"])

#items(): returns a view of all the key-value pairs in the dictionary.
print(person.items())   # Prints dict_items([("name", "Juan"), ("age", 25), ("city", "Madrid")])

#update(another_dictionary): updates the dictionary with the key-value pairs from another dictionary.
person.update({"profession": "Engineer"})
print(person)  # Prints {"name": "Juan", "age": 25, "city": "Madrid", "profession": "Engineer"}



