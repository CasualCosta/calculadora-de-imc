print("Seja bem-vindo(ª) à calculadora de Índice de Massa Corporal!")
while True:
    try:
        massa = float(input("Escreva sua massa em quilogramas: "))
        break
    except ValueError:
        print("Valor inválido. Favor utilizar apenas números e, opcionalmente, um ponto.")
while True:
    try:
        altura = float(input("Escreva sua altura em metros: "))
        break
    except ValueError:
        print("Valor inválido. Favor utilizar apenas números e, opcionalmente, um ponto.")
imc = massa / (altura ** 2)
mensagem = "Seu índice de massa corporal é " + str(imc) + "."
print(mensagem)