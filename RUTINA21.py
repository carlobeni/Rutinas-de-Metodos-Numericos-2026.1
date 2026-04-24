################RUTINA021##########################
########MANUAL (Version con grad de jax, from jax import grad)##########
def dy(x, y):
    return ...

def d2y(x, y):
    # (dy)'_x + (dy)'_y * dy
    return grad(dy, argnums=0)(x, y) + grad(dy, argnums=1)(x, y) * dy(x, y)

def d3y(x, y):
    # (dy)'_x + (dy)'_y * dy
    return grad(d2y, argnums=0)(x, y) + grad(d2y, argnums=1)(x, y) * dy(x, y)

def d4y(x, y):
    # (dy)'_x + (dy)'_y * dy
    return grad(d3y, argnums=0)(x, y) + grad(d3y, argnums=1)(x, y) * dy(x, y)

def d5y(x, y):
    # (dy)'_x + (dy)'_y * dy
    return grad(d4y, argnums=0)(x, y) + grad(d4y, argnums=1)(x, y) * dy(x, y)



for i in range(0, n):
    f1  = dy(x0, y0)
    f2  = d2y(x0, y0)
    f3  = d3y(x0, y0)
    f4  = d4y(x0, y0)
    f5  = d5y(x0, y0)
    y1  = y0 + f1*h + f2/2 * h**2+(f3*h**3)/6+(f4*h**4)/24+(f5*h**5)/120
    x1  = x0 + h
    y0  = y1
    x0  = x1
    

###########GENERALIZADO (Version con sympy, import sympy as sp)##############
# x, y = sp.Symbol('x'), sp.Symbol('y')
df=[f]
for i in range(n):
    df.append(sp.diff(df[i],'x')+sp.diff(df[i],'y')*f)

R=np.array(([y0]),dtype=float)
x_=x0
y_=y0
for j in range(m):
    for i in range(n+1):
        y_+=df[i].subs({x:x_,y:y0})*h**(i+1)/math.factorial(i+1)
    x_+=h
    y0=y_
