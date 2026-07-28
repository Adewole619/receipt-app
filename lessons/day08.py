with open("data/hello.txt", "w") as file:
    file.write("Welcome to my Receipt App!\n")

with open("data/hello.txt", "r") as file1:
    print(file1.read())

with open("data/hello.txt", "a") as file2:
    file2.write("Another receipt\n")


with open("data/hello.txt", "r") as file3:
    print(file3.read())