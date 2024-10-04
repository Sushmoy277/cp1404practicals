# 1.
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()
# 3.
in_file = open("number.txt", "r")
numbers1 = int(in_file.readline())
numbers2 = int(in_file.readline())
in_file.close()
print(f"The sum of line 1 and 2 is {numbers1 + numbers2}")

# 4.
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
print(f"The sum of lines is {total}")
in_file.close()
