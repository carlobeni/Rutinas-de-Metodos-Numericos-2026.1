################RUTINA009##########################
for i in range(m):
    F = sistema(P0)
    J = jacob_sist(P0)
    deltaP = jnp.linalg.solve(J, -F)
    P = P0 + deltaP
    err = jnp.linalg.norm(deltaP)
    relerr = err / jnp.linalg.norm(P)
    f_norm = jnp.linalg.norm(F)
    if (err < tol) or (relerr < tol) or (f_norm < tol):
        P0 = P
        break
    P0 = P
