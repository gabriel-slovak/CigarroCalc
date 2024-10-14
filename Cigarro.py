tempofumante = int(input("Insira quantos anos vc fuma: "))
CigarroDia = int(input("Quantos cigarros fuma por dia: "))
valorCarteira = float(input("Quanto custa a carteira do cigarro: "))


valor = (tempofumante*365) / 20
resultado = valor*valorCarteira

print("Seu gasto em cigarros foi de",resultado)
