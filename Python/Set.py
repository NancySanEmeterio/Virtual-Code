#Sets
#--------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}


union = set1 | set2
print(union)  # Prints {1, 2, 3, 4, 5}


intersection = set1 & set2
print(intersection)  # Prints {3}


difference = set1 - set2
print(difference)  # Prints {1, 2}


symmetric_difference = set1 ^ set2
print(symmetric_difference)  # Prints {1, 2, 4, 5}


#Set methods
fruits = {"apple", "banana", "orange"}

#add(element): adds an element to the set.
fruits.add("pear")
print(fruits)  # Prints {"apple", "banana", "orange", "pear"}

#remove(element): removes an element from the set. If the element does not exist, it raises an error.
fruits.remove("banana")
print(fruits)  # Prints {"apple", "orange", "pear"}

#discard(element): removes an element from the set if present. If the element does not exist, it does nothing.
fruits.discard("grape")
print(fruits)  # Prints {"apple", "orange", "pear"}

#clear(): removes all elements from the set.
fruits.clear()
print(fruits)  # Prints set()