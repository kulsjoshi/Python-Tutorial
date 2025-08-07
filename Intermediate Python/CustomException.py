# Custom exceptions
# Make domain-specific exceptions so calling code can handle them cleanly
class DivisionError(Exception):
    pass

def safe_divide(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        raise DivisionError("custom error and division by zero not allowed") from e
    
print(safe_divide(9,0))