################RUTINA005##########################
for i in range(n):
 c=(b*f(a)-a*f(b))/(f(a)-f(b))
 err=np.abs(c0-c)
 relerr=np.abs(err/c)
 if tol>err or tol>relerr or tol>np.abs(f(c)):
   break
 else:
   if f(a)*f(c)<0:
     b=c
   else:
     a=c
 c0=c