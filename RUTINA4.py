################RUTINA004##########################
for i in range(n):
 c=(a+b)/2
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