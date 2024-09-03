import os
import json

def load_config():
    # Obtenha o caminho absoluto do diretório atual
    current_dir = os.path.dirname(__file__)

    # Obtenha o caminho absoluto do arquivo config.json
    config_path = os.path.join(current_dir, 'config.json')

    # Abra o arquivo config.json e carregue as configurações
    with open(config_path, "r") as f:
        config = json.load(f)
    return config