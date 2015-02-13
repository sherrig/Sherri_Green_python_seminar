Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.random
<built-in method random of Random object at 0x1030a0220>
>>> random.random()
0.5241088130261797
>>> random.__file__
'/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.pyc'
>>> ================================ RESTART ================================
>>> 
>>> q[1]
[-1, 0, 1, -1]
>>> q
[[1, 0, 1, 2], [-1, 0, 1, -1], [0, 1, -1, 1], [0, -1, -1, -2]]
>>> [1, 0, 1, 2] + [-1, 0, 'string', -1]
[1, 0, 1, 2, -1, 0, 'string', -1]
>>> 'string' + 'thing'
'stringthing'
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/joegriffin/Documents/Work/ES.S70/Untitled.py", line 54, in <module>
    E_tot[0] = E[0][0] + E[1][0] + E[2][0] + E[3][0]        #   can add together the components to
NameError: name 'E' is not defined
>>> ================================ RESTART ================================
>>> 
[-9532738223.337902, -9532738223.337902, -6355158815.558601]
>>> ================================ RESTART ================================
>>> 
E = [-9532738223.337902, -9532738223.337902, -6355158815.558601] N/C
>>> from const import E0
>>> E0
8.854187817e-12
>>> ================================ RESTART ================================
>>> def function(x):
	return x+1

>>> function(4)
5
>>> function(3)
4
>>> function(3.0)
4.0
>>> function('string')

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    function('string')
  File "<pyshell#12>", line 2, in function
    return x+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> def function(x):
	print x+1

	
>>> funciton(4)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    funciton(4)
NameError: name 'funciton' is not defined
>>> function(4)
5
>>> def function(x):
	return x+1

>>> function(function(4))
6
>>> def function(x):
	print x+1

	
>>> function(function(4))
5

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    function(function(4))
  File "<pyshell#25>", line 2, in function
    print x+1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> c = 1
>>> def f(n)
SyntaxError: invalid syntax
>>> def f(n):
	c = c + n

	
>>> f(3)

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    f(3)
  File "<pyshell#31>", line 2, in f
    c = c + n
UnboundLocalError: local variable 'c' referenced before assignment
>>> def f(n):
	c = 1
	c = c + n

	
>>> f(3)
>>> c
1
>>> l = [1, 4, 2]
>>> l.append(3)
>>> l
[1, 4, 2, 3]
>>> []
[]
>>> l = []
>>> l.append(3)
>>> l
[3]
>>> 
