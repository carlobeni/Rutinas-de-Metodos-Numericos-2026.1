################RUTINA009##########################
for i in range(m):
    F=sistema(P0)
    J=jacob_sist(P0)
    deltaP=jnp.linalg.solve(J.reshape(n,n),-F)
    P=P0+deltaP
    err=jnp.linalg.norm(P-P0)
    relerr=err/jnp.linalg.norm(P)
    if tol>err or tol>relerr:
        break
    else:
        P0=P.copy()
