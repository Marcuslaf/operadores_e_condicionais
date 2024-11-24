frase = input("Digite uma frase: ").strip().lower()
caractere = input("Digite uma caractere: ").strip().lower()

if caractere in frase:
    print(f"A frase contém o caractere '{caractere}'.")
else:
    print(f"A frase não contém o caractere '{caractere}'.") 