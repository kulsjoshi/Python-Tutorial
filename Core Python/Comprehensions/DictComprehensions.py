# ✅ PART 3: Dict Comprehensions

# 🔹 Basic Format:
# new_dict = {key_expr: value_expr for item in iterable}

numbers = [1,2,3,4,5,6,7,8,9]
squares = { numb : numb*numb for numb in numbers}
print(f"Dict Comprehension result:\nSquares: {squares}")

# Filtered Dict
grades = {"Kuldeep":99,"Jaymin":98,"Neil":97,"Shreyas":97}
passed = { k: value for k, value in grades.items() if value > 97}
print(f"Passed students are: {passed}")