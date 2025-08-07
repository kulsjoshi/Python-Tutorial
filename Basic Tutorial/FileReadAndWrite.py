# ✅ File Reading & Writing
# 🧠 What You’ll Learn
# How to read from and write to files
# File modes: "r" (read), "w" (write), "a" (append), "r+" (read + write)

# writing a file as using "w"(write)
with open("test_notes.txt","w") as file:
    file.write("This is my first ever file!\n")
    file.write("I am currently learning Python and it is fun")

# appending a file
with open("test_notes.txt","a") as file:
    file.write("\nAppending a new line")
    
# reading a file as using "r"(read)
with open("test_notes.txt","r") as file:
    content = file.read()
    print(content)
    
# reading and wriitng a file using "r+" (read and write)
with open("test_notes.txt","r+") as file:
    file.write("\nTrying read and write together")
    print(file.read())
    
