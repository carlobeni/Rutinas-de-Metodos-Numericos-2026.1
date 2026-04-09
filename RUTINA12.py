################RUTINA012##########################
for i in range(n):
 a=np.delete(np.arange(n),i)
 p=np.poly1d([1,-x[a[0]]])
 for j in range(1,n-1):
  p=np.polymul(p,np.poly1d([1,-x[a[j]]]))
 P+=y[i]*p/p(x[i])
