Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 1
1
>>> 1.3
1.3
>>> 1.0
1.0
>>> 1.
1.0
>>> 'This is a string'
'This is a string'
>>> len('This is a string')
16
>>> 0.012348760123840815723408712034769736498618623451078263498612973645
0.012348760123840816
>>> 1239486087165098623498756928740962
1239486087165098623498756928740962L
>>> True
True
>>> False
False
>>> None
>>> var = True
>>> type(var)
<type 'bool'>
>>> var
True
>>> (1, 2, 3)
(1, 2, 3)
>>> [2, 5, 1]
[2, 5, 1]
>>> (1, 3.4, 'text')
(1, 3.4, 'text')
>>> var = (1, 3.4, 'text')
>>> var
(1, 3.4, 'text')
>>> var[1]
3.4
>>> type(var)
<type 'tuple'>
>>> var[1]
3.4
>>> l = [2, 'string', 1.0]
>>> l[2]
1.0
>>> 1 / 3
0
>>> 1.0 / 3.0
0.3333333333333333
>>> 2 / 3
0
>>> 1.0 / 3.0
0.3333333333333333
>>> 6 * 3
18
>>> 6 * 3.
18.0
>>> l = [2, 'string', [2, 4, (2, 0.0)]]
>>> l
[2, 'string', [2, 4, (2, 0.0)]]
>>> l = [2, 'string', 1.0]
>>> a = l
>>> a
[2, 'string', 1.0]
>>> l
[2, 'string', 1.0]
>>> l[2] = 5.0
>>> l
[2, 'string', 5.0]
>>> a
[2, 'string', 5.0]
>>> a[1]
'string'
>>> a[0:2]
[2, 'string']
>>> a[0:3]
[2, 'string', 5.0]
>>> b = a[0:3]
>>> b[1] = None
>>> b
[2, None, 5.0]
>>> a
[2, 'string', 5.0]
>>> a[0:len(a)]
[2, 'string', 5.0]
>>> a[:]
[2, 'string', 5.0]
>>> a[:1]
[2]
>>> a[:2]
[2, 'string']
>>> 
