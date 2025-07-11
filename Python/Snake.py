from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
import time

URL_LIST = [
 "https://forumdesustentabilidade.com.br/gestao-medica-da-medplus-que-evita-deslocamentos-de-pacientes/"   
]

def process_page(driver, url):
    """Acessa a URL, faz scroll imediatamente e espera 1 segundo"""
    try:
        print(f"Acessando: {url}")
        
        # Configura para não esperar o carregamento completo
        driver.set_page_load_timeout(5)  # Timeout de 5s (continua mesmo se não carregar tudo)
        
        try:
            driver.get(url)  # Tenta carregar a página
        except:
            pass  # Ignora se a página não carregar totalmente
        
        driver.execute_script("window.scrollBy(0, 800);")
        print("✔ Scroll realizado")
        
        # Espera 1 segundo antes de ir para o próximo link
        time.sleep(1)
        
    except Exception as e:
        print(f"Erro ao processar {url}: {e}")

def main():
    options = Options()
    options.headless = False 
    time.sleep(1)

    try:
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1280, 720)
    
        for ciclo in range(100):
            print(f"\n=== CICLO {ciclo + 1}/1000 ===")
            
            for url in URL_LIST:
                process_page(driver, url)
                
            # Pequena pausa entre ciclos (opcional)
            time.sleep(2)
            
    except Exception as e:
        print(f"ERRO no navegador: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()
            print("Navegador fechado.")

if __name__ == "__main__":
    main()
