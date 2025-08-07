# 🧠 What You’ll Learn
# How to use dict to store key–value pairs
# How to use set to store unique values

#📘 Dictionaries (dict)
person = {
    "name":"Kuldeep",
    "age": 100,
    "city":"Los Angeles"
}

#Accessing value
print(person["name"])

person["age"] = 50
person["email"] = "kuldeep@xyz.com"

for key, value in person.items():
    print((key), " is ", (value))
    
#📗 Sets (set)
unique_numbers = {1,3,5,7,9,5,3}
print("Unique numbers are: ",unique_numbers)

unique_numbers.add(4)
print("Unique numbers are: ",unique_numbers)
unique_numbers.discard(9)
print("Unique numbers are: ",unique_numbers)