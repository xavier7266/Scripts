import numpy as np
from scipy.optimize import curve_fit

# Datos experimentales para 48 horas
concentraciones = np.array([64, 32, 16, 8, 4])  # en ppm
mortalidad = np.array([0.98, 0.9784, 0.9610, 0.448, 0.2243])  # en proporción

# Transformar concentraciones a log10
log_concentraciones = np.log10(concentraciones)

# Definir el modelo logístico
def modelo_logistico(x, a, b):
    return 1 / (1 + np.exp(-(a + b * x)))

# Ajustar el modelo a los datos
parametros, _ = curve_fit(modelo_logistico, log_concentraciones, mortalidad)

# Extraer los parámetros a y b
a, b = parametros
print(f"Parámetros ajustados: a = {a:.3f}, b = {b:.3f}")

# Calcular la LC50
LC50 = 10**(-a / b)
print(f"LC50 (48 horas) = {LC50:.3f} ppm")