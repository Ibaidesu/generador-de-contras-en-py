#!/usr/bin/env python

from random import choice

longitud = 99
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+0099"
print ("la contraseña generada es la siguiente")
p = ""
p = p.join([choice(valores) for i in range(longitud)])
print(p)

#!/generador de contraseñas seguras