import os

# file creation
filename = "Kerwin Concepcion.txt"
with open(filename, "w") as file:
    file.write("Hello! World. I am Kerwin Concepcion from 12-Q.\n")
    file.write("I am a person with a dream that one day I'll be a hotdog in a freezer.\n") 

 

# file overwrite
with open(filename, "w") as file:
    file.write("Hello! Jupyter. This is my alter ego, anita max wynn.\n")

 

# file read
with open(filename, "r") as file:
    content = file.read()
    print(content)

 

#file deletion
os.remove(filename)