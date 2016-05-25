# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def smallest(a,b,c):
	big=biggest(a,b,c)
	if a==big:
		if b>c:
			return c
		else:
			return b
	if b==big:
		if a>c:
			return c
		else:
			return a
	if c==big:
		if a>b:
			return b
		else:
			return a

def set_range(a,b,c):
    big=biggest(a,b,c)
    small=smallest(a,b,c)
    return big-small

def median(a,b,c):
	if a==biggest(a,b,c):
		return bigger(b,c)

	if b==biggest(a,b,c):
		return bigger(a,c)
	
	else:
		return bigger(a,b)


#TEST
print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1, 4, 4)
#>>> 3  # since 4 - 1 = 3

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7