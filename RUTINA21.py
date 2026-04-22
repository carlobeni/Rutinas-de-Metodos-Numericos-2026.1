################RUTINA021##########################
for i in range(1, 4):
    f1  = dy(x0, y0)
    f2  = d2y(x0, y0)
    y1  = y0 + f1*h + f2/2 * h**2
    x1  = x0 + h
    yr  = ...   # Valor real de la funcion                     
    err = abs(y1 - yr)
    f11 = dy(x1, y1)
    f21 = d2y(x1, y1)
    y0  = y1
    x0  = x1
