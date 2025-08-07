# ✅ PART 1: List Comprehensions – The Basics
# 🔹 Basic Format:

### new_list = ['expression' for 'item' in 'iterable']

# Initialze iterable
numbers = [1,2,3,4,5,6]
print(f"Listed numbers are: {numbers}")

#📘 Example: Square numbers
squares = [ numb*numb for numb in numbers]
print(f"Squares are: {squares}")

# with IF condition to find even number
evens = [numb for numb in numbers if numb%2==0]
print(f"Even numbers are: {evens}")

# with IF-ELSE condition to print odd and even using (ternary inside expression)
labels = ['even' if numb%2==0 else 'odd' for numb in numbers]
print(f"Labels are: {labels}")