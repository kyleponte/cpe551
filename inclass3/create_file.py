"""
create_file.py
Creates a new text file and writes text within the file before closing it
Kyle Ponte
kponte@stevens.edu
9/24/25
"""

with open("myFile.txt", "w") as f:
    f.write("I love Python.\n") # writes text to line 1
    f.write("It is more user-friendly than other programming languages.")