new_data = {'key' : 'value', ('key', 2): ['value', 2.0]}

staff = { 'Joe' : [6, 8.022, 6.01, 18.03],
          'Paola': [8, 8.012, 8.022],
          'Analia': [8, 8.01, 8.02]
          }

def inc(j):
    return j + 1

def func_to_list(func, l):
    for i in xrange(len(l)):
        l[i] = func(l[i])

class hero: # No physical meaning
    def __init__(self, power):
        self.power = power

    def response(self, attack):
        return attack * self.power

class robotic_hero(hero):
    def __init__(self, height):
        self.height = height
        self.power = 1
        self.weight = height * 50

