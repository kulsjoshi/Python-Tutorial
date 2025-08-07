# ✅ 2. with Statement (Context Managers)
# Purpose:
# Safely manage resources like files without manually closing them.

with open("with_test_file.txt","w") as file:
    file.write("This is file with operator")
    
with open("with_test_file.txt","r") as file:
    print(f"CONTENT:\n{file.read()}")