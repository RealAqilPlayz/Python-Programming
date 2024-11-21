# Example 1:
def get_info():
    info_line = input("Enter your name-age-gender (separated by hyphen): ").split("-")
    print(type(info_line))

    print(f"Name: {info_line[0]}")
    print(f"Age: {info_line[1]}")
    print(f"Gender: {info_line[2]}")

get_info()


"""
input:

Eros-25-male



output: 

Name: Eros
Age: 25
Gander: Male
"""






# List Comprehension with integers
numList = [i for i in range(10, 20)]
print(numList)

# List comprehension with strings
# .split() separates a line of input into multiple parts
# .strip() removes leading/trailing space from a string
names = input("Enter your name: ").split(",")
names = [i.strip() for i in names]
print(names)


