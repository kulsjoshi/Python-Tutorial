from joke_fetcher import get_random_joke
import os

file_name = "jokes_directory.txt"

if __name__ == "__main__":
    print("Fetching a random joke...")
    
    random_joke = get_random_joke()
    print(random_joke)
    
    # If txt file is not created then it will create one
    if not os.path.exists(file_name):
        with open(file_name,"w") as file:
            file.write("====== Random Jokes Dictionary ======")
        
    # Append jokes in the exisitng file        
    with open(file_name,"a") as f:
        f.write(f"\n> {random_joke}")