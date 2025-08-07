# Convert list of strings to lowercase
names = ["Kuldeep","NEIL","naitik","JaYMiN","SHReyash"]
lowerCase = [ name.lower() for name in names]
print(f"Names in lower case: {lowerCase}")

# Flatten a 2D list
matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
print(f"flatten data: {flat}")

# Create a dictionary of word lenghts
words = ["apple","banana","ice","airplane","lockhead martin"]
wordCount = {word: len(word) for word in words}
print(f"word count: {wordCount}")