#AND en este ambas condiciones tienen que ser True para que devuelva True

resultado = True & True #Devuelve True
resultado2 = False & True #Devuelve False
resultado3 = True & False #Devuelve False
resultado4 = False & False #Devuelve False

#OR en este ambas condiciones tienen que ser False para que devuelva False, en caso contrario devolverá True

resultado5 = True | True #Devuelve True
resultado6 = False | True #Devuelve True
resultado7 = True | False #Devuelve True
resultado8 = False | False #Devuelve False

#NOT esta es la negación, si le damos un valor True lo vuelve False y viceversa

resultado9 = not 2 > 49 #Devuelve False
resultado10 = not False #Devuelve True