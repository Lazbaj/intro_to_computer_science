# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# find_element con ciclo for
# def find_element(mylist,value):
# 	pos=0
# 	for e in mylist:
# 		if e==value:
# 			return pos
# 		pos=pos+1
# 	return -1

# find_element con metodo index ed operatore IN
def find_element(mylist,value):
	if value in mylist:
		return mylist.index(value)
	else:
		return -1


#TEST
print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1


#-------------------------------------------
# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(list1,list2):
	for e in list2:
		if e not in list1:
			list1.append(e)


# TEST
a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]

print b
#>>> [2,4,6]