'''
Python gotchas
 Some gothchas and interesting behaviour of the Python interpreter 
 encountered during development and working through the great book 
 on Data Structures and Algorithms by Michael T. Goodrich et al.
'''


## SET ____________________________________________________________
#
# although {x,y} inits a set, {} is an empty dictionary, NOT a set
# both set and dict share the same definition notiation { }
set1 = {'white','blue'}
dict1 = {'key': 'value'}
empty_set = set() # can't do this with {}
empty_dict = {}

# remember that sets do not hold duplicates and are in random order
set2 = set('Hello world') # result: {'w', 'H', ' ', 'd', 'e', 'o', 'l', 'r'} 

# sorted set becomes a list which makes sense because a set is in random order but might not be what you expect
list1 = sorted(set2) # result: [' ', 'H', 'd', 'e', 'l', 'o', 'r', 'w']


## RANGE (and comprehension example) ______________________________
#
# ranges are not inclusive
range(1,5) # returns iterable object with values 1, 2, 3, 4 so not including stop value (5)
range(5)   # returns iterable object with values 0, 1, 2, 3, 4 range defines the length (5) - eg to iterate over a data sequence (list, set, tuple, dict)

# range(n) returns iterable <range> object, not a list with n items
# this also means large n like range(1000000) does not calculate/reserve a million values in memory but only when needed
list1 = list(range(10)) # can be used to generate a list with the actual numbers

# list comprehension example producing sqares of numbers based on a range
list2 = [ k * k for k in range(1, 10) ] 
# (useless) example with conditional expression and list comprehension
# not very readable so be careful but can sometime be useful
list3 = [ -k if k % 2 == 0 else k for k in range(1, 10) ] 


## ROUND (even vs. odd / round up vs. round down) _________________
#
# round is broken toward the even value in a tie
round(2.5) # result: 2 (not 3) because closest even value is 2, not 3 so rounds down
round(3.5) # result: 4 (not 3) because closest even value is 4, not 3 so rounds up


## AUTO PACK/UNPACK _______________________________________________
#
# Python automatically packs multi values as a tuple
# Not really relevant but at least good to be aware of
return x, y  # result: tuple(x, y) because Python will still return a single tuple object
a = 2, 4  # similar to this statement which creates a new tuple object
b, c = a  # automatically unpacks tuple values to b and c


## += ASSIGNMENT OPERATOR _________________________________________
# 
# Python object behaviour might not be what you expect when using assignment operator +=
# Consider this example, first using list + x and then list += x
# Variant 1: +
list1 = [1,2,3]
list2 = list1
list2 = list1 + [4,5]
# Result:
#  list1 [1, 2, 3] 
#  list2 [1, 2, 3, 4, 5]
# Note: only list2 has changed, which is likely as expected, but hold on for variant 2
# list2 is no longer an alias for list1 but a new object

# Variant 2: +=
list1 = [1,2,3]
list2 = list1
list2 += [4,5]
# Result:
#  list1 [1, 2, 3, 4, 5]
#  list2 [1, 2, 3, 4, 5]
# Note: both list1 and list2 have been extended and not only list 2 as in variant 1
# list2 and list1 are both still an alias for the same object

# The same applies to MUTABLE object types passed to a function (e.g. list)
# The following assignment within the function will change the values of object l
def extend_list(l):
	l += [4,5]

l1 = [1,2,3]
extend_list(l1)
# Result:
# l1 [1, 2, 3, 4, 5] 
# Note: assignments within the function affects the object outside of function scope
# Make sure that your function name makes this clear and this behaviour is intended
# If not desired, do not use += operator - cannot assign to local var first because it will still behave as above

# However, this does NOT apply to IMMUTABLE types (strings or numbers)
def add_ten(a):
	a += 10

i1 = 5
add_ten(i1)
# Result: 
# i1 = 5, NOT 15 
# local a in the scope of the function add_ten is 15 (which is likely what you expect)

## SCOPE/NAMESPACE ________________________________________________
# 
# Python tries to resolve a variable from a 'higher' scope
g_var1 = 1
g_var2 = 10
g_var3 = 100
def some_function():
	# Even if not explicitly defined as global, 
	# g_var1 in the local scope of this function will reference to global g_var1
	# no UnboundLocalError will be thrown which might result in unexpected behaviour.
	# Especially for common var names like i, j, n, etc.
	# Note: see what happens to g_var3 below though.
	print('g_var1 exists here:', g_var1) # Result: 1, not UnboundLocalError

	# The following assignment creates a new local var.
	# This does not affect the equally named global var which is as expected. 
	g_var2 = 50 # Result: within function: g_var2 = 50, outside function g_var2 = 10

	# The following will throw an UnboundLocalError: 
	# local variable 'g_var3' referenced before assignment.
	g_var3 += 10  # or g_var3 = g_var3 + 10 (same behaviour)

	# So unless defined as 'global g_var3' condider these global vars as read-only!
	# Or better: do not rely on them at all because that might result in unexpected behaviour.
	# This can still introduce some perky bugs.

# To be continued...
