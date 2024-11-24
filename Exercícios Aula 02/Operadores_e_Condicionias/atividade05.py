preco = float(input("Digite o preço do produto: R$ "))

desconto = preco * 0.05
preco -= desconto

print(f"O preço do produto com desconto de 5% é: R$ {preco:.2f}")