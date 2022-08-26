# Comments:
'''
- Comments in program are written to make program
more readable. These lines are ignored by the interpreter.
- Use # symbol for single line comment.
- For multiline comment: Use either tripple single or double
quotes at start and end of lines.
'''

# Statement:
'''
- Statements are the instructions that a python interpreter
can execute.
'''
#print("hello") # single line statement
#a=10; # single line statement (semicolon is optional)
#print(a)

# for multiline statement:
# optn 1: Use escape character i.e, \ (line continuation charcater)
'''
b= 10+20\
+30+40
print(b)
'''
# optn 2: Use bracket ()
'''
c= (10+20
+30+40)
print(c)
'''

# Tokens:
'''
- Token is the smallest unit inside the given program.
- Tokens can be defined as a punctuator mark, reserved words
and each individual word in a statement.
- There are following tokens in Python:
    - Keywords
    - Identifiers
    - Literals
    - Operators
'''

# Keywords:
'''
- Python keywords are the reserved words in python.
- These keywords have a special meaning to python interpreter.
- Python keywords can not be used as identifier names.
- Keywords are case sensitive.
'''
'''
import keyword # It's a module
kw = keyword.kwlist
print(kw)
# kwlist is an attribute which return list of python keywords.
print(len(kw))
# len() to calculate length of a sequence
'''

# Identifiers:
'''
- Identifiers in python are those names that identify a
variable, function, class, module, package, or object.
- It helps in differentiating one entity from another.
- Naming Rule:
* Only lowercase or uppercase alphabets(a-z, A-Z) or digit(0-9)
or an underscore character combination is used.
* An identifier can't start with a digit.
* Keywords can't be used for identifier naming.
* Special characters like !,@ etc can't be used.
- Eg.
    var=10 (valid)
    1var = 10 (Invalid)
    v@r = 10 (Invalid)
    var age=10 (Invalid)
    _var= 10 (valid)
'''

# Literals:
'''
- Literals can be defined as a data that is given in a
variable or constant.

# Python support the following literals:
- 1. String literals: String literals can be formed by
enclosing a text in the quotes.

- 2. Numeric literals: Numeric Literals are immutable.

- 3. Boolean literals: A Boolean literal can have any of
the two values: True or False.

- 4. Special literals: Python contains one special literal
i.e., None.
None is used to specify to that field that is not created.
It is also used for end of lists in Python.

- 5. Literal Collections: Collections such as tuples, lists,
dictionary, sets, array etc are used in Python.
'''

# Variable or Reference Variable:
'''
- In python variables is an entity which stores
(in stack memory) the memory address of referenced value
(object) stored inside memory(heap memory).
    - Similar to pointers in C, variables in Python refer to
    values (or objects) stored somewhere in memory.
'''

# Variable Assignment: Use assignemnt operator: =
# Single Variable assignment:
a=10

# Multiple variable Assignment:
b,c = 20,'Hello'
d=e=50
















