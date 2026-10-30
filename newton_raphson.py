import math

def f(x):
    return x - math.exp(-x)

def df(x):
    return 1 + math.exp(-x)

def newton_raphson(x0, tol=0.001, max_iter=50):
    print(f"{'i':>2} | {'x_i':>10} | {'error':>10}")
    print("-" * 28)
    print(f"{0:>2} | {x0:>10.6f} | {'-':>10}")
    x_prev = x0
    for i in range(1, max_iter + 1):
        x_new = x_prev - f(x_prev) / df(x_prev)
        error = abs(x_new - x_prev)
        print(f"{i:>2} | {x_new:>10.6f} | {error:>10.6f}")
        if error < tol:
            return x_new
        x_prev = x_new
    raise RuntimeError("No convergió")

raiz = newton_raphson(x0=0.5)
print(f"\nRaíz aproximada: {raiz:.6f}")

# Verificación: x debe ser casi igual a e^(-x)
print(f"Verificación -> x = {raiz:.6f} | e^(-x) = {math.exp(-raiz):.6f}")
print(f"f(raíz) = {f(raiz):.2e}")
