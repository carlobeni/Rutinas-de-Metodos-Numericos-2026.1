import numpy as np
import os
os.system('cls')
x=np.array(([5,8,12,12.7]),dtype=float)
y=np.array(([104.2,140.2,181.7,180]),dtype=float)

n=len(x)
p=np.poly1d([1,-x[0]])
P=np.poly1d([y[0]])
for i in range(1,n):
 a=(y[i]-P(x[i]))/p(x[i])
 P=np.polyadd(P,a*p)
 p=np.polymul(p,np.poly1d([1,-x[i]]))
#print(np.array((P),dtype=float))
print(P)








