with open("notes.txt", "w") as file:
    file.write("CiA\n")
    file.write("Ai Engineer\n")
    file.write("Solutions\n")

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("notes.txt", "a") as file:
    file.write("L2E\n")
    file.write("Cohort2\n")

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

try:
    with open("missing.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error file not found")

fav_items = ["No fav food", "No fav book", "Slow songs"]
with open("list.txt", "w") as file:
    for item in fav_items:
        file.write(item + "\n")

with open("list.txt", "r") as file:
    for line in file:
        print(line.strip())
