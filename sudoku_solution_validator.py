# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

incorrect6 = [ [2, 1, 3],
               [3, 2, 1]]
               
def validate_square(square): #Check if elements are all integers and if columns=rows
	rows=len(square)
	for e in square:
		cols=len(e)
		if rows!=cols:
			return False
		for f in e:
			if type(f)!=int: return False
	return True


def check_line(line):
	n = len(line)
	i=0
	while i < n:
		# print 'Linea da controllare: ' + str(e)
		# print 'Elemento da controllare: ' + str(i+1)
		# print (i+1) in e
		if (i+1) not in line:
			return False
		else: i = i+1
	return True

def check_sudoku(square):
	if not validate_square(square):
		return False
	
	n = len(square)

# Check all rows
	for e in square:
		if not check_line(e):
			return False

# Check all cols
	j=0
	while j<n:
		col_to_check=[]
		for e in square:
			col_to_check.append(e[j])
		if not check_line(col_to_check):
			return False
		j=j+1

	return True




#TEST LAZ
#print validate_square(incorrect6)

#print check_sudoku(incorrect6)
#>>> False

#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False


