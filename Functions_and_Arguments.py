# A Parameterised Function

numList = [10, 20, 30, 40, 50]
priceList = [1, 2, 3, 4, 5]

def sum_all(anyList):
    # use a for-each loop to iterate through list
    sum = 0
    for i in anyList:
        sum = sum + i
    return sum


def sum_two_lists(list1, list2):
    if len(list1) == len(list2):
        resultList = []
        # use range-based for loop to iterate both lists at the same time
        for i in range(0, len(list1), 1):
            resultList.append(list1[i] + list2[i])
        return resultList
    else:
        print("Submit two lists of identical size")


# Default arguments
# preset a value for an arg
def sum_two_nums(x = 0, y = 0):
    print(x + y)



# Keyword arguments
def intro(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)





# Revision
def search_target(anyList=[], target=0):
    for i in anyList:
        if i == target:
            print("Target found")
            return
    print("Target not found")


#search_target() #error
#search_target(numList, 0)
#search_target(numList, 22)
#search_target(target=22, anyList=numList)
search_target()















