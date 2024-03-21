from datetime import datetime

class Identificar:

    def __init__(self):

        # Ponto de corte
        self.dias_abastecimento = 1

        # Configuração o sistema fuzzy:



    def calcular(self, data, ultima_entrada, proxima_venda, proxima_entrada):


        # Verifica se a próxima venda ocorre apenas após a próxima entrada (ou no mesmo dia)
        if proxima_venda >= proxima_entrada:

            # Existe ruptura (RUPTURA = 1)
            return 1
        
        # Caso a próxima venda ocorra antes da próxima entrada
        else:

            # Calcula dias a partir da última entrada
            dias_ultima_entrada = (corrigir_data(data) - corrigir_data(ultima_entrada)).days
            
            # Verifica se está dentro do prazo de abastecimento definido no início da classe
            if dias_ultima_entrada <= self.dias_abastecimento:

                # Existe ruptura (RUPTURA = 1)
                return 1
        
        # Caso nenhuma das condições seja atendida: não há ruptura (RUPTURA = 0)
        return 0

# Transforma string em data (yyyy-mm-dd)
def corrigir_data(data):

    return datetime.strptime(str(data), "%Y-%m-%d")