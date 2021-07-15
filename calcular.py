
cantidad = 'cantidad'
subtotal = 5 * cantidad
numero_cajas  = round(cantidad/4,0)
flete = numero_cajas*50
if (cantidad>1000):
    descuento=subtotal*0.15
else:
    if(cantidad>100):
        descuento=subtotal*0.05
    else:
        descuento=0

total=subtotal+flete-descuento
print ("El precio total a pagar es: "+total+"<br>")
print ("El monto por flete es: "+flete+"<br>")
print ("El descuento aplicado fue: "+descuento)

