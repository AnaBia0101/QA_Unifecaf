def soma(a, b):
    return a + b

# Teste unitário simplificado com asserts
def testar_soma():
    print("Iniciando testes da função soma()...")
    
    # Testes com valores positivos
    assert soma(2, 3) == 5, "2 + 3 deveria ser 5"
    
    # Testes com valores negativos
    assert soma(-2, 3) == 1, "-2 + 3 deveria ser 1"
    assert soma(-2, -3) == -5, "-2 + -3 deveria ser -5"
    
    # Testes com zero
    assert soma(0, 0) == 0, "0 + 0 deveria ser 0"
    
    print("✅ Todos os testes passaram!")

# Executa os testes
testar_soma()
