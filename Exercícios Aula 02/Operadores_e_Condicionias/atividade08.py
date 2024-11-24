
frase = input("Digite uma frase: ").strip()
palavra = input("Digite uma palavra: ").strip()

if palavra in frase:
    print(f"A palavra '{palavra}' está presente na frase.")
else:
    print(f"A palavra '{palavra}' não está presente na frase.")