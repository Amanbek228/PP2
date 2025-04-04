#1
import os

def list_contents(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All:", os.listdir(path))

path = "."  
list_contents(path)

#2
import os

def check_path_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = "test.txt"  
check_path_access(path)

#3
import os

def check_path(path):
    if os.path.exists(path):
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

path = "example/test.txt" 
check_path(path)

#4
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

filename = "example.txt"  
print("Number of lines:", count_lines(filename))

#5
def write_list_to_file(filename, lst):
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(f"{item}\n" for item in lst)

lst = ["apple", "banana", "cherry"]
filename = "output.txt"  # Укажите имя файла
write_list_to_file(filename, lst)

#6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w", encoding="utf-8") as f:
        f.write(f"File {letter}.txt")

#7
def copy_file(src, dst):
    with open(src, 'r', encoding='utf-8') as f1, open(dst, 'w', encoding='utf-8') as f2:
        f2.write(f1.read())

copy_file("source.txt", "destination.txt")

#8
import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or cannot be deleted.")

delete_file("test.txt")  