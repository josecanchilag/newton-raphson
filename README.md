# Método de Newton-Raphson

Aproximación de la solución de la ecuación x = e^(-x).

## Planteamiento
f(x) = x - e^(-x), f'(x) = 1 + e^(-x), x0 = 0.5, tolerancia 0.001.

## Resultado
x ≈ 0.5671 (obtenido en 2 iteraciones)

| i | x_i | error |
|---|-----|-------|
| 0 | 0.500000 | - |
| 1 | 0.566311 | 0.066311 |
| 2 | 0.567143 | 0.000832 |

## Gráfica
![Gráfica en GeoGebra](gr%C3%A1fica_geogebra.png)

## Uso
    python newton_raphson.py
