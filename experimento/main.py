import streamlit as st
import random

# Lista de palavras possíveis
palavras = [
    "soma", "raiz", "pi", "reta", "grau", "aluno", "zero", "média", "teto", "ângulo",
    "par", "ímpar", "vetor", "x", "y", "eixo", "area", "volume", "regra", "base",
    "matriz", "número", "conta", "sinal", "dados",
    "átomo", "sol", "lua", "céu", "cloro", "ar", "vento", "fóton", "célula", "flora",
    "fauna", "pedra", "régio", "onda", "sal", "gás", "pólen", "ferro", "ácido", "neve",
    "água", "calor", "plantas", "oxigênio", "plasma"
]

# Função para escolher uma palavra
def gerar_palavra():
    return random.choice(palavras)

# Converter palavra em binário
def converter_para_binario(palavra):
    return " ".join(format(ord(c), "08b") for c in palavra)

# Estado da sessão do usuário
if "palavra" not in st.session_state:
    st.session_state.palavra = gerar_palavra()
    st.session_state.binario = converter_para_binario(st.session_state.palavra)
    st.session_state.erros = 0
    st.session_state.acertou = False

st.set_page_config(page_title="Adivinhe a Palavra", page_icon="🧠", layout="centered")
st.title("🧩 Jogo: Adivinhe a Palavra em Binário")

st.write("Tente descobrir qual é a palavra representada abaixo em código binário:")

# Exibir binário da palavra
st.code(st.session_state.binario, language="text")

# Formulário de resposta
with st.form("form_resposta"):
    resposta = st.text_input("Digite sua resposta:", "")
    submit = st.form_submit_button("Verificar")

    if submit and not st.session_state.acertou:
        if resposta.lower().strip() == st.session_state.palavra:
            st.success("🎉 Parabéns! Você acertou a palavra!")
            st.session_state.acertou = True
        else:
            st.session_state.erros += 1
            st.error(f"❌ Erro {st.session_state.erros}: Tente novamente!")

# Botão para reiniciar
if st.button("🔄 Nova Palavra"):
    st.session_state.palavra = gerar_palavra()
    st.session_state.binario = converter_para_binario(st.session_state.palavra)
    st.session_state.erros = 0
    st.session_state.acertou = False
    st.experimental_rerun()
