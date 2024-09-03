# Vulnerability Scanner XXS e SQL Injection

**Vulnerability Scanner** é um script Python que detecta vulnerabilidades de SQL Injection e XSS em sites. Ele analisa URLs listadas em um arquivo de configuração e fornece detalhes sobre a presença dessas falhas, incluindo sugestões de exploração e correção.

## Funcionalidades

- **SQL Injection**: Detecta vulnerabilidades de SQL Injection.
- **XSS**: Identifica vulnerabilidades de Cross-Site Scripting (XSS).

## Requisitos

- Python 3.12.5
- Bibliotecas Python: `requests`, `logging`, `json`


## Arquivos

- **`XSS_SQLinjection_Scanner.py`**: O script principal para escaneamento de vulnerabilidades.
- **`config.json`**: Arquivo de configuração contendo a lista de URLs a serem escaneadas.

### Estrutura do Arquivo `config.json`

O arquivo `config.json` deve estar no mesmo diretório que o script e deve ter o seguinte formato:

```
{
    "urls": [
        "https://example.com/",
        "https://another-example.com/"
    ]
}
Adicione as URLs que você deseja escanear no array "urls".
```

## Objetivo do Script

Ler as URLs do arquivo config.json.
Realizar escaneamentos para SQL Injection e XSS.
Exibir resultados detalhados no console, incluindo:
URL
Código de Status HTTP
Tamanho da Resposta
Conteúdo da Resposta (primeiros 500 caracteres)
Descrição e sugestões para exploração e correção das vulnerabilidades detectadas
Saída do Script
A saída do script será organizada e fornecerá informações detalhadas sobre as vulnerabilidades detectadas:

SQL Injection:

Descrição de como a vulnerabilidade pode ser explorada.
Sugestões de correção.

XSS:

Descrição de como a vulnerabilidade pode ser explorada.
Sugestões de correção.
Considerações
Segurança: Use o script apenas em sites para os quais você tem permissão para realizar testes de segurança. A realização de escaneamentos em sites sem permissão pode ser ilegal e antiético.
Desenvolvimento Futuro: Este script é uma base para escaneamento de vulnerabilidades e pode ser expandido para incluir outras vulnerabilidades e técnicas de escaneamento.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou relatar problemas. Abra um pull request ou issue no repositório para qualquer sugestão ou correção.

## Licença

Este projeto é licenciado sob a MIT License.
