    # Paso 1: Definir el valor actual del Euro y Dolar con respecto al Peso Mexicano

tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

    # Paso 2: Solicitar al usuario el tipo de conversión que desea realizar (Euro a Mex o Dolar a Mex)

tipo_conversion= input("Ingrese la moneda de origen para la conversión (EUR/USD): ")
    # Paso 3: Solicitar al usuario el monto a convertir
monto_a_convertir= float(input("Ingrese el monto a convertir: "))

    # Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente
if tipo_conversion.upper()== "EUR":
    resultado= monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es:", resultado)
elif tipo_conversion.upper() == "USD": 
    resultado= monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es:", resultado)
else: 
    print("No está disponible este tipo de conversión actualmente.")
