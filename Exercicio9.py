cigarros_por_dia = int (input("Digite a quantidade de cigarros fumados por dia:"))
anos_fumados = int (input("Digite quantos anos você fuma:"))

tempo_perdido_dia = (cigarros_por_dia * 10)
tempo_perdido_ano = ((anos_fumados * 365) * tempo_perdido_dia) / (24 * 60)

print ("Você perdeu {0:3.1f}".format (tempo_perdido_ano),"dias de vida")