import  matplotlib.pyplot as plt
class RK4(object):
    """
    from https://github.com/sbillaudelle/runge-kutta
    """

    def __init__(self, *functions):

        """
        Initialize a RK4 solver.
        :param functions: The functions to solve.
        """

        self.f = functions
        self.t = 0


    def solve(self, y, h, n):

        """
        Solve the system ODEs.
        :param y: A list of starting values.
        :param h: Step size.
        :param n: Endpoint.
        """

        t = []
        res = []
        for i in y:
            res.append([])

        while self.t <= n and h != 0:
            t.append(self.t)
            y = self._solve(y, self.t, h)
            for c, i in enumerate(y):
                res[c].append(i)

            self.t += h

            if self.t + h > n:
                h = n - self.t

        return t, res


    def _solve(self, y, t, h):

        functions = self.f

        k1 = []
        for f in functions:
            k1.append(h * f(t, *y))

        k2 = []
        for f in functions:
            k2.append(h * f(t + 0.5*h, *[y[i] + 0.5*h*k1[i] for i in range(0, len(y))]))

        k3 = []
        for f in functions:
            k3.append(h * f(t + 0.5*h, *[y[i] + 0.5*h*k2[i] for i in range(0, len(y))]))

        k4 = []
        for f in functions:
            k4.append(h * f(t + h, *[y[i] + h*k3[i] for i in range(0, len(y))]))

        return [y[i] + (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6.0 for i in range(0, len(y))]


k1, k2, k3 = 100, 600, 150
E0, S0, ES0, P0 = 1, 10, 0, 0 # initial value
h = 0.0001 # step size
n = 0.3 # endpoint 

f1 = lambda t, e, es, s, p: (k2+k3)*es - k1*e*s
f2 = lambda t, e, es, s, p: k1*e*s - (k2+k3)*es
f3 = lambda t, e, es, s, p: k2*es - k1*e*s
f4 = lambda t, e, es, s, p: k3*es
rk4 = RK4(f1,f2,f3,f4)
t, y = rk4.solve([E0,ES0,S0,P0],h,n)

for i in range(4):
    plt.subplot(3,2,i+1)
    plt.plot(t,y[i])
#plt.plot(t,y[0],t,y[1],t,y[2],t,y[3])
plt.subplot(3,2,5)
plt.plot(y[2],[val*k3 for val in y[1]])
plt.show()