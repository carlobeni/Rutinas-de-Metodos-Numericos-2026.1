################RUTINA014##########################
h=(b-a)/n
A=0
y=f(np.linspace(a,b,n+1))
k=0
while(k<n):
    A+=(h/2)*(y[k]+y[k+1])
    k+=1
