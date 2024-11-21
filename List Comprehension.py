# List comprehension
nums = [i for i in range(0, 10)]
nums = [i+10 for i in nums]
print(nums)


# Example 2
# Using List Comprehension
# Create a list that has all even numbers from -10 to 10
evenList = [i for i in range(-10, 11, 2)]
evenList = ["+" if i>0 else "-" for i in evenList]
print(evenList)


# Example 3
nums2 = [i for i in range(0, 10)]
nums2 = [i if i%2==0 else "*" for i in nums2]
print(nums2)


# Example 4 (List comprehension with string)
str1 = "F1-Grand-Prix"
str1_list = list(str1)
str1_list = [i+"#" for i in str1_list]
print(str1_list)


# Example 5
str2 = "aeson"
str2_list = [i for i in str2] #for each i in str2, add i to str2_list

print(str2_list)

"""
vowel - remains
consonant - "-"

['a', 'e', 's', 'o', 'n']
['a', 'e', '-', 'o', '-']
"""























