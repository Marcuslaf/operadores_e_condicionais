nome_usuario = input("Digite o nome de usuário: ").strip()
senha = input("Digite a senha: ").strip()

# Verifica se o nome de usuário e senha estão corretos
if nome_usuario == "admin" and senha == "1234":
    print("Login bem-sucedido! Bem-vindo, admin.")
else:
    print("Nome de usuário ou senha incorretos. Tente novamente.")