def test_aceitacao_fluxo_completo_login():
    print("\n🔐 Teste de Aceitação - Fluxo Completo de Login e Ações Pós-Login")
    
    # 1. Cadastro do usuário
    resultado_cadastro = cadastrar_usuario("João", "joao@email.com", "senha123")
    assert resultado_cadastro == "Usuário cadastrado com sucesso!", f"Falha no cadastro: {resultado_cadastro}"
    
    # 2. Login
    resultado_login = login_usuario("joao@email.com", "senha123")
    assert resultado_login == "Login bem-sucedido", f"Falha no login: {resultado_login}"
    
    # 3. Ações pós-login
    perfil = acessar_perfil()
    assert "João" in perfil["nome"], f"Perfil incorreto: {perfil}"
    assert "joao@email.com" in perfil["email"], f"Email não encontrado no perfil"
    
    print("✅ Fluxo completo testado com sucesso!")

# Funções simuladas (substitua pelas reais)
def cadastrar_usuario(nome, email, senha):
    return "Usuário cadastrado com sucesso!"

def login_usuario(email, senha):
    return "Login bem-sucedido"

def acessar_perfil():
    return {"nome": "João", "email": "joao@email.com"}

# Execução
test_aceitacao_fluxo_completo_login()
