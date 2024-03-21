# Algoritmos de Identificação de Ruptura

Algoritmos desenvolvidos como parte da Dissertação de Mestrado: "*IDENTIFICAÇÃO DE RUPTURAS DE ESTOQUE NO VAREJO ALIMENTAR ATRAVÉS DE TÉCNICAS DE SOFT COMPUTING*"

O primeiro (```Identification.py```) faz a identificação prévia dos dados (rotulagem) com base em dados passados e futuros. Desenvolvido apenas a partir de regras de negócio estabelecidas.

O segundo (```FuzzyLogic.py```) faz a identificação preditiva, utilizando apenas dados passados. Desenvolvido utilizando técnicas de *soft computing*, especificamente *fuzzy logic*.


## Identification.py
Idenfificação da ruputura baseada nos dados passados.  
Verifica se um item esteve em estado de ruptura em um determinado período baseado em seu reinício de vendas ou prazo de reposição (0 = Não e 1 = Sim).  
Variáveis de entrada (data atual, data da última entrada, data da próxima venda e data da próxima entrada) no formato "yyyy-mm-dd"

Teste através do arquivo ```ExecutarIdentificacao.py```


## FuzzyLogic.py
Utiliza lógica difusa para o cálculo da probabilidade e um ponto de corte para definição do status (0 = Não e 1 = Sim).  
Definições iniciais do algoritmo estão somente na inicilização. Inclusive ponto de corte.  
Uma vez inicializado, os parâmetros de entrada (variáveis P1, P2, P3 e P4) são informados no método "calcular" que retorna o status de identificação de acordo com o ponto de corte.

Teste através do arquivo ```ExecutarAlgoritmo.py```




