import sys

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")
print(f"Path: {sys.path}")

# sys has a list which name argv it contains the data whch passed from command line to python script. It is a list which contains the command line arguments passed to the script.

print(f"Command line arguments: {sys.argv}")

for arg in sys.argv:
    print(arg) # it prints all the command line arguments passed to the script