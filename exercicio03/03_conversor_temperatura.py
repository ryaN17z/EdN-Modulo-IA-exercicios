temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").strip().upper()
destino = input("Digite a unidade de destino (C, F ou K): ").strip().upper()

if origem == destino:
    resultado = temp
elif origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    else:
        resultado = temp + 273.15
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    else:
        resultado = (temp - 32) * 5/9 + 273.15
else:
    if destino == "C":
        resultado = temp - 273.15
    else:
        resultado = (temp - 273.15) * 9/5 + 32

print(f"{temp} {origem} é igual a {resultado:.2f} {destino}")