class Calculadora01:
    def somar(self, n1, n2):
        return n1 + n2
    def subtrair(self, n1, n2):
        return n1 - n2
    def multiplicar(self, n1, n2):
        return n1 + n2
    def dividir (self, n1, n2):
        return n1 / n2

numero01 = float(input("digite o primeiro numero:"))
numero02 = float(input("digite o segundo numero:"))
opcao = input ("Digite a operação:\next+ Soma\n- Subtração\n\ Divisão\n* Multiplicação")
c1 = Calculadora01 ()
if opcao == "+":
    resultado = c1.somar(numero01, numero02)
    print ("Resultado: ", resultado)
elif opcao == "-":
    resultado = c1.subtrair(numero01, numero02)
    print("Resultado é ", resultado)
elif opcao == "*":
    resultado = c1.multiplicar(numero01, numero02)
    print("resultado é", resultado)
elif opcao == "/":
    resultado = c1.dividir(numero01, numero02)
    print("o resultado é", resultado)
else:
    print("error 404")
