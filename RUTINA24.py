################RUTINA024##########################
m=len(y0)
a=np.hstack((np.zeros((m-1,1)),np.eye((m-1))))
A=lambda x:np.vstack((a,np.array(([...]),dtype=float)))
B=lambda x:np.vstack((np.zeros((m-1,1)),np.array(([...]),dtype=float)))
x1=x0+h
x2=x1+h
x3=x2+h
for i in range(n):
    dy1=A(x1)@y1+B(x1)
    dy2=A(x2)@y2+B(x2)
    dy3=A(x3)@y3+B(x3)
    
    p=y0+(4/3)*h*(2*dy1-dy2+2*dy3)
    x4=x3+h
    dy4=A(x4)@p+B(x4)
    
    y=y2+(h/3)*(dy2+4*dy3+dy4)
    
    y0=y1.copy()
    y1=y2.copy()
    y2=y3.copy()
    y3=y.copy()
    x1=x2
    x2=x3
    x3=x4
