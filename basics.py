# Now we're going to learn about the basics of Python programming.

# This is a single line comment

"""
This is a multi-line comment
"""

sum = 1 + 1 # This is an expression
print(sum) # This is a statement

# Math is what you would expect
print(1 + 1) # 2
print(8 - 1) # 7
print(10 * 2) # 20
print(35 / 5) # 7.0 

# Division is a bit tricky. It is integer division and floors the results automatically
# Rounds towards negative infinity
# It's always a float
print(5 / 2) # 2.5  (not 2)

# To fix this, you can use float division
print(5 / 2.0) # 2.5
print(5.0 / 2) # 2.5  (also works)

# Modulo operation
print(7 % 3) # 1

# Exponentiation (x to the power of y)
print(2 ** 3) # 8 
# The above ^ is new to me, didn't know you could do 2^3 as 2 ** 3. That's cool.

# Boolean values are primitives (Note: True and False are capitalized)
print(True)
# and and or in Python are written out:
print(True and False) # False
print(True or False) # True

# Don't forget is and is not
print(1 is 1) # True
print(1 is not 1) # False

# Negation is written as not
print(not True) # False

# True and False are actually 1 and 0 but with different keywords
# Comparison operators look like this:
print(1 == 1) # True

# They look at the numerical value of True and False:
print(True == 1) # True
print(False == 0) # True
print(True == 0) # False
print(False == 1) # False

# None, 0 and empty strings/lists/dicts/tuples/sets all evaluate to False
bool(0)      # => False
bool("")     # => False
bool([])     # => False
bool({})     # => False
bool(())     # => False
bool(set())  # => False
bool(4)      # => True
bool(-6)     # => True

# Strings!

# Strings are created with " or '
print("This is a string.")
print('This is also a string.')

# Strings can be added too! But try not to do this.
print("Hello " + "world!") # Hello world!

# Strings can be added without the + operator
print("Hello " "world!") # Hello world!

# Strings can be multiplied
print("Hello" * 3) # HelloHelloHello

# A string can be treated like a list of characters
print("This is a string"[0]) # T

# You can find the length of a string
print(len("This is a string")) # 16

# You can also format using the % operator
x = "apple"
y = "lemon"
z = "The items in the basket are %s and %s" % (x, y)
print(z) # The items in the basket are apple and lemon

# A newer way to format strings is the format method
# This method is the preferred way
# It's available since Python 2.6
print("The items in the basket are {} and {}".format(x, y)) # The items in the basket are apple and lemon

# You can use keywords if you don't want to count.
print("The items in the basket are {fruit1} and {fruit2}".format(fruit1="apple", fruit2="lemon")) # The items in the basket
# are apple
# and lemon

# You can also format using f-strings
# This method is the preferred way
# It's available since Python 3.6
print(f"The items in the basket are {x} and {y}") # The items in the basket are apple and lemon

# None is an object
# None is used to represent the absence of a value
x = None
print(x == None) # True
print(x is None) # True

# Don't use the equality "==" symbol to compare objects to None
# Use "is". This checks for equality of object identity.
# This is the preferred way
print(x == None) # True
print(x is None) # True

# Don't forget the strings print a newline at the end by default
print("Hello, World!")
# If you don't want a newline, you can use the end argument
print("Hello, World!", end="")
print("Hello, World!", end=" ")
print("Hello, World!", end="!\n")

# Listssss

# Lists are like arrays in other languages
# They can contain any type of variable, and they can contain as many variables as you wish
# Lists can be defined with square brackets []
# Lists are mutable
# Lists are 0-indexed
# Lists can be nested

# Add items to a list with append
li = []
li.append(1) # li is now [1]

# Access a list like you would any array
print(li[0]) # 1

# Assign new values to indexes that have already been initialized with = li[0] = 42

# You can add lists
li.append(2) # li is now [1, 2]
print(li) # [1, 2]

# Remove from the end with pop
li.pop() # => 2 and li is now [1]

# You can add lists with addition
li + [3, 4] # => [1, 3, 4] but li is unchanged

# Concatenate lists with extend
li.extend([3, 4]) # li is now [1, 3, 4]

# Remove arbitrary elements from a list with "del"
del li[0] # li is now [3, 4]

# Remove first occurrence of a value
li.remove(3) # li is now [4]

# Insert an element at a specific index
li.insert(0, 5) # li is now [5, 4]

# Get the index of the first item found matching the argument
li.index(4) # => 1

# Check for existence in a list with "in"
1 in li # =>  False

