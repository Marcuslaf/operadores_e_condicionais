idade = int(input("Digite sua idade: "))

habilitação = input("Você possui habilitação? (Sim ou Não): ").strip().lower()

if idade >= 18 and habilitação == "sim":
    print("Vocẽ é maior de idade e possui habilitação!")
elif idade >= 18 and habilitação == "não":
    print("Vocẽ é maior de idade e não possui habilitação!")
else:
    "Vocẽ não é maior de idade"