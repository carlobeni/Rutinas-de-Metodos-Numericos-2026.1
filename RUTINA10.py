################RUTINA010##########################
y_pred = (K_opt[0] * x_data + K_opt[1]) ** (-2)
y_mean = jnp.mean(y_data)
yp_mean = jnp.mean(y_pred)
num = jnp.sum((y_data - y_mean) * (y_pred - yp_mean))
den = jnp.sqrt(
    jnp.sum((y_data - y_mean)**2) *
    jnp.sum((y_pred - yp_mean)**2)
)
r = num / den