# Examine the length with "len()"
len(li) # => 2

# Look at range with slice syntax
li[1:] # => [4]
li[2:] # => []

li = [1, 2, 3, 4, 5]
li[1:3] # => [2, 3] # return list from index 1 to 3
li[2:] # => [3, 4, 5] # return list from index 2 to end
li[:3] # => [1, 2, 3] # return list up to index 3
li[::2] # => [1, 3, 5] # return list selecting elements with a step of 2
li[::-1] # => [5, 4, 3, 2, 1] # return list in reverse 

# Dictionary

# Dictionaries store mappings from keys to values
# Dictionaries can be defined with curly braces {}
# Dictionaries are mutable
# Dictionaries are unordered
# Dictionaries can be nested

empty_dict = {}
# Here's a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with []
filled_dict["one"] # => 1

# Get all keys as a list with "keys()"
filled_dict.keys() # => ["one", "two", "three"]

# Get all values as a list with "values()"
filled_dict.values() # => [1, 2, 3]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict # => True
1 in filled_dict # => False

# Looking up a non-existing key is a KeyError
# filled_dict["four"] # KeyError

# Use get() method to avoid the KeyError
filled_dict.get("one") # => 1
filled_dict.get("four") # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4) # => 1
filled_dict.get("four", 4) # => 4

# Set the value of a key with a value
filled_dict["four"] = 4 # filled_dict is now {"one": 1, "two": 2, "three": 3, "four": 4}

# Remove keys from a dictionary with del
del filled_dict["one"] # {"two": 2, "three": 3, "four": 4}

# Sets

# Sets store ... well sets
# Sets can be defined with curly braces {}
# Sets are unordered
# Sets contain no duplicates
# Sets can be used for set operations

empty_set = set()
# Initialize a set with a bunch of values
some_set = {1, 1, 2, 2, 3, 4} # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable
# You can add to sets with the add method
some_set.add(5) # some_set is now {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
some_set & other_set # => {3, 4, 5}

# Do set union with |
some_set | other_set # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
some_set - other_set # => {1, 2}

# Do set symmetric difference with ^
some_set ^ other_set # => {1, 2, 6}

# Check if set on the left is a superset of set on the right
some_set > {1, 2} # => True

# Check if set on the left is a subset of set on the right
{1, 2} < some_set # => True

# Check for existence in a set with in
2 in some_set # => True

# Can you delete from a set?
# Yes, with the discard method
some_set.discard(5) # some_set is now {1, 2, 3, 4}
# If the element is not in the set, nothing happens
some_set.discard(5) # some_set is still {1, 2, 3, 4}

# Control flow and iterables

some_var = 5

# Here is an if statement. Indentation is significant in Python!
# Convention is to use 4 spaces (not tabs!) for indenting.

if some_var > 10:
  print("some_var is totally bigger than 10.")
elif some_var < 10:
  print("some_var is smaller than 10.")
else:
  print("some_var is indeed 10.")

# For loops iterate over lists
for animal in ["dog", "cat", "mouse"]:
  print("{} is a mammal".format(animal))

# "range(number)" returns an iterable of numbers from zero to the given number
for i in range(4):
  print(i)

# "range(lower, upper)" returns an iterable of numbers from the lower number to the upper number
for i in range(4, 8):
  print(i)

# "range(lower, upper, step)" returns an iterable of numbers from the lower number to the upper number, while incrementing by step. 
# If step is not indicated, the default value is 1.
for i in range(4, 8, 2):
  print(i)

# While loops go until a condition is no longer met
x = 0
while x < 4:
  print(x)
  x += 1  # Shorthand for x = x + 1

# Handle exceptions with a try/except block
try:
  # Use "raise" to raise an error
  raise IndexError("This is an index error")
except IndexError as e:
  pass  # Pass is just a no-op. Usually you would do recovery here.

# Instead of try/finally to cleanup resources you can use with to auto close resources
with open("file.txt") as f:
  for line in f:
    print(line)

# Python also has iterators

# You can define your own iterator by defining a class with __iter__ and __next__ methods
class Fib:
  def __init__(self):
    self.a, self.b = 0, 1

  def __iter__(self):
    return self

  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    return self.a

# You use an iterator by calling next() on it
fib = Fib()
print([next(fib) for _ in range(10)])

# You can use iter() to convert the iterable to an iterator
print([x for x in iter([1, 2, 3, 4, 5])])

# List comprehensions provide a powerful way to create lists
# These are also iterators
print([x for x in range(5) if x % 2 == 0]) # => [0, 2, 4]

# You can construct set and dict comprehensions as well.
print({x for x in 'abcddeef' if x in 'abc'}) # => {'a', 'b', 'c'}
print({x: x**2 for x in range(5)}) # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Functions

# Use "def" to create new functions
def add(x, y):
  print("x is {} and y is {}".format(x, y))
  return x + y  # Return values with a return statement

# Calling functions with parameters
add(5, 6) # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments

add(y=6, x=5) # Keyword arguments can arrive in any order.

# You can define functions that take a variable number of positional arguments
def varargs(*args):
  return args

print(varargs(1, 2, 3)) # => (1, 2, 3)

# You can define functions that take a variable number of keyword arguments, as well
def keyword_args(**kwargs):
  return kwargs

# Let's call it to see what happens
print(keyword_args(big="foot", loch="ness")) # => {"big": "foot", "loch": "ness"}

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
  print(args)
  print(kwargs)

all_the_args(1, 2, a=3, b=4) # prints (1, 2) and {"a": 3, "b": 4}

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand positional arguments and use ** to expand keyword arguments
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs) # equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs) # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)

# You can pass args and kwargs along to other functions that take args/kwargs
# by expanding them with * and ** respectively
def pass_all_the_args(*args, **kwargs):
  all_the_args(*args, **kwargs)

pass_all_the_args(1, 2, 3, a=4, b=5)

# Function Scope

x = 5

def set_x(num):
  # Local var x not the same as global variable x
  x = num # => 43
  print(x) # => 43

def set_global_x(num):
  global x
  print(x) # => 5
  x = num # global var x is now set to 6
  print(x) # => 6

set_x(43)
set_global_x(6)

# Python has first class functions
# This means you can pass functions to other functions
def create_adder(x):
  def adder(y):
    return x + y
  return adder

add_10 = create_adder(10)
add_10(3) # => 13

# There are also anonymous functions
print((lambda x: x > 2)(3)) # => True
print((lambda x, y: x ** 2 + y ** 2 )(2, 1)) # => 5

# There are built-in higher order functions
print(list(map(add_10, [1, 2, 3]))) # => [11, 12, 13]
print(list(map(max, [1, 2, 3], [4, 2, 1]))) # => [4, 2, 3]
print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))) # => [6, 7]

# You can use list comprehensions for nice maps and filters
print([add_10(i) for i in [1, 2, 3]]) # => [11, 12, 13]
print([x for x in [3, 4, 5, 6, 7] if x > 5]) # => [6, 7]

# You can construct set and dict comprehensions as well.
print({x for x in 'abcddeef' if x in 'abc'}) # => {'a', 'b', 'c'}
print({x: x**2 for x in range(5)}) # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Modules

# You can import modules
import math
print(math.sqrt(16)) # => 4.0

# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7)) # => 4.0
print(floor(3.7)) # => 3.0

# You can import all functions from a module.
# Warning: this is not recommended
from math import *

# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16) # => True

# Python modules are just ordinary Python files. You can write your own, and import them. The name of the module is the same as the name of the file.

# If you have a Python script named math.py in the same folder as your current script, the file math.py will be loaded instead of the built-in Python module.

# You can find out which functions and attributes are defined in a module.
import math
dir(math)

# You can also use the help function on modules
help(math)
help(math.ceil)

# Everything is an object

# Python is an object-oriented language, and in Python everything is an object.

# Functions are objects
def foo():
  print("foo")

# Classes

# Classes are defined with the class keyword
class Human:

  # A class attribute. It is shared by all instances of this class
  species = "H. sapiens"

  # Basic initializer
  def __init__(self, name):
    # Assign the argument to the instance's name attribute
    self.name = name

  # An instance method. All methods take self as the first argument
  def say(self, msg):
    return "{name}: {message}".format(name=self.name, message=msg)

  # A class method is shared among all instances
  # They are called with the calling class as the first argument
  @classmethod
  def get_species(cls):
    return cls.species

  # A static method is called without a class or instance reference (doesn't need self!)
  @staticmethod
  def grunt():
    return "*grunt*"

#A @property is a way to define a method that can be accessed as an attribute
class Jack:
  def __init__(self, age):
    self.age = age

# read-only attribute
  @property
  def age(self):
    return self._age

# allows the property to be set
  @age.setter
  def age(self, value):
    if value < 0:
      raise ValueError("age can't be negative")
    self._age = value

# allows the property to be deleted
  @age.deleter
  def age(self):
    del self._age



