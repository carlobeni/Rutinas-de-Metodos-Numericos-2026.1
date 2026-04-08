A = 0.0
h = (b - a) / n
for xi in np.arange(a, b - 2*h, 2*h):
    A = A + (h/3) * (f(xi) + 4*f(xi + h) + f(xi + 2*h))
print(A)
