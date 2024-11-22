# List
my_list = [1, 2, 3]
my_list[0] = 4  # This is allowed

# Tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This will raise an error

"""
In summary:

Lists = mutable, use square brackets [].
Tuples = immutable, use parentheses ().
"""


# To append an item to a list in Python, you use the .append() method. This method adds an item to the end of the list.

# Example:

my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the end of the list
print(my_list)
# Output: [1, 2, 3, 4]

# However, tuples are immutable, so you cannot directly append to a tuple. If you need to "add" items to a tuple, you must create a new tuple that combines the original tuple with the new elements.

# Example:

my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4,)  # Creates a new tuple with 4 added
print(my_tuple)
# Output: (1, 2, 3, 4)


# Remember, + (4,) creates a new tuple with the item, and my_tuple is reassigned to this new tuple.
#  The original my_tuple itself remains unchanged.