def calcular_desconto(valor, percentual):
    return valor - (valor * percentual)

def testar_regressao_desconto():
    print("\n🔍 Teste de Regressão - Cálculo de Desconto")
    
    # Casos de teste conhecidos
    casos_teste = [
        (100, 0.1, 90),    # 10% de desconto
        (200, 0.2, 160),    # 20% de desconto
        (50, 0.05, 47.5),   # 5% de desconto
        (1000, 0, 1000),    # 0% de desconto
    ]
    
    for valor, percentual, esperado in casos_teste:
        resultado = calcular_desconto(valor, percentual)
        assert resultado == esperado, (
            f"REGRESSÃO DETECTADA! "
            f"Entrada: ({valor}, {percentual}) | "
            f"Esperado: {esperado} | "
            f"Obtido: {resultado}"
        )
    
    print("✅ Nenhuma regressão encontrada - cálculo de desconto funciona conforme esperado!")

# Executando o teste
testar_regressao_desconto()
