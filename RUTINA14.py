################RUTINA014##########################
A = 0.0
h = (b - a) / n
for xi in np.arange(a, b - h, h):
    A = A + (h/2) * (f(xi) + f(xi + h))
