import numpy as np
import os
os.system('cls')
x=[5,8,12,12.7]
y=[104.2,140.2,181.7,180]

n=len(x)
P=np.poly1d([0])
for i in range(n):
 a=np.delete(np.arange(n),i)
 p=np.poly1d([1,-x[a[0]]])
 for j in range(1,n-1):
  p=np.polymul(p,np.poly1d([1,-x[a[j]]]))
 P=np.polyadd(P,y[i]*p/p(x[i]))
print(P)
