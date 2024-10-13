# numbers[0] should give 3 (first element)
# numbers[-1] should give 2 (last element)
# numbers[3] should give 1 (forth element)
# numbers[:-1] [3,1,4,1,5,9] should give all except the last element
# numbers[3:4] should give [1]
# 5 in number should give True
# 7 in number should give False
# "3" in numbers should give False
# numbers + [6, 5, 3] should give [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] adding more in the elements


numbers = [3, 1, 4, 1, 5, 9, 2]

# 1
numbers[0] = "ten"

# 2
numbers[-1] = 1

# 3
print(numbers[2:])
# 4
print(9 in numbers)