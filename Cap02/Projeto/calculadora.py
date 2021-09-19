# Cabeçalho
print(f'{19*"*"} Python Calculator {19*"*"}')
print('\nSelecione o número de opção desejada:\n')
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')

# Variáveis de entradas do usuário
op = input('\nDigite a sua opção (1/2/3/4): ')
num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('\nDigite o segundo número: '))

# Expressões Lambdas
soma = lambda num1, num2: num1 + num2
subtracao = lambda num1, num2: num1 - num2
multiplicacao = lambda num1, num2: num1 * num2
divisao = lambda num1, num2: num1 / num2

# Condicionais
if op == '1':
    print(f'\nResultado: {num1} + {num2} = {soma(num1, num2)}')
elif op == '2':
    print(f'\nResultado:{num1} - {num2}  = {subtracao(num1, num2)}')
elif op == '3':
    print(f'\nResultado:{num1} * {num2} = {multiplicacao(num1, num2)}')
elif op == '4':
    print(f'\nResultado:{num1} / {num2} = {divisao(num1, num2)}')
else:
    print('\nOpção Inválida!')
