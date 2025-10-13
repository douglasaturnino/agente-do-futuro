

# Agente do Futuro - Análise Fiscal

Este projeto utiliza a API Gemini do Google para realizar análises fiscais automatizadas de dados extraídos de arquivos CSV contendo informações de Notas Fiscais eletrônicas (NF-e). O objetivo do sistema é avaliar a coerência fiscal de produtos e operações com base em campos como CFOP, NCM/SH e Natureza da Operação.

## Funcionalidades

- **Upload de arquivos CSV**: O usuário pode carregar arquivos CSV contendo dados de NF-e.
- **Análise Fiscal**: O sistema utiliza um modelo de IA (Gemini) para analisar a coerência fiscal de cada item da nota, com base nas informações fornecidas (como CFOP, NCM, etc.).
- **Classificação de Risco**: Para cada item de nota fiscal, o sistema retorna uma classificação de risco (BAIXO, MÉDIO ou ALTO), juntamente com uma justificativa e uma recomendação.
- **Interface Web com Streamlit**: O sistema é acessado por meio de uma interface web simples e intuitiva, desenvolvida com o Streamlit.

## Como Usar

1. **Instalação**: Clone este repositório em sua máquina local e instale as dependências necessárias.

```bash
git clone https://github.com/douglasaturnino/agente-do-futuro.git
cd agente-do-futuro
pip install -r requirements.txt
````

2. **Configuração da API**: Obtenha uma chave de API do Google Gemini e armazene-a nas configurações do Streamlit.

* Coloque sua chave de API no arquivo `secrets.toml`:

```toml
[general]
GOOGLE_API_KEY = "sua_chave_de_api"
```

3. **Execução**: Inicie a aplicação Streamlit com o seguinte comando:

```bash
streamlit run app.py
```

4. **Uso**: Na interface web, carregue um arquivo CSV contendo dados de NF-e. O sistema irá processar os dados e retornar uma análise fiscal para cada item.

## Exemplo de Saída

A análise fiscal de cada item será exibida no formato JSON, como no exemplo abaixo:

```json
{
  "CHAVE_ACESSO": "1234567890",
  "RISCO_FISCAL": "MÉDIO",
  "JUSTIFICATIVA": "O NCM fornecido não é adequado para o tipo de operação CFOP 5101.",
  "RECOMENDAÇÃO": "Ajustar o NCM ou a natureza da operação."
}
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Tecnologias Utilizadas

* **Streamlit**: Framework para criação de aplicações web interativas.
* **Pandas**: Biblioteca para análise de dados em Python.
* **Google Gemini API**: API de IA generativa do Google, utilizada para análise fiscal.
* **JSON**: Formato de dados utilizado para a resposta da análise.






