dividendo = int(input("Qual o dividendo: "))
divisor = int(input("E qual o divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"{dividendo} / {divisor} = {quociente} (quociente) \n(O resto é) {resto}")
