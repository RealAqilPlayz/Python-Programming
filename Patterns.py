import time

# Output:
# *
# **
# ***
# ****
# *****

def right_angle_triangle_of_stars(n):
    if n < 0:
        return

    for i in range(1, n+1, 1):
        print("*" * i)




# Output:
# *****
# ****
# ***
# **
# *
def inverted_right_angle_triangle_of_stars(n):
    for i in range(n, 0, -1):
        print("*" * i)






# Output:
#     *
#    ***
#   *****
#  *******
# *********

def pyramid(n):

    # think of counter j as the row number
    for j in range(1, n+1, 1):
        # print all spaces of a row
        for i in range(n - j):
            print(" ", end="")

        # print all stars of a row
        for i in range(2 * j - 1):
            print("*", end="")

        print("", end="\n")



"""
row        spaces         stars
1             4             1
2             3             3
3             2             5
4             1             7
5             0             9
"""


# Output:
# *********
#  *******
#   *****
#    ***
#     *

def inverted_pyramid(n):
    # think of counter j as the row number
    for j in range(1, n + 1, 1):
        # print all spaces of a row
        for i in range(j - 1 + 1):
            print(" ", end="")

        # print all stars of a row
        for i in range(2 * (n - j) + 1):
            print("*", end="")

        print("", end="\n")

"""
row      spaces        stars
1           0            9
2           1            7
3           2            5
4           3            3
5           4            1
"""

pyramid(5)
inverted_pyramid(4)















