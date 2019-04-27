distancia = int ( input ("Digite a distância a ser percorrida em km:"))
velocidade = int ( input("Digite a velocidade média em km/h:"))

print ("Você chegará em seu destino em {0:3.1f}".format (distancia / velocidade),"horas")