# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
with open("file.txt") as file:
    contents = file.read()
    print(contents)

# with open("file.txt", mode="a") as file:
#     contents = file.write(" New Text.")
#     print(contents)

# with open("file.txt", mode="w") as file:
#     contents = file.write("New Text.")

with open("file1.txt", mode="w") as file:
    contents = file.write("New Text.")