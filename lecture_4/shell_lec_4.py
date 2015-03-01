Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> rod = cylinder(pos=(-L/2,0,0), axis=(L,0,0), radius=0.03, opacity=0.5, color=color.red)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    rod = cylinder(pos=(-L/2,0,0), axis=(L,0,0), radius=0.03, opacity=0.5, color=color.red)
NameError: name 'cylinder' is not defined
>>> rod = cylinder(pos=(-L/2,0,0), axis=(L,0,0), radius=0.03,
               opacity=0.5,color=color.red)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    rod = cylinder(pos=(-L/2,0,0), axis=(L,0,0), radius=0.03,
NameError: name 'cylinder' is not defined
>>> import math
>>> math.cos(3)
-0.9899924966004454
>>> from math import cos
>>> cos(3)
-0.9899924966004454
>>> def gt(arg1, arg2):
	if arg1 > arg2:
		return True
	else:
		return False

	
>>> ================================ RESTART ================================
>>> 
True
String
>>> ================================ RESTART ================================
>>> 
String
>>> def gt(arg1, arg2):
	if arg1 > arg2:
		return True
	elif arg1 == arg2:
		return None
	else:
		return False

	
>>> gt(5, 5)
>>> def gt(arg1, arg2):
	if arg1 > arg2:
		print True
	if arg1 >= arg2:
		print None
	else:
		print False

		
>>> gt(5, 5)
None
>>> gt(6, 5)
True
None
>>> for i in range(10):
	print i

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10) + range(5):
	print i

	
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
>>> for i in (1, 2, 3):
	print i

	
1
2
3
>>> for i in xrange(10):
	print i

	
0
1
2
3
4
5
6
7
8
9
>>> xrange(10)
xrange(10)
>>> type(xrange(1))
<type 'xrange'>
>>> xrange(10)[5]
5
>>> range(10)[5]
5
>>> def total(List):
	Sum = 0
	for i in List:
		Sum = Sum + i
	return Sum

>>> total(range(10))
45
>>> a = 0
>>> while i < 10:
	a += i

	

Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    a += i
KeyboardInterrupt

>>> i = 0
>>> while i < 10:
	a += i
	i += 1

	
>>> a
521904708
>>> a = 0
>>> while i < 10:
	a += i
	i += 1

	
>>> a
0
>>> i = 0
>>> a = 0
>>> while i < 10:
	a += i
	i += 1

	
>>> a
45
>>> while i < 10:
	a += i
	i += 1
	break

>>> i = 0; a = 0
>>> i = 1
>>> while i < 10:
	a += i
	i += 1
	break

>>> a
1
>>> while i < 10:
	a += i
	i += 1
	pass

>>> if False:
	print 'fun'
else:
	pass

>>> i = 0; a = 0
>>> while i < 10:
	a += i
	i += 1
	continue
	break

>>> a
45
>>> while not (i < 10):
	a += i
	i += 1
	continue
	break


Traceback (most recent call last):
  File "<pyshell#81>", line 3, in <module>
    i += 1
KeyboardInterrupt
>>> a
2472017520419028
>>> 
