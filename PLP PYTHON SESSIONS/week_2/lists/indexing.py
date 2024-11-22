'''To find the index of a value in a list, you can use the .index() method. Here's how to do it:'''

# Example:

my_list = [10, 20, 30, 40]
index_of_30 = my_list.index(30)  # Finds the index of the first occurrence of 30
print(index_of_30)
# Output: 2

'''Key Notes:
.index(value):
Finds the first occurrence of value in the list.
Raises a ValueError if the value is not in the list.
'''

# Optional: Handling Errors
# If you're unsure whether the value exists in the list, use a conditional check:

my_list = [10, 20, 40]  # 30 is not in this list
if 30 in my_list:
    index_of_30 = my_list.index(30)
    print(index_of_30)
else:
    print("30 is not in the list")


'''what if i wanted to ptint 30 as a value alone?'''
# Example:
my_list = [10, 20, 30, 40]
print(my_list[2])  # Access the value at index 2 (30)
# Output: 30

'''
Steps:
'''
# Find the index of 30 using .index() (if needed):
index_of_30 = my_list.index(30)
print(my_list[index_of_30])
# Output: 30

# Alternatively, if you know the index already, directly access it:
print(my_list[2])  # 2 is the index of 30 in this example
# Output: 30

'''If you just want to print the value and it's already known 
(e.g., 30 exists in the list), simply use:'''

print(30)
# Output: 30
