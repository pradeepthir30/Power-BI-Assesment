import os
with open('example.txt', 'w') as file:
    file.write("hello everyone\n")

with open("example.txt", "a") as file:
    file.write("completing the assigned task.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

if os.path.exists("example.txt"):
    print("example.txt exists")

