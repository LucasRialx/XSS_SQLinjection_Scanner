import requests
import logging
import os
import json

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_sql_injection(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Lança um erro para códigos de status HTTP 4xx/5xx

        response.encoding = response.apparent_encoding  # Ajusta a codificação
        if "SQL" in response.text:
            logging.info("\n" + "-"*50)
            logging.info("Detecção de SQL Injection")
            logging.info("-" * 50)
            logging.info(f"URL: {url}")
            logging.info(f"Código de Status HTTP: {response.status_code}")
            logging.info(f"Tamanho da Resposta: {len(response.text)} caracteres")
            logging.info(f"Conteúdo da Resposta (primeiros 500 caracteres):\n{response.text[:500]}")
            logging.info("Vulnerabilidade encontrada: SQL Injection")
            logging.info("Como explorar: Uma SQL Injection pode permitir que um atacante execute comandos SQL maliciosos no banco de dados. Exemplos incluem a injeção de código SQL em campos de entrada.")
            logging.info("Sugestões de Correção: Valide e escape todos os dados de entrada do usuário. Use consultas preparadas e procedimentos armazenados.")
            logging.info("-" * 50)
    except requests.RequestException as e:
        logging.error(f"Erro ao acessar {url}: {e}")

def scan_xss(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

        response.encoding = response.apparent_encoding
        if "<script>" in response.text:
            logging.info("\n" + "-"*50)
            logging.info("Detecção de XSS")
            logging.info("-" * 50)
            logging.info(f"URL: {url}")
            logging.info(f"Código de Status HTTP: {response.status_code}")
            logging.info(f"Tamanho da Resposta: {len(response.text)} caracteres")
            logging.info(f"Conteúdo da Resposta (primeiros 500 caracteres):\n{response.text[:500]}")
            logging.info("Vulnerabilidade encontrada: XSS")
            logging.info("Como explorar: Um ataque XSS pode permitir que um atacante insira scripts maliciosos em uma página da web, que serão executados no navegador de outros usuários.")
            logging.info("Sugestões de Correção: Escape todos os dados de entrada do usuário que são exibidos em uma página da web. Utilize Content Security Policy (CSP) para reduzir o impacto de ataques XSS.")
            logging.info("-" * 50)
    except requests.RequestException as e:
        logging.error(f"Erro ao acessar {url}: {e}")

def load_config():
    try:
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, 'config.json')
        with open(config_path, "r") as f:
            config = json.load(f)
        return config
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"Erro ao carregar o arquivo de configuração: {e}")
        raise

def main():
    try:
        config = load_config()
        urls = config.get("urls", [])
        if not urls:
            logging.warning("Nenhuma URL encontrada no arquivo de configuração.")
        for url in urls:
            logging.info("\n" + "-"*50)
            logging.info(f"Iniciando escaneamento para {url}")
            logging.info("-" * 50)
            scan_sql_injection(url)
            scan_xss(url)
    except Exception as e:
        logging.error(f"Erro no processo de escaneamento: {e}")

if __name__ == "__main__":
    main()
