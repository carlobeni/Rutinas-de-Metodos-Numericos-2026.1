################RUTINA023##########################
m=len(y0)
a=np.hstack((np.zeros((m-1,1)),np.eye((m-1))))
A=lambda x:np.vstack((a,np.array(([...]),dtype=float)))
B=lambda x:np.vstack((np.zeros((m-1,1)),np.array(([...]),dtype=float)))
x=x0
for i in range(n):
    dy0=A(x)@y0+B(x)
    x+=h/2
    y1=y0+(h/2)*dy0
    dy1=A(x)@y1+B(x)

    y2=y0+(h/2)*dy1
    dy2=A(x)@y2+B(x)

    x+=h/2
    y3=y0+h*dy2
    dy3=A(x)@y3+B(x)

    y=y0+(h/6)*(dy0+2*dy1+2*dy2+dy3)
    y1=y.copy()
################
