################RUTINA016##########################
A = 0.0
h = (b - a) / n
for xi in np.arange(a, b - 3*h, 3*h):
    A = A + (3*h/8) * (f(xi) + 3*f(xi + h) + 3*f(xi + 2*h) + f(xi + 3*h))
