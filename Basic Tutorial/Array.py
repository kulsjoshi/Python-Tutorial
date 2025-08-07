# ✅ Lesson 6: Lists
# 🧠 What You’ll Learn
# How to store multiple values in one variable
# Access, update, and loop through a list

fruits = ["apple","banana","cherry"]

#Access items
print(fruits[0]) #apple

# Add item
fruits.append("orange")

# Change item
fruits[1]="mango"

for fruitItem in fruits:
    print(fruitItem)
    
print("================")

#My take
cities = ["Gilbert","Tempe","Phoenix","Scottsdale"]

print(cities[0]) #Gilbert

#Change city
cities[1] = "Mesa"

for cityName in cities:
    print(cityName)