import math

metros_quadrados = int ( input("Metros quadrados da área a ser pintada: "))

lata = 18
galão = 3.6
vlata = 80
vgalão = 25

cobertura = metros_quadrados / 6
print ("Quantidade de tinta necessária: {0:3.1f}".format (cobertura), "litros.")

#Situação A: Comprar apenas latas de 18 litros.

latas_necessárias = math.ceil(cobertura / lata)
print ("Você precisará de",latas_necessárias, "latas.")
print ("e pagará R$", latas_necessárias * vlata)

print ("===*====" * 10)

#Situação B: Comprar apenas galões de 3.6 litros.

galões_necessários = math.ceil(cobertura / galão)
print ("Você precisará de", galões_necessários, "galões.")
print ("e pagará R$", galões_necessários * vgalão)

print ("===*====" * 10)

#Situação C: misturar latas e galões.

latas_necessárias = int (cobertura / lata)
falta = cobertura % 18
galões_necessários = math.ceil(falta / galão)

print("São necessárias", latas_necessárias, "latas")
print ("e", galões_necessários, "galões")
print ("e pagará R$", (latas_necessárias * vlata) + (galões_necessários * vgalão))