# ✅ PART 2: Nested Loops in List Comprehensions

pairs = [(x,y)for x in [1,2] for y in ['a','b']]
print(f"Nested loop pairs: {pairs}")

#Above code is equivalent to 
result = []
for x in [1,2]:
    for y in ['a','b']:
        result.append((x,y))
print(f"Nested loop pairs with large code: {result}")