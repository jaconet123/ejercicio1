palabra= str(input("ingrese palabra o frase a comprobar")).replace(" ","")

if palabra==palabra[::-1]:
    print("es palindromo")
else:
    print("no es palindromo")