#Create three (3) legal variables. You may put "This is Legal" as your data.
v1 = "age"
print (v1)
v2 = "DaTe"
print (v2)
v3 = "nAME"
print (v3)

#Create three (3) multi-word variables that follows different variable cases. Put the name of the case as your data.
print("This is Camel Case")
print("this_is_snake_case")
print("ThisIsPascalCase")

#Create four (4) variables and store data with different data types (str, int, float, bool).
print(str("wowww"))
v6 = int(42)
print(v6)
v7 = float(3.14)
print(v7)
print(bool(True))

#Create three (3) variables that converts data type. Use casting to do this.
print(str(v6))
print(int(v7))
print(float(v6))

#Manipulate the string of two (2) variables by changing their case. Use lower() and upper() method.
print(v1.upper())
print(v2.lower())

#Perform four (4) arithmetic operations.
print(v6 + v7)
print(v6 - v7)
print(v6 * v7)
print(v6 / v7)

#Perform four (4) assignment operations.
v8 = v6 + v7
print(v8)
v9 = v6 - v7
print(v9)
v10 = v6 * v7
print(v10)
v11 = v6 / v7
print(v11)

#Perform four (4) comparison operations.
print(v6 == v7)
print(v6 != v7)
print(v6 > v7)
print(v6 < v7)

#Perform four (4) logical operations.
print(v6 > v7 and v6 < v7)
print(v6 > v7 or v6 < v7)
print(not(v6 > v7))
print(not(v6 < v7))

#Create four (4) variables with different data structures. 
list1 = ["apple", "banana", "cherry"]
tuple1 = ("apple", "banana", "cherry")
set1 = {"apple", "banana", "cherry"}
dict1 = {"name": "John", "age": 36}