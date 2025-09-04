import streamlit as st
import random

st.set_page_config(page_title="Adivinhe a Palavra", page_icon="🧠", layout="centered")

# Lista de palavras expandida
palavras = [
    "soma", "raiz", "pi", "reta", "grau", "aluno", "zero", "média", "teto", "ângulo",
    "par", "ímpar", "vetor", "x", "y", "eixo", "area", "volume", "regra", "base",
    "matriz", "número", "conta", "sinal", "dados", "função", "derivada", "integral",
    "átomo", "sol", "lua", "céu", "cloro", "ar", "vento", "fóton", "célula", "flora",
    "fauna", "pedra", "régio", "onda", "sal", "gás", "pólen", "ferro", "ácido", "neve",
    "água", "calor", "plantas", "oxigênio", "plasma", "galáxia", "estrela", "quasar",
    "cometa", "buraco", "negro", "astro", "sistema", "planeta", "luz", "som", "energia",
    "campo", "força", "massa", "velocidade", "tempo"
]

# Funções
def gerar_palavra():
    return random.choice(palavras)

def converter_para_binario(palavra):
    return " ".join(format(ord(c), "08b") for c in palavra)

# CSS estilo hacker moderno com fundo preto
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'JetBrains Mono', monospace;
    background-color: #000000;
    color: #ffffff;
}

.stApp {
    background-image: radial-gradient(circle at 15% 50%, rgba(0, 80, 80, 0.1) 0%, rgba(0, 0, 0, 0.99) 60%);
}

.main {
    background-color: rgba(0, 0, 0, 0.85);
    padding: 3rem 2rem;
    border-radius: 15px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.15);
    position: relative;
    overflow: hidden;
}

.main::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #00ffff, transparent);
    animation: scanline 8s linear infinite;
}

@keyframes scanline {
    0% { top: 0%; }
    100% { top: 100%; }
}

h1 {
    text-align: center;
    color: #00ffff;
    font-size: 2.8rem;
    margin-bottom: 1.5rem;
    text-shadow: 0 0 15px rgba(0, 255, 255, 0.7);
    letter-spacing: 2px;
    position: relative;
    padding-bottom: 15px;
}

h1::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 150px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #00ffff, transparent);
}

h2, h3 {
    color: #00ffff;
    border-left: 4px solid #00ffff;
    padding-left: 12px;
    text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
}

.code-container {
    background-color: rgba(0, 20, 20, 0.9);
    padding: 25px;
    border-radius: 8px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    margin: 25px 0;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

.code-container::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, rgba(0, 255, 255, 0.05) 0%, transparent 70%);
    pointer-events: none;
}

.code-content {
    color: #00ffff;
    font-size: 1.2rem;
    line-height: 1.8;
    text-shadow: 0 0 8px rgba(0, 255, 255, 0.4);
    letter-spacing: 1px;
}

.stTextInput>div>div>input {
    background-color: rgba(0, 30, 30, 0.8) !important;
    color: #00ffff !important;
    border: 2px solid rgba(0, 255, 255, 0.4) !important;
    border-radius: 6px;
    padding: 12px 15px;
    font-size: 1.1rem;
    transition: all 0.3s ease;
}

.stTextInput>div>div>input:focus {
    border: 2px solid #00ffff !important;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
    outline: none;
}

.stTextInput>div>div>input::placeholder {
    color: rgba(0, 255, 255, 0.6) !important;
}

.stButton>button {
    background: linear-gradient(to right, #003333, #001a1a) !important;
    color: #00ffff !important;
    border: none !important;
    border-radius: 6px;
    padding: 12px 24px;
    font-size: 1.1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
    width: 100%;
    margin-top: 10px;
    position: relative;
    overflow: hidden;
}

.stButton>button::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(to right, transparent, rgba(0, 255, 255, 0.2), transparent);
    transform: rotate(45deg);
    animation: shine 3s infinite;
}

@keyframes shine {
    0% { left: -50%; }
    100% { left: 150%; }
}

.stButton>button:hover {
    background: linear-gradient(to right, #004444, #002222) !important;
    transform: translateY(-2px);
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
}

.stButton>button:active {
    transform: translateY(0);
}

.info-box {
    background: rgba(0, 30, 30, 0.7);
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid #00ffff;
    margin: 20px 0;
}

.stAlert {
    border-radius: 8px;
    padding: 15px 20px;
    background-color: rgba(0, 0, 0, 0.8) !important;
    border: 1px solid;
}

.stSuccess {
    border-color: rgba(0, 255, 0, 0.3) !important;
    color: #00ff00 !important;
}

.stError {
    border-color: rgba(255, 0, 0, 0.3) !important;
    color: #ff5555 !important;
}

.stInfo {
    border-color: rgba(0, 150, 255, 0.3) !important;
    color: #55aaff !important;
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: rgba(0, 255, 255, 0.7);
    font-size: 0.9rem;
    padding-top: 20px;
    border-top: 1px solid rgba(0, 255, 255, 0.2);
}

.pulse {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(0, 255, 255, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(0, 255, 255, 0); }
    100% { box-shadow: 0 0 0 0 rgba(0, 255, 255, 0); }
}

.erro-counter {
    background-color: rgba(255, 0, 0, 0.1);
    color: #ff5555;
    padding: 10px 15px;
    border-radius: 6px;
    border: 1px solid rgba(255, 0, 0, 0.3);
    display: inline-block;
    margin-top: 15px;
}

.dica-box {
    background-color: rgba(0, 100, 100, 0.2);
    padding: 15px;
    border-radius: 6px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    margin: 10px 0;
}

#MainMenu, header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Inicialização da sessão
if "palavra" not in st.session_state:
    st.session_state.palavra = gerar_palavra()
    st.session_state.binario = converter_para_binario(st.session_state.palavra)
    st.session_state.erros = 0
    st.session_state.acertou = False

# Container principal
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Título e instruções
    st.markdown("<h1>🧩 DECIFRE O CÓDIGO BINÁRIO</h1>", unsafe_allow_html=True)
    st.write("Descubra a palavra oculta por trás deste código:")

    # Exibir binário com estilo
    st.markdown('<div class="code-container"><div class="code-content">', unsafe_allow_html=True)
    st.code(st.session_state.binario, language="text")
    st.markdown('</div></div>', unsafe_allow_html=True)

    # Explicação ASCII
    with st.expander("ℹ️ **COMO FUNCIONA**", expanded=True):
        st.markdown("""
        - Cada caractere tem um número na tabela **ASCII** (ex: `"a"` → 97)  
        - Esse número é convertido em binário de 8 bits (ex: `97` → `01100001`)  
        - A palavra é formada juntando os binários de cada letra
        """)

    # Formulário de resposta
    with st.form("form_resposta"):
        resposta = st.text_input("**Digite sua resposta:**", placeholder="Escreva a palavra aqui...")
        submit = st.form_submit_button("🚀 VERIFICAR RESPOSTA", use_container_width=True)

        if submit and not st.session_state.acertou:
            if resposta.lower().strip() == st.session_state.palavra:
                st.success("🎉 Parabéns! Você decifrou o código corretamente!")
                st.balloons()
                st.session_state.acertou = True
            else:
                st.session_state.erros += 1
                st.error(f"❌ Resposta incorreta! Tentativa #{st.session_state.erros}")
                if st.session_state.erros >= 2:
                    with st.container():
                        st.markdown('<div class="dica-box">', unsafe_allow_html=True)
                        st.info(f"💡 Dica: A palavra tem {len(st.session_state.palavra)} letras.")
                        st.markdown('</div>', unsafe_allow_html=True)
                if st.session_state.erros >= 3:
                    with st.container():
                        st.markdown('<div class="dica-box">', unsafe_allow_html=True)
                        st.info(f"🔍 Dica adicional: A primeira letra é '{st.session_state.palavra[0].upper()}'")
                        st.markdown('</div>', unsafe_allow_html=True)

    # Botão para nova palavra
    if st.button("🔄 GERAR NOVO DESAFIO", use_container_width=True, type="primary"):
        st.session_state.palavra = gerar_palavra()
        st.session_state.binario = converter_para_binario(st.session_state.palavra)
        st.session_state.erros = 0
        st.session_state.acertou = False
        st.rerun()

    # Exibir contador de erros
    if not st.session_state.acertou and st.session_state.erros > 0:
        st.markdown(f'<div class="erro-counter"><strong>Tentativas:</strong> {st.session_state.erros}</div>', unsafe_allow_html=True)

    # Rodapé
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.write("Desafie suas habilidades de decodificação!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
