################RUTINA015##########################
h=(b-a)/n
A=0
y=f(np.linspace(a,b,n+1))
k=0
while(k<n):
    A+=(h/3)*(y[k]+4*y[k+1]+y[k+2])
    k+=2
