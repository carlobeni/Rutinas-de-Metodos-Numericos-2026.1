################RUTINA008##########################
for i in range(n):
 x2=(x1*f(x0)-x0*f(x1))/(f(x0)-f(x1))
 err=np.abs(x2-x1)
 relerr=np.abs(err/x2)
 if tol>err or tol>relerr or tol>np.abs(f(x2)):
   break
 x0=x1
 x1=x2