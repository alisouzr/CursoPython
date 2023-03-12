"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
  <- Contagem de complexidade (ruim)
Varável é para deixar seu códio mais fácil de ler
"""

velocidade = 61  # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60   # velocidade máxima do radar1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_car_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
  local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_car_passou_radar_1

if velocidade > RADAR_1:
    print(f'Seu carro passou da velocidade do Radar 1')