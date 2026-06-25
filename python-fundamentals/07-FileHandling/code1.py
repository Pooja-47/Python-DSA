# ==========================
# File Handling in Python
# ==========================

"""
Till now, we have used variables to store data.

Variables provide temporary storage because they are stored in RAM.
When the program stops or the system is turned off, the stored data is lost.

For permanent storage, we use files.
"""

# Examples of files:
"""
notes.txt   -> Text File
program.py  -> Python File
video.mp4   -> Video File
song.mp3    -> Audio File
"""

# --------------------------
# File Modes
# --------------------------

"""
1. 'r' -> Read Mode
   - Used to read the contents of a file.
   - The file must already exist.
   - You cannot modify the file in this mode.

2. 'w' -> Write Mode
   - Used to write data into a file.
   - If the file exists, its previous content is overwritten.
   - If the file does not exist, a new file is created.

3. 'a' -> Append Mode
   - Used to add new content at the end of a file.
   - Existing content remains unchanged.
   - If the file does not exist, a new file is created.

4. 'x' -> Create Mode
   - Creates a new file and opens it for writing.
   - Raises an error if the file already exists.
"""

"""
A file can be created using the following modes:
'w', 'a', and 'x'
"""

# --------------------------
# open() Function
# --------------------------

"""
All file operations are performed using the open() function.

Syntax:
open("path_or_filename", "mode")

Example:
file = open("notes.txt", "r")

The open() function returns a file object,
which is used to perform operations on the file.
"""

# --------------------------
# Path and File Name
# --------------------------

"""
Every file and folder in a computer has a unique location called a path.

Example Path:
C:/Users/Username/Desktop/notes.txt
"""

"""
filename:

Used when the file is present in the current working directory.

If only the file name is provided, Python creates or searches
for the file in the current working directory.


Example:
open("notes.txt", "r")

path:
Used when the file is located in a different directory.

Example:
open("C:/Users/Username/Desktop/notes.txt", "r")
"""

r"""
Escape Sequences:-

Escape sequences are special character combinations that start
with a backslash (\) and perform a specific action.

Common escape sequences:

\n -> New Line
\t -> Tab Space
\\ -> Single Backslash
\" -> Double Quote
\' -> Single Quote
"""

# --------------------------
# Raw String
# --------------------------

r"""
In Windows file paths, backslashes (\) are very common.

Python may interpret some backslash combinations
such as \n and \t as escape sequences.

To prevent this, we use a raw string by placing 'r'
before the string.

Example:

r"C:\Users\Username\Desktop\notes.txt"

The 'r' tells Python to treat backslashes as normal
characters instead of escape sequences.

Note:
The 'r' before the path is different from the 'r'
used as the file mode in open().

open(r"C:\Users\Username\Desktop\notes.txt", "r")

First r  -> Raw String
Second r -> Read Mode
"""

# --------------------------
# CRUD Operations
# --------------------------

"""
Most file operations can be grouped into CRUD operations:

C -> Create   : Create a new file
R -> Read     : Read data from a file
U -> Update   : Modify existing file content
D -> Delete   : Remove a file
"""


# 1. Create a File using open()

"""
Syntax:
open("path_or_filename", "mode")

path:
Used when the file is located in a different directory.

filename:
Used when the file is created in the current working directory.
"""


# ==========================
# File Modes Implementation
# ==========================

# --------------------------
# 1. Create a File ('x' Mode)
# --------------------------

"""
'x' mode creates a new file.

- Creates the file if it does not exist.
- Raises FileExistsError if the file already exists.
"""

#open("hello.txt", "x")


"""
This creates a new file named 'hello.txt'.

Note:
The file is created in the current working directory (CWD),
not necessarily in the same folder as the Python file.

You can check the current working directory in the VS Code terminal:

pwd

You can change the directory using:

cd folder_name
"""

""" 
Important Fix:
- 'x' mode is less commonly used than 'w' mode.

- It is useful when we want to ensure that
an existing file is not overwritten accidentally.

- For this we can use with statement as:
"""
try:
    with open("hello.txt", "x"):
        print("File created successfully")
except FileExistsError:
    print("File already exists")



# --------------------------
# 2. Write to a File ('w' Mode)
# --------------------------

"""
'w' mode is used to write data into a file.

- Creates the file if it does not exist.
- Overwrites all existing content if the file already exists.
"""

file = open("Intro.txt", "w")

data = input("Enter your introduction: ")

file.write(data)

file.close()

print("Data written successfully!")


# --------------------------
# 3. Read a File ('r' Mode)
# --------------------------

"""
'r' mode is used to read file contents.

- The file must already exist.
- Raises FileNotFoundError if the file does not exist.
"""

file = open("Intro.txt", "r")

print("\nContent of Intro.txt:")
print(file.read())

file.close()


# --------------------------
# 4. Append to a File ('a' Mode)
# --------------------------

"""
'a' mode is used to add data at the end of a file.

- Existing content remains unchanged.
- Creates the file if it does not exist.
"""

file = open("Intro.txt", "a")
file.write("\nLearning Python File Handling")
file.close()

file = open("Intro.txt", "r")
print("\nIntro.txt after appending:")
print(file.read())
file.close()
print("New data appended successfully!")

# Performing CRUD operations using with keyword:
"""
-Always use the
with
statement — it automatically closes the file for you, even if an error occurs.
"""
# Syntax:
"""
with open("filename-or-path","mode") as f:
   block of code

- with : keyword
- f : variable name where the object of open function is stored.
- this uses indentation so when you are out of indentation it automatically closes the file.
"""
with open("Intro.txt","a") as f:
    f.write("\nLet's learn together with NYC.")

with open("Intro.txt","r") as f:
    print(f"\nAfter appending Intro.txt using with keyword:\n{f.read()}")

   