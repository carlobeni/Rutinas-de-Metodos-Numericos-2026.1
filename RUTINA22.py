################RUTINA022##########################
m=len(y0)
a=np.hstack((np.zeros((m-1,1)),np.eye((m-1))))
A=lambda x:np.vstack((a,np.array(([...]),dtype=float)))
B=lambda x:np.vstack((np.zeros((m-1,1)),np.array(([...]),dtype=float)))
x=x0
for i in range(n):
    dy1=A(x)@y0+B(x)
    y1=y0+h*dy1
    x+=h
    dy2=A(x)@y1+B(x)
    y=y0+(h/2)*(dy1+dy2)
    y0=y.copy()
