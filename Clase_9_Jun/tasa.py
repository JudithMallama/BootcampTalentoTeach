# Datos proporcionados
monto_prestamo = 70000000  # en pesos
tasa_interes_anual = 17.03 / 100  # tasa de interés anual en porcentaje
plazo_anos = 4  # plazo del préstamo en años

# Convertir la tasa de interés anual a mensual
tasa_interes_mensual = tasa_interes_anual / 12

# Número total de cuotas (plazo en meses)
numero_cuotas = plazo_anos * 12

# Aplicar la fórmula de amortización
cuota_mensual = monto_prestamo * (tasa_interes_mensual * (1 + tasa_interes_mensual) ** numero_cuotas) / ((1 + tasa_interes_mensual) ** numero_cuotas - 1)

print(f"La cuota mensual es: ${cuota_mensual:,.2f}")