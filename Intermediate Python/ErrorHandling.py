# Lesson 1 — Error Handling & Logging (deep dive)
# 
# 
# 1) try / except / else / finally
# try = run code that may fail
# except = handle specific errors (always prefer specific exceptions)
# else = runs if no exception raised
# finally = always runs, typically for cleanup

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("You can not divide the value by zero!!")
    except TypeError:
        print("Both values must be numbers")
    else:
        print(f"result: {result}")
    finally:
        print("Done...")

# calling a method        
divide(10,0)

# Don’t use bare except:
# try:
#    ...
# except:
#     pass
# This hides bugs. Prefer catching Exception or specific exceptions and either handle or re-raise.

print("+++++++++++++++++++++++++")

# Raising and chaining exceptions
# You can raise your own exceptions and chain them:
class MyAppError(Exception):
    pass

try:
    int(1)
except ValueError as e:
    raise MyAppError("faild to parse int") from e
    
print("+++++++++++++++++++++++++")

