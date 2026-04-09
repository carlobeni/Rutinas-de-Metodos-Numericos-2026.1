################RUTINA013##########################
for i in range(1,n):
 a=(y[i]-P(x[i]))/p(x[i])
 P+=a*p
 p=np.polymul(p,np.poly1d([1,-x[i]]))
