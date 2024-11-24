
preco_original = float(input("Digite o preço original do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

total_sem_desconto = preco_original * quantidade

if quantidade > 10:
    desconto = total_sem_desconto * 0.10
    total_com_desconto = total_sem_desconto - desconto
    print(f"Você comprou mais de 10 unidades. Um desconto de 10% foi aplicado.")
    print(f"O total com desconto é: R$ {total_com_desconto:.2f}")
else:
    print(f"O total sem desconto é: R$ {total_sem_desconto:.2f}")
