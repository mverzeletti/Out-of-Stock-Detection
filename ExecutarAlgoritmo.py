from Algoritmo_Fuzzy import Ruptura

# Inicializa algoritmo
RUPTURA = Ruptura()

# Variáveis de entrada
P1 = 0.5
P2 = 0.5
P3 = 0.5
P4 = 0.5

# Calcula e imprime o status
status = RUPTURA.calcular(P1, P2, P3, P4)
print(f"Para as probabilidades definidas:")
print(f"P1 = {P1}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print("Temos:")
print(f"Ruptura = {status}\n")

# Variáveis de entrada
P1 = 0.9
P2 = 0.9
P3 = 0.9
P4 = 0.9

# Calcula e imprime o status
status = RUPTURA.calcular(P1, P2, P3, P4)
print(f"Para as probabilidades definidas:")
print(f"P1 = {P1}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print("Temos:")
print(f"Ruptura = {status}\n")


# Variáveis de entrada
P1 = 0.64259343
P2 = 0.64259343
P3 = 0.83644157
P4 = 0.65752598

# Calcula e imprime o status
status = RUPTURA.calcular(P1, P2, P3, P4)
print(f"Para as probabilidades definidas:")
print(f"P1 = {P1}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print("Temos:")
print(f"Ruptura = {status}\n")

# Variáveis de entrada
P1 = 0.98729024
P2 = 0.98729024
P3 = 0.99999878
P4 = 0.32536698

# Calcula e imprime o status
status = RUPTURA.calcular(P1, P2, P3, P4)
print(f"Para as probabilidades definidas:")
print(f"P1 = {P1}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print(f"P2 = {P2}")
print("Temos:")
print(f"Ruptura = {status}\n")
