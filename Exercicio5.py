vmercadoria = float (input("Digite o valor da mercadoria: "))
pdesconto = float (input("Digite o percentual de desconto: "))

print("Você ganhou R$", (vmercadoria * pdesconto / 100),"de desconto.")
print ("Valor a pagar: R$", vmercadoria - (vmercadoria * pdesconto / 100))