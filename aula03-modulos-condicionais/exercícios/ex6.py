num1 = int(input("Digite um número: "))
num2 = int(input("Digite um outro número: "))
op = str(input("Selecione uma das operações matemáticas (+, -, *, /): "  ))

match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)