from Identification import Identificar


#### Restrições
# Datas no formato: yyyy-mm-dd
# ultima_entrada <= data < proxima_entrada <= proxima_venda

# Inicializa identificação
RUPTURA = Identificar()

# Variáveis de entrada
data = "2022-06-01"
ultima_entrada = "2022-05-25"
proxima_venda =  "2022-06-18"
proxima_entrada = "2022-06-18"

# Calcula e imprime o status
status = RUPTURA.calcular(data, ultima_entrada, proxima_venda, proxima_entrada)
print(f"Para a situação definida:")
print(f"Data = {data}")
print(f"Última entrada = {ultima_entrada}")
print(f"Próxima venda = {proxima_venda}")
print(f"Próxima entrada = {proxima_entrada}")
print("Temos:")
print(f"Ruptura = {status}\n")

# Variáveis de entrada
data = "2022-06-01"
ultima_entrada = "2022-05-25"
proxima_venda =  "2022-06-18"
proxima_entrada = "2022-06-19"

# Calcula e imprime o status
status = RUPTURA.calcular(data, ultima_entrada, proxima_venda, proxima_entrada)
print(f"Para a situação definida:")
print(f"Data = {data}")
print(f"Última entrada = {ultima_entrada}")
print(f"Próxima venda = {proxima_venda}")
print(f"Próxima entrada = {proxima_entrada}")
print("Temos:")
print(f"Ruptura = {status}\n")

# Variáveis de entrada
data = "2022-06-01"
ultima_entrada = "2022-05-31"
proxima_venda =  "2022-06-18"
proxima_entrada = "2022-06-19"

# Calcula e imprime o status
status = RUPTURA.calcular(data, ultima_entrada, proxima_venda, proxima_entrada)
print(f"Para a situação definida:")
print(f"Data = {data}")
print(f"Última entrada = {ultima_entrada}")
print(f"Próxima venda = {proxima_venda}")
print(f"Próxima entrada = {proxima_entrada}")
print("Temos:")
print(f"Ruptura = {status}\n")