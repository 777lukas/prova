num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case "+":
        soma = num1 + num2
        print("Soma:", soma)
    case "-":
        subtracao = num1 - num2
        print("Subtração:", subtracao)
    case "*":
        multiplicacao = num1 * num2
        print("Multiplicação:", multiplicacao)
    case "/":
        if num2 != 0:
            divisao = num1 / num2
            print("Divisão:", divisao)
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida! Use +, -, * ou /.")




      
      
      
idade = int(input("Digite sua idade: "))
match idade:
    case x if x < 12:
        print("Criança")
    case x if x > 12 and x < 18:
        print("Adolescente")
    case x if x > 18 and x < 60:
        print("Adulto")
    case x if x > 60 and x < 100:
        print("Idoso")
    case x if x >= 100:
        print("Múmia")
    case _:
        print("Idade inválida")



nota = int(input("Digite sua nota: "))

match nota:
    case 10:
        print("Parabéns, nota máxima!")
    case 9 | 8 | 7:
        print("Aprovado")
    case 6 | 5 | 4 | 3 | 2 | 1 | 0:
        print("Reprovado")
    case _:
        print("Nota inválida")