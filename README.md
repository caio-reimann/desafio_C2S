<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Desafio Técnico – Vaga de Desenvolvedor Python | C2S</h3>

  <p align="center">
    Modelagem de dados / MCP (Cliente e Servidor) / Agente IA
  </p>
</div>

### Introdução
Este projeto foi desenvolvido para o Desafio Técnico – Vaga de Desenvolvedor Python,  proposto pela C2S.


### Linguagem e pacotes utilizados

[![python](https://img.shields.io/badge/python-3.12.3-blue)](https://www.python.org)
[![faker](https://img.shields.io/badge/faker-37.4.2-green)](https://github.com/joke2k/faker)
[![faker-vehicle](https://img.shields.io/badge/faker_vehicle-0.2.0-pink)]()
[![langchain-groq](https://img.shields.io/badge/langchain_groq-0.3.6-red)]()
[![mcp](https://img.shields.io/badge/mcp-1.11.0-white)]()
[![mcp-use](https://img.shields.io/badge/mcp_use-1.3.6-cyan)]()
[![sqlalchemy](https://img.shields.io/badge/sqlalchemy-2.0.41-orange)]()
[![pytest](https://img.shields.io/badge/pytest-8.4.1-purple)]()

### Instalação

_Para executar o projeto, siga os passos:_

1. Instale o gerenciador de pacotes UV (https://docs.astral.sh/uv/getting-started/installation/)

2. Crie um ambiente virtual e instale os pacotes necessários
  ```sh
  uv sync
  ```
3. Crie um arquivo .env com o seguinte formato (Não esqueça de trocar o \<APIKEY\> pela sua api key do GROQ).  
  ```sh
GROQ_API_KEY=<APIKEY> # https://console.groq.com/keys
DB_URL=<DB_URL> # Ex: sqlite:///cars.db
VERBOSE=False # https://docs.mcp-use.com/guides/logging#agent-specific-verbosity
  ```
4. Ative o ambiente virtual
  ```sh
  source .venv/bin/activate
  ```


### Iniciando o Projeto
Para iniciar o projeto execute:
  ```sh
  ./run_mcp.sh
  ```

### Testando automaticante o Projeto
Para iniciar os testes automatizados execute:
  ```sh
  ./run_tests.sh
  ```

### Testando manualmente o Servidor MCP
Para testar o servidor MCP execute:
  ```sh
  ./run_mcp_server_dev.sh
  ```
