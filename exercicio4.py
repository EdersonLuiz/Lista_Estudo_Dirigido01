salario = float ( input ("Digite seu salário: R$ "))
porcentagem = float ( input ("Porcentagem de aumento: "))

print ("Você teve um aumento de: R$", salario * porcentagem / 100)
print ("Seu salário agora é: R$",(salario + (salario * porcentagem / 100)))