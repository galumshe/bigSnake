notes for lists in python

In Python, tuples and lists are both used to store collections of items, but they have some key differences:

Mutability:

Lists are mutable, meaning you can modify them (add, remove, or change elements).
Tuples are immutable, meaning once created, they cannot be changed.
Syntax:

Lists are defined with square brackets: my_list = [1, 2, 3].
Tuples are defined with parentheses: my_tuple = (1, 2, 3).
Use Cases:

Use lists when you need a collection that can change, such as a list of items in a shopping cart.
Use tuples when you want a fixed collection, such as coordinates (x, y) or other data that should not be altered.
Performance:

Tuples can be slightly faster than lists due to their immutability, which allows Python to optimize their memory usage.


Summary Table
Method	Removes by	Behavior
.remove(value)	Value	Removes the first occurrence of value.
del my_list[index]	Index	Deletes the item at a specific index.
.pop(index)	Index	Removes and returns the item.
.clear()	Entire list	Empties the list.
Let me know if you need examples for specific cases! 😊

<td>