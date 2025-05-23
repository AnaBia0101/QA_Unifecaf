import requests

def verificar_status_api():
    url = "https://reqres.in/api/users?page=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Teste 01 - Verificação de status da API ReqRes: PASSOU (Status 200)")
        return True
    else:
        print(f"Teste 01 - Verificação de status da API ReqRes: FALHOU (Status {response.status_code})")
        return False

# Chamando a função para executar o teste
verificar_status_api()
