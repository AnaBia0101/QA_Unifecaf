from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configurar opções do Chrome para execução headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Execução sem interface gráfica
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')  # Melhora desempenho em CI/CD
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1200')  # Tamanho padrão da janela

# Inicializar o navegador Chrome
driver = webdriver.Chrome(
    service=Service(),  # Você pode especificar o caminho do chromedriver aqui se necessário
    options=chrome_options
)

try:
    # Acessar o site de teste
    driver.get("https://www.saucedemo.com/")
    print("Página de login carregada com sucesso")

    # Preencher credenciais de login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    print("Credenciais preenchidas")

    # Clicar no botão de login
    driver.find_element(By.ID, "login-button").click()
    print("Botão de login clicado")

    # Aguardar carregamento e verificar se o login foi bem-sucedido
    time.sleep(2)
    assert "inventory" in driver.current_url, "Falha no login - Redirecionamento incorreto"
    print("✅ Teste de login automatizado passou com sucesso!")

except Exception as e:
    print(f"❌ Erro durante a execução do teste: {str(e)}")
    raise  # Re-lança a exceção para falhar o teste em sistemas de CI/CD

finally:
    # Fechar o navegador mesmo se o teste falhar
    driver.quit()
    print("Navegador fechado")
