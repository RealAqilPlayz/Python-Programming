# arbitrary arg passing
# We can pass any number of inputs for the function
def adder(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)


#adder(1, 3, 5)
#adder(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)


# A function that takes a combination of fixed and arbitrary args
def describe_pet(pet_name, *traits):
    print(pet_name + " has the following traits: ")
    for trait in traits:
        print("- " + trait)


#describe_pet("Kopi", "friendly", "playful", "loyal", "cheerful")
#describe_pet("Meowi", "agressive", "bad-tempered")
#describe_pet("Buddy")



def return_max(*nums):
    # assume the first num is the max
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    print(max)



def return_min(*nums):
    print(type(nums))
    print(nums)
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    print(min)

#return_min(10, 4, 5, 1)



def average(*args):
    if not args:
        print("args tuple is empty")
    else:
        print(sum(args) / len(args))

#average(1, 2, 3)





def sum_values(a, b=5, *c):
    total = a + b

    for i in c:
        total = total + i
    print(total)


# sum_values(2) # 7
# sum_values(2, 8) #10
# sum_values(2, 8, 4, 5) #19




# Never place an * variable in front a regular variable with no default value
def sum_values_2(*a, b=5, c):
    total = b + c

    for i in a:
        total = total + i
    print(total)


# sum_values_2(1, 2, 3, 4, 5) # ERROR! *variable shouldn't precede positional variable












