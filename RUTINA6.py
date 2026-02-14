#df = grad(f) # jax reconoce automaticamente que debe derivar respecto al parámetro de f definido previamente Ej: def f(r) # deriva respecto a r

################RUTINA006##########################
for i in range(n):
 p=p0-f(p0)/df(p0)
 err=jnp.abs(p-p0)
 relerr=jnp.abs(err/p)
 if tol>err or tol>relerr or tol>jnp.abs(f(p)):
   break
 p0=p
