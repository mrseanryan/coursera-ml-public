import sympy

J, w = sympy.symbols('J,w')

J = w ** 2

print("=== Derivation ===")

dJ_dw = sympy.diff(J,w)
print(f"diff of 'J = w^2' = {dJ_dw}")

result = dJ_dw.subs([(w,2)])
print(f"dJ_dw(w = 2) = {result}")

J = w ** 3
dJ_dw = sympy.diff(J,w)
print(f"diff of 'J = w^3' = {dJ_dw}")

print("=== Integration ===")

print(f"int of '3w^2' = {sympy.integrate(dJ_dw)}")

print("=== ===")
print("Deriving via arithmetic:")
J = w**2
print(J)
J = (3)**2
epsilon = 0.00001
J_epsilon = (3 + epsilon)**2
k = (J_epsilon - J)/epsilon
print(f"w = 3 -> J = {J}, J_epsilon = {J_epsilon}, dJ_dw ~= k = {k} ")

print("Deriving via symbols:")
J = w**2
dJ_dw = sympy.diff(J,w)
print(dJ_dw)
print(f"w = 3 -> dJ_dw = {dJ_dw.subs([(w, 3)])} which ~= k above")
