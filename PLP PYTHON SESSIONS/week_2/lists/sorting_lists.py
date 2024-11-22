# sorting lists
''' the .sort() method does not take any arguments (other than optional ones like key or reverse). Passing my_list to .sort() will raise an error.

Here's the correct way to sort the list in ascending order:'''

my_list = [30, 10, 20, 40]
my_list.sort()  # Sorts the list in ascending order
print(my_list)
# Output: [10, 20, 30, 40]

'''
Key Notes:
.sort() modifies the list in place:

It directly changes the original list.
It does not return a new list.
If you need a new sorted list without modifying the original, use the sorted() function:

'''

my_list = [30, 10, 20, 40]
new_list = sorted(my_list)  # Creates a new sorted list
print(new_list)
# Output: [10, 20, 30, 40]

''' 
Optional Arguments for Sorting:
reverse=True: To sort in descending order.
'''

# reverse=True: To sort in descending order.
my_list.sort(reverse=True)
print(my_list)
# Output: [40, 30, 20, 10]

# key=function: To sort based on a custom key.
my_list = ["apple", "banana", "cherry"]
my_list.sort(key=len)  # Sort by string length
print(my_list)
# Output: ['apple', 'cherry', 'banana']

