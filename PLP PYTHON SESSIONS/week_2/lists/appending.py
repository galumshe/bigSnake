
# To append an item to a list in Python, you use the .append() method. This method adds an item to the end of the list.
# Example:

my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the end of the list
print(my_list)
# Output: [1, 2, 3, 4]


# appending to a list
# Use append() multiple times (one for each element).
# Use extend(), which is designed to add multiple elements to a list.

'''Option 1: Using append() multiple times'''

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# Output: [10, 20, 30, 40]

''' Option 2: Using extend()'''

my_list = []
my_list.extend([10, 20, 30, 40])  # Add all elements at once
print(my_list)
# Output: [10, 20, 30, 40]

'''
Explanation:
append() adds a single item (e.g., 10) to the list.
extend() takes an iterable (like a list) and adds each element to the list individually.

If you attempt to use my_list.append(10, 20, 30, 40), Python will throw a TypeError.

'''