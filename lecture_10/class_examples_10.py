def shiftList(l):
    for i in xrange(len(l)):
        if not type(l[i]) == type(1):
            raise TypeError('Bad arg:', l[i], 'Index:', i)
        l[i] = l[i] + 5

def incrElt(l, i):
    try:
        l[i] += 1
    except TypeError:
        print "You can't increment anything but numbers."
    except IndexError:
        print "The list isn't", i+1, 'elements long.'
    finally:
        print "Thanks for using this code."

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as error:
        print 'You can’t divide by zero.', error.message
    else:
        print 'Result is:', result
    finally:
        print 'Thanks for choosing ESG functions.'

class ExplosionError(Exception):
	def __init__(self, capacitor, voltage):
		self.capacitor = capacitor
		self.voltage = voltage
		self.msg = 'You blew out capacitor ' + \
                           str(capacitor) + \
                           ' by applying a voltage of ' + \
                           str(voltage) + \
                           ' to it.'

Questionable_condition = 9 > 10
assert Questionable_condition

a = range(5)
shiftList(a)
a = a + ['kooky']
incrElt(a, 2)
incrElt(a, 5)
incrElt(a, 6)
divide(5, 6)
divide(4, 0)


