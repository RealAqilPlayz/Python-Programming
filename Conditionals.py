"""
Variations of conditionals:
1. if
2. if - elif(s)
3. if - elif(s) - else
4. if - else
"""

country = "Japan"

if country == "Japan":
    print("^_^")

# In an if-elif stack, Python only executes the FIRST statement that evaluates to True
# Hence, there is AT MOST 1 output
# Example 1:
score = 10
if score > 5:
    print("@_@")
elif score > 7:
    print("$_$")

# Example 2:
age = 15
if age > 20:
    print("*_*")
elif age % 2 == 1:
    print("#_#")
elif age + 5 == 20:
    print("%_%")


# Example 3:
name = "Jennie"
if len(name) == 1:
    print("1")
elif len(name) == 2:
    print("2")
elif len(name) == 3:
    print("3")
else:
    print("None of the above")



# Example 4:
# Each if-stack is evaluated separately!
if 3 > 0:
    print("A")
elif (4 - 2) > 0:
    print("B")

if "A" == "a":
    print("C")
else:
    print("D")



# Example 5:
# There all 3 if-stacks!
price = 100

if price > 10:
    print(10)
if price > 20:
    print(20)
if price > 30:
    print(30)



























