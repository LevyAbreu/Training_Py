tempo_viagem = int(input())
velocidade_media = int(input())

distancia = tempo_viagem * velocidade_media

consumo_medio = 12

litros_necessarios = distancia / consumo_medio

print("{:.3f}".format(litros_necessarios))
