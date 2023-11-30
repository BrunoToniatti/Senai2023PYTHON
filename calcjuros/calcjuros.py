# Calculo de juros simples

#Entrada
capital = float(input('Quanto é a capital: '))
taxa = float(input('Qual o valora da taxa: '))
prazo = int(input('Qual o prazo final: '))

#Processamento
juros = float((capital*taxa*prazo)/ 100)

#Saída
print("O juros final será de {}".format(juros))