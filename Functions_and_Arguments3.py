"""
In Python, we primarily have five ways to pass arguments to functions:

Positional Arguments
Keyword Arguments
Default Arguments
Variable-Length Positional Arguments (*args)
Variable-Length Keyword Arguments (**kwargs)
"""

def print_employee_info(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}")



# Calling the function with different keyword arguments
print_employee_info(name="Brian", age=20, salary=5000, experience=10)
print_employee_info(name="Cindy", age=25, salary=6000, experience=15)





























