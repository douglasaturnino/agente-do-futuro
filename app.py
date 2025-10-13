import json
import os

import pandas as pd
import streamlit as st
from google import genai

os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]


client = genai.Client()

st.set_page_config(page_title="Agente do Futuro", layout="centered")
st.title("📑 Agente do Futuro - Análise Fiscal")

uploaded_file = st.file_uploader("Carregue o arquivo CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=",", dtype=str)
    st.write("Prévia do CSV:")
    st.dataframe(df.head())

    for _, row in df.iterrows():
        chave_acesso = row.get("CHAVE DE ACESSO", "")
        cfop = row.get("CFOP", "")
        ncm_tipo = row.get("NCM/SH (TIPO DE PRODUTO)", "")
        codigo_ncm = row.get("CÓDIGO NCM/SH", "")
        natureza = row.get("NATUREZA DA OPERAÇÃO", "")

        prompt = f"""
            Chave de acesso: {chave_acesso}
            CFOP: {cfop}
            NCM/SH (TIPO DE PRODUTO): {ncm_tipo}
            CÓDIGO NCM/SH: {codigo_ncm}
            NATUREZA DA OPERAÇÃO: {natureza}

            Você é um Analista Fiscal sênior e muito rigoroso. Sua tarefa é analisar a coerência fiscal de um único item de NF-e.

            Responda estritamente em JSON no formato:

            {{
            "CHAVE_ACESSO": "{chave_acesso}",
            "RISCO_FISCAL": "BAIXO | MÉDIO | ALTO",
            "JUSTIFICATIVA": "Explicação resumida",
            "RECOMENDAÇÃO": "Ação sugerida"
            }}
            """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            resposta_text = response.text.strip()

            parsed = json.loads(resposta_text)
            st.json(parsed)

        except json.JSONDecodeError:
            st.warning(
                "Não foi possível interpretar como JSON. Exibindo resposta crua:"
            )
            st.text(resposta_text)
        except Exception as e:
            st.error(f"Erro na chamada da API: {e}")
