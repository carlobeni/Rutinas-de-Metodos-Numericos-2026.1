#df = grad(f) # jax reconoce automaticamente que debe derivar respecto al parámetro de f definido previamente Ej: def f(r) # deriva respecto a r

################RUTINA007##########################
for i in range(n):
 p=g(p0)
 err=np.abs(p-p0)
 relerr=np.abs(err/p)
 if tol>err or tol>relerr or tol>np.abs(f(p)):
   break
 p0=p