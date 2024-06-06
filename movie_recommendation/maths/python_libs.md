# Approach : Using extend() method

Step-by-step approach:

First, import the “collections” module in the Python program.
Define two lists: lst1 and lst2 which contain some integer values.
Use the extend() method to append all the elements of lst2 to lst1. Now, lst1 contains all the elements of both lst1 and lst2.
Use the print() function to display the combined list, lst1, which maintains the repetition of elements.
Use the set() function to create a set from lst1, which will not maintain the repetition of elements or the order of elements.
Use the list() function to convert the resulting set back into a list.
Use the print() function to display the new list, x, which does not maintain repetition or order.

# Python program to illustrate union
 
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst1.extend(lst2)
 
# Maintaining repetition
print("Maintaining repetition "+str(lst1))
 
# Not maintaining repetition and order
x = list(set(lst1))
print("Not maintaining repetition "+str(x))



################################################################################

# Approach : Using itertools

The itertools module has functions for working with iterable data structures in Python. One of its functions is chain() function which can be used to concatenate two or more lists together.

Algorithm:

Import the itertools module.
Use the chain() function from the itertools module to concatenate two or more lists into one list.
Use the set() function to remove duplicates and convert the concatenated list to a set
Convert the set back to a list and return it as the final union
Return the concatenated list.



# import the itertools module
import itertools
 
# define the function to find the union of two or more lists
def union_lists(*lists):
     
    # use the chain() function from itertools to concatenate all the lists
    concatenated_list = list(itertools.chain(*lists))
     
    # use the set() function to remove duplicates and convert the concatenated list to a set
    unique_set = set(concatenated_list)
     
    # convert the set back to a list and return it as the final union
    final_union = list(unique_set)
    return final_union
 
# Example usage of the function
list1 = [23, 15, 2, 14, 14, 16, 20 ,52]
list2 = [2, 48, 15, 12, 26, 32, 47, 54]
list3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]
 
# Find the union of three lists
print(union_lists(list1, list2, list3))




#############################################################################################

Intersection

# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 
# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))


# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
	return list(set(lst1) & set(lst2))

# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))




# Python program to illustrate the intersection
# of two lists using set() and intersection()
def Intersection(lst1, lst2):
	return set(lst1).intersection(lst2)
	
# Driver Code
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))





# Python program to illustrate the intersection
# of two lists
def intersection(lst1, lst2):

	# Use of hybrid method
	temp = set(lst2)
	lst3 = [value for value in lst1 if value in temp]
	return lst3

# Driver Code
lst1 = [9, 9, 74, 21, 45, 11, 63]
lst2 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
print(intersection(lst1, lst2))








# Python program to illustrate the intersection
# of two lists, sublists and use of filter()
def intersection(lst1, lst2):
	lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
	return lst3

# Driver Code
lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print(intersection(lst1, lst2))




# Using reduce
from functools import reduce

lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

intersection = reduce(lambda acc, x: acc + [x] if x in lst2 and x not in acc else acc, lst1, [])

print(intersection)
#This code is contributed by Rayudu.




