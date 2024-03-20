# Bibliotecas necessarias
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


class Ruptura:

    def __init__(self):

        # Ponto de corte
        self.m = 0.85

        # Criar conjuntos fuzzy para as variáveis de entrada e saída
        # P1 : probabilidade de ruptura calculada pela ocorrência de venda nula
        # P2 : probabilidade de ruptura calculada pela sequência de venda nula
        # P3 : probabilidade de ruptura calculada pela venda acumulada nos últimos 7 dias
        # P4 : probabilidade de ruptura calculada pelo saldo a partir da última entrada
        # R : probabilidade de ruptura a partir da execução do algoritmo
        P1 = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'P1')
        P2 = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'P2')
        P3 = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'P3')
        P4 = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'P4')
        R = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'R')

        # Funções de pertinência
        P1['Baixa'] = fuzz.trimf(P1.universe, [0, 0.34, 0.68])
        P1['Media'] = fuzz.trimf(P1.universe, [0.61,0.7,0.79])
        P1['Alta'] = fuzz.trimf(P1.universe, [0.72,0.85, 1])

        P2['Baixa'] = fuzz.trimf(P2.universe, [0, 0.425, 0.85])
        P2['Media'] = fuzz.trimf(P2.universe, [0.78,0.89,1])
        P2['Alta'] = fuzz.trimf(P2.universe, [0.96,0.98, 1])

        P3['Baixa'] = fuzz.trimf(P3.universe, [0, 0.40, 0.80])
        P3['Media'] = fuzz.trimf(P3.universe, [0.75,0.865,0.98])
        P3['Alta'] = fuzz.trimf(P3.universe, [0.89,0.945, 1])

        P4['Baixa'] = fuzz.trimf(P4.universe, [0, 0.14, 0.28])
        P4['Media'] = fuzz.trimf(P4.universe, [0.19,0.395,0.60])
        P4['Alta'] = fuzz.trimf(P4.universe, [0.51,0.755, 1])

        R['Baixa'] = fuzz.trimf(R.universe, [0, 0.25, 0.5])
        R['Media'] = fuzz.trimf(R.universe, [0.45,0.625,0.8])
        R['Alta'] = fuzz.trimf(R.universe, [0.75,0.875, 1])

        # Definição das regras de pertinência definidas de acordo com o negócio
        # Definidas de forma a considerar a importância das variáveis de entrada
        regra01 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Alta"] & P4["Alta"], R["Alta"])
        regra02 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Alta"] & P4["Media"], R["Alta"])
        regra03 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Alta"] & P4["Baixa"], R["Alta"])
        regra04 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Media"] & P4["Alta"], R["Alta"])
        regra05 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Media"] & P4["Media"], R["Alta"])
        regra06 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Media"] & P4["Baixa"], R["Alta"])
        regra07 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Baixa"] & P4["Alta"], R["Alta"])
        regra08 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Baixa"] & P4["Media"], R["Alta"])
        regra09 = ctrl.Rule(P1["Alta"] & P2["Alta"] & P3["Baixa"] & P4["Baixa"], R["Alta"])
        regra10 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Alta"] & P4["Alta"], R["Alta"])
        regra11 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Alta"] & P4["Media"], R["Alta"])
        regra12 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Alta"] & P4["Baixa"], R["Alta"])
        regra13 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Media"] & P4["Alta"], R["Alta"])
        regra14 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Media"] & P4["Media"], R["Alta"])
        regra15 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Media"] & P4["Baixa"], R["Alta"])
        regra16 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Baixa"] & P4["Alta"], R["Alta"])
        regra17 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Baixa"] & P4["Media"], R["Alta"])
        regra18 = ctrl.Rule(P1["Alta"] & P2["Media"] & P3["Baixa"] & P4["Baixa"], R["Alta"])
        regra19 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Alta"] & P4["Alta"], R["Media"])
        regra20 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Alta"] & P4["Media"], R["Media"])
        regra21 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Alta"] & P4["Baixa"], R["Media"])
        regra22 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Media"] & P4["Alta"], R["Media"])
        regra23 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Media"] & P4["Media"], R["Media"])
        regra24 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Media"] & P4["Baixa"], R["Media"])
        regra25 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Baixa"] & P4["Alta"], R["Media"])
        regra26 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Baixa"] & P4["Media"], R["Media"])
        regra27 = ctrl.Rule(P1["Alta"] & P2["Baixa"] & P3["Baixa"] & P4["Baixa"], R["Media"])
        regra28 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Alta"] & P4["Alta"], R["Alta"])
        regra29 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Alta"] & P4["Media"], R["Alta"])
        regra30 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Alta"] & P4["Baixa"], R["Alta"])
        regra31 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Media"] & P4["Alta"], R["Alta"])
        regra32 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Media"] & P4["Media"], R["Alta"])
        regra33 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Media"] & P4["Baixa"], R["Alta"])
        regra34 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Baixa"] & P4["Alta"], R["Alta"])
        regra35 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Baixa"] & P4["Media"], R["Alta"])
        regra36 = ctrl.Rule(P1["Media"] & P2["Alta"] & P3["Baixa"] & P4["Baixa"], R["Media"])
        regra37 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Alta"] & P4["Alta"], R["Alta"])
        regra38 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Alta"] & P4["Media"], R["Media"])
        regra39 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Alta"] & P4["Baixa"], R["Media"])
        regra40 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Media"] & P4["Alta"], R["Media"])
        regra41 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Media"] & P4["Media"], R["Media"])
        regra42 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Media"] & P4["Baixa"], R["Media"])
        regra43 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Baixa"] & P4["Alta"], R["Media"])
        regra44 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Baixa"] & P4["Media"], R["Media"])
        regra45 = ctrl.Rule(P1["Media"] & P2["Media"] & P3["Baixa"] & P4["Baixa"], R["Media"])
        regra46 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Alta"] & P4["Alta"], R["Media"])
        regra47 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Alta"] & P4["Media"], R["Baixa"])
        regra48 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Alta"] & P4["Baixa"], R["Baixa"])
        regra49 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Media"] & P4["Alta"], R["Baixa"])
        regra50 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Media"] & P4["Media"], R["Baixa"])
        regra51 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Media"] & P4["Baixa"], R["Baixa"])
        regra52 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Baixa"] & P4["Alta"], R["Baixa"])
        regra53 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Baixa"] & P4["Media"], R["Baixa"])
        regra54 = ctrl.Rule(P1["Media"] & P2["Baixa"] & P3["Baixa"] & P4["Baixa"], R["Baixa"])
        regra55 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Alta"] & P4["Alta"], R["Alta"])
        regra56 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Alta"] & P4["Media"], R["Alta"])
        regra57 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Alta"] & P4["Baixa"], R["Alta"])
        regra58 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Media"] & P4["Alta"], R["Media"])
        regra59 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Media"] & P4["Media"], R["Media"])
        regra60 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Media"] & P4["Baixa"], R["Media"])
        regra61 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Baixa"] & P4["Alta"], R["Media"])
        regra62 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Baixa"] & P4["Media"], R["Media"])
        regra63 = ctrl.Rule(P1["Baixa"] & P2["Alta"] & P3["Baixa"] & P4["Baixa"], R["Media"])
        regra64 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Alta"] & P4["Alta"], R["Alta"])
        regra65 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Alta"] & P4["Media"], R["Alta"])
        regra66 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Alta"] & P4["Baixa"], R["Media"])
        regra67 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Media"] & P4["Alta"], R["Media"])
        regra68 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Media"] & P4["Media"], R["Media"])
        regra69 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Media"] & P4["Baixa"], R["Baixa"])
        regra70 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Baixa"] & P4["Alta"], R["Baixa"])
        regra71 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Baixa"] & P4["Media"], R["Baixa"])
        regra72 = ctrl.Rule(P1["Baixa"] & P2["Media"] & P3["Baixa"] & P4["Baixa"], R["Baixa"])
        regra73 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Alta"] & P4["Alta"], R["Baixa"])
        regra74 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Alta"] & P4["Media"], R["Baixa"])
        regra75 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Alta"] & P4["Baixa"], R["Baixa"])
        regra76 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Media"] & P4["Alta"], R["Baixa"])
        regra77 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Media"] & P4["Media"], R["Baixa"])
        regra78 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Media"] & P4["Baixa"], R["Baixa"])
        regra79 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Baixa"] & P4["Alta"], R["Baixa"])
        regra80 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Baixa"] & P4["Media"], R["Baixa"])
        regra81 = ctrl.Rule(P1["Baixa"] & P2["Baixa"] & P3["Baixa"] & P4["Baixa"], R["Baixa"])

        # Cria objeto com todas as regras definidas
        regras = []
        regras.append(regra01)
        regras.append(regra02)
        regras.append(regra03)
        regras.append(regra04)
        regras.append(regra05)
        regras.append(regra06)
        regras.append(regra07)
        regras.append(regra08)
        regras.append(regra09)
        regras.append(regra10)
        regras.append(regra11)
        regras.append(regra12)
        regras.append(regra13)
        regras.append(regra14)
        regras.append(regra15)
        regras.append(regra16)
        regras.append(regra17)
        regras.append(regra18)
        regras.append(regra19)
        regras.append(regra20)
        regras.append(regra21)
        regras.append(regra22)
        regras.append(regra23)
        regras.append(regra24)
        regras.append(regra25)
        regras.append(regra26)
        regras.append(regra27)
        regras.append(regra28)
        regras.append(regra29)
        regras.append(regra30)
        regras.append(regra31)
        regras.append(regra32)
        regras.append(regra33)
        regras.append(regra34)
        regras.append(regra35)
        regras.append(regra36)
        regras.append(regra37)
        regras.append(regra38)
        regras.append(regra39)
        regras.append(regra40)
        regras.append(regra41)
        regras.append(regra42)
        regras.append(regra43)
        regras.append(regra44)
        regras.append(regra45)
        regras.append(regra46)
        regras.append(regra47)
        regras.append(regra48)
        regras.append(regra49)
        regras.append(regra50)
        regras.append(regra51)
        regras.append(regra52)
        regras.append(regra53)
        regras.append(regra54)
        regras.append(regra55)
        regras.append(regra56)
        regras.append(regra57)
        regras.append(regra58)
        regras.append(regra59)
        regras.append(regra60)
        regras.append(regra61)
        regras.append(regra62)
        regras.append(regra63)
        regras.append(regra64)
        regras.append(regra65)
        regras.append(regra66)
        regras.append(regra67)
        regras.append(regra68)
        regras.append(regra69)
        regras.append(regra70)
        regras.append(regra71)
        regras.append(regra72)
        regras.append(regra73)
        regras.append(regra74)
        regras.append(regra75)
        regras.append(regra76)
        regras.append(regra77)
        regras.append(regra78)
        regras.append(regra79)
        regras.append(regra80)
        regras.append(regra81)

        # Cria sistema de controle fuzzy a partir das regras estabelecidas
        sistema_ctrl = ctrl.ControlSystem(regras)
        self.sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

    def calcular(self, p1, p2, p3, p4):

            self.sistema.input["P1"] = corrigir(p1)
            self.sistema.input["P2"] = corrigir(p2)
            self.sistema.input["P3"] = corrigir(p3)
            self.sistema.input["P4"] = corrigir(p4)

            # Computar o resultado
            self.sistema.compute()


            if self.sistema.output["R"] > self.m:
                
                return 1
            
            else:
                
                return 0
             
# Correção para valores fora do intervalo
def corrigir(valor):
    if valor == 0:

        return 0.0000001
    if valor == 1:

        return 0.9999999
    return valor
