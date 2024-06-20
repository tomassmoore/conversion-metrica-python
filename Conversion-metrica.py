
# Paso 1. Solicitar al usuario ingresar medidas en cm

medida_en_cm= float(input('Porfavor, ingrese las medidas del mueble en cm: '))  

# Paso 2. Convertir las medidas de cm a pulgadas

medida_en_pulgadas = medida_en_cm / 2.54

# Paso 3. Mostrar las medidas convertidas en pulgadas al usuario
   
print('Las medidas en pulgadas del mueble ingresado son: ', medida_en_pulgadas)