################RUTINA020##########################
m=len(y0)
a=np.hstack((np.zeros((m-1,1)),np.eye((m-1))))
A=lambda x:np.vstack((a,np.array(([...]),dtype=float)))
B=lambda x:np.vstack((np.zeros((m-1,1)),np.array(([...]),dtype=float)))
x=x0
for i in range(n):
    dy=A(x)@y0+B(x)
    y=y0+h*dy
    y0=y.copy()
    x+=h
