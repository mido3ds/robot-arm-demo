import math

class Robot:
    def __init__(self, **kwargs):
        if 'q' in kwargs:
            self.q = [kwargs['q'], ]
        if 'l' in kwargs:
            self.l = kwargs['l']
        if 'a' in kwargs:
            self.a = kwargs['a']
        if 'b' in kwargs:
            self.b = kwargs['b']
        if 'theta' in kwargs:
            self.theta = kwargs['theta']

        if 'q' not in kwargs:
            self._compute_q()
        else:
            self._compute_ab()
            self._compute_theta()

    def _compute_theta(self):
        ''' theta = q1 + q2 + q3 + q4 + .. '''
        self.theta = sum(self.q[0])

    def _compute_ab(self):
        ''' compute missing a, b from l and q '''

        self.a = self._compute_part_ab(0, 0, math.cos)
        self.b = self._compute_part_ab(0, 0, math.sin)

    def _compute_part_ab(self, i, q_sum, func):
        ''' compute part of equation recursivly, take func (sin or cos) to apply '''

        # stop when you finish summing all q
        if i == len(self.q[0]): return 0

        # update the whole sum with current q
        q_sum += self.q[0][i]

        this_part = self.l[i] * func(q_sum)
        next_part = self._compute_part_ab(i + 1, q_sum, func)

        return this_part + next_part

    def _compute_q(self):
        ''' compute missing q from a, b and theta for less than 3 joints '''

        if len(self.l) == 3:
            a = self.a - self.l[2] * math.cos(self.theta)
            b = self.b - self.l[2] * math.sin(self.theta)
            self.q = self._compute_q_2joints(a, b)
            for i in range(2):
                self.q[i].append(self.theta - self.q[i][0] - self.q[i][1])
        else:
            a = self.a
            b = self.b
            self.q = self._compute_q_2joints(a, b)



    def _compute_q_2joints(self, a, b):
        ''' compute q for joints system '''
        r = _hypotenuse(a, b)
        alpha = _alpha(self.l[0], self.l[1], r)
        q1, q2 = [], []

        for q in (q1, q2):
            alpha = - alpha
            q.append(math.atan(b / a) - alpha)
            q.append((r * math.sin(alpha)) / (r * math.cos(alpha) - self.l[0]))

        return [q1, q2]


def _alpha(l1, l2, r):
    return math.acos((l1 ** 2 + r ** 2 - l2 ** 2) / 2 * l1 * r)

def _hypotenuse(a, b):
    ''' return length of hypotenuse in right angle '''
    return math.sqrt(a ** 2 + b ** 2)        