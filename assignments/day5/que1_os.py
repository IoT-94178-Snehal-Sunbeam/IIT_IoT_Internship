import os

folder="notes"
os.makedirs(folder, exist_ok=True)

file_path=os.path.join(folder, "hello.txt")

with open(file_path,"w") as f:
    f.write("Hello to python!\n")

with open(file_path, "r") as f:
    content=f.read()

print("File content:",content)
print("Saved at:",file_path)
