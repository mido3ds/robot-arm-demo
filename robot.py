import math, _draw

class Robot:
    def __init__(self, **kwargs):
        self.conf = kwargs

        if 'q' not in kwargs:
            self._compute_q()
        else:
            self._compute_ab()
            self._compute_theta()


    def draw(self): 
        _draw.draw(self)

    def _compute_theta(self):
        ''' theta = q1 + q2 + q3 + q4 + .. '''
        self.conf['theta'] = sum(self.conf['q'])

    def _compute_ab(self):
        ''' compute missing a, b from l and q '''

        self.a = self._compute_part_ab(0, 0, math.cos)
        self.b = self._compute_part_ab(0, 0, math.sin)

    def _compute_part_ab(self, i, q_sum, func):
        ''' compute part of equation recursivly, take func (sin or cos) to apply '''

        # stop when you finish summing all q
        if i == len(self.conf['q']): return 0

        # update the whole sum with current q
        q_sum += self.conf['q'][i]

        this_part = self.conf['q'][i] * func(q_sum)
        next_part = self._compute_part_ab(i + 1, q_sum, func)

        return this_part + next_part

    def _compute_q(self):
        ''' compute missing q from a and b '''
        pass

def _alpha(l1, l2, r):
    return math.acos((l1 ** 2 + r ** 2 - l2 ** 2) / 2 * l1 * r)

def _hypotenuse(a, b):
    ''' return length of hypotenuse in right angle '''
    return math.sqrt(a ** 2 + b ** 2)        