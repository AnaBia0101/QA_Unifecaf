def login(username, password):
    user = buscar_usuario(username)
    return autenticar_usuario(user, password)

def buscar_usuario(username):
    return {"username": username, "password": "senha123"}

def autenticar_usuario(user, password):
    return user["password"] == password

# Teste de Integração
def test_login_com_usuario_e_senha_corretos():
    print("Testando login com usuário e senha corretos...")
    assert login("ana", "senha123") == True, "Login deveria ser bem-sucedido com credenciais corretas"
    print("✅ Teste de integração PASSOU!")

# Executando o teste
test_login_com_usuario_e_senha_corretos()
