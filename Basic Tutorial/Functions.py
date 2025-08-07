# ✅ Lesson 7: Functions
# 🧠 What You’ll Learn
# How to create reusable blocks of code
# How to pass data to functions using parameters

#Initialize function
def greet(name):
    print("Hello, ",name)
    
# Call the function
greet("Kuldeep")
greet("Vaidehi")

print("++++++++++++++++++++++")

def sum(a,b):
    print("Sum of a and b is ",(a+b))
    
sum(11,9)

print("++++++++++++++++++++++")

#With Return function

def multiply(a,b):
    return a*b

print("Multiply of 3 and 6 is ",multiply(3,6))