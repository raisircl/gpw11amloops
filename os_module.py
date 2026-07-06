import os

#os.mkdir("docs") # it creates a docs folder inside current directory

os.chdir("docs") # it changes the current working directory to docs folder

print(f"Current working directory: {os.getcwd()}")
os.chdir("..") # it changes the current working directory to parent directory
print(f"Now you current directory: {os.getcwd()}")

print(os.listdir()) # it lists all the files and folders in the current working directory
for file in os.listdir():
    print(file) # it prints all the files and folders in the current working directory

os.rmdir("docs") # it removes the docs folder from the current working directory
