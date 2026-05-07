################RUTINA016##########################
h=(b-a)/n
A=0
y=f(np.linspace(a,b,n+1))
k=0
while(k<n):
    A+=(3*h/8)*(y[k]+3*y[k+1]+3*y[k+2]+y[k+3])
    k+=3
