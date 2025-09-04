import streamlit as st
import random

st.set_page_config(page_title="Adivinhe a Palavra", page_icon="🧠", layout="centered")

# Lista de palavras
palavras = [
    "soma","raiz","pi","reta","grau","aluno","zero","media","teto","angulo","par","impar",
    "vetor","x","y","eixo","area","volume","regra","base","matriz","numero","conta","sinal",
    "dados","funcao","derivada","integral","atomo","sol","lua","ceu","cloro","ar","vento",
    "foton","celula","flora","fauna","pedra","regio","onda","sal","gas","polen","ferro",
    "acido","neve","agua","calor","plantas","oxigenio","plasma","galaxia","estrela","quasar",
    "cometa","buraco","negro","astro","sistema","planeta","luz","som","energia","campo",
    "forca","massa","velocidade","tempo"
]

def gerar_palavra(): 
    return random.choice(palavras)

def converter(p): 
    return " ".join(format(ord(c), "08b") for c in p)

# CSS simplificado
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
html,body,[class*="css"]{font-family:'Share Tech Mono',monospace;background:#000;color:#fff}
.stApp{background:radial-gradient(circle at 15% 50%,rgba(0,255,170,0.05)0%,#000 70%)}
.main{background:rgba(0,0,0,.85);padding:2rem;border-radius:15px;
      border:1px solid rgba(0,255,170,.4);box-shadow:0 0 25px rgba(0,255,170,.3)}
h1{text-align:center;color:#00ffaa;font-size:2.5rem;text-shadow:0 0 20px #00ffaa}
.code-box{background:rgba(0,30,30,.9);padding:15px;border-radius:10px;
          border:1px solid rgba(0,255,170,.4);margin:20px 0}
.code{color:#00ffaa;font-size:1.2rem;text-shadow:0 0 10px rgba(0,255,170,.6)}
.stTextInput>div>div>input{background:rgba(0,20,20,.9)!important;color:#00ffaa!important;
    border:2px solid rgba(0,255,170,.5)!important;border-radius:8px;padding:10px;font-size:1rem}
.stTextInput>div>div>input:focus{border:2px solid #00ffaa!important;
    box-shadow:0 0 15px rgba(0,255,170,.4)}
.stButton>button{background:linear-gradient(to right,#003333,#001a1a)!important;color:#00ffaa!important;
    border-radius:8px;padding:10px 20px;font-weight:bold;box-shadow:0 0 10px rgba(0,255,170,.3);width:100%}
.stButton>button:hover{background:linear-gradient(to right,#004444,#002222)!important;transform:translateY(-2px)}
.hint,.erro{margin:10px 0;padding:10px;border-radius:6px;font-size:.95rem}
.hint{background:rgba(0,100,100,.2);border:1px solid rgba(0,255,170,.3);color:#55ffaa}
.erro{background:rgba(255,0,0,.1);border:1px solid rgba(255,0,0,.3);color:#f55}
.footer{text-align:center;margin-top:30px;color:rgba(0,255,170,.7);font-size:.9rem}
#MainMenu,header,footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

# Sessão inicial
if "palavra" not in st.session_state:
    st.session_state.update({
        "palavra": gerar_palavra(),
        "binario": "",
        "erros": 0,
        "acertou": False
    })
    st.session_state.binario = converter(st.session_state.palavra)

# Função de dicas
def mostrar_dicas():
    if st.session_state.erros == 2:
        st.markdown(f'<div class="hint">💡 A palavra tem {len(st.session_state.palavra)} letras.</div>', unsafe_allow_html=True)
    if st.session_state.erros >= 3:
        st.markdown(f'<div class="hint">🔍 A primeira letra é "{st.session_state.palavra[0].upper()}"</div>', unsafe_allow_html=True)

# Interface
st.markdown("<h1>DECIFRE O CÓDIGO BINÁRIO</h1>", unsafe_allow_html=True)

# Texto explicativo
st.markdown("""
<div style="text-align:center; font-size:1.1rem; margin-bottom:15px;">
    <p>💻 Você recebeu uma sequência de <b>bits</b>.</p>
    <p>🔎 Sua missão é decifrar e descobrir qual <b>palavra secreta</b> eles escondem.</p>
    <p>❌ Cada erro aumenta suas tentativas e libera <b>dicas especiais</b>.<br>
    🎯 Acerte para desbloquear a vitória!</p>
</div>
""", unsafe_allow_html=True)

# Exibe o binário
st.markdown(f'<div class="code-box"><div class="code">{st.session_state.binario}</div></div>', unsafe_allow_html=True)

# Formulário de resposta
with st.form("resposta"):
    r = st.text_input("Digite sua resposta:", placeholder="Escreva aqui...").lower().strip()
    if st.form_submit_button("🚀 VERIFICAR"):
        if r == st.session_state.palavra:
            st.success("🎉 Parabéns! Você decifrou o código!")
            st.balloons()
            st.session_state.acertou = True
        else:
            st.session_state.erros += 1
            st.error(f"❌ Tentativa #{st.session_state.erros}")
            mostrar_dicas()

# Botão de novo desafio
if st.button("🔄 NOVO DESAFIO", use_container_width=True):
    st.session_state.update({
        "palavra": gerar_palavra(),
        "binario": "",
        "erros": 0,
        "acertou": False
    })
    st.session_state.binario = converter(st.session_state.palavra)
    st.rerun()

# Exibe número de tentativas
if not st.session_state.acertou and st.session_state.erros:
    st.markdown(f'<div class="erro"><strong>Tentativas:</strong> {st.session_state.erros}</div>', unsafe_allow_html=True)

# Rodapé
st.markdown('<div class="footer">Desafie suas habilidades de decodificação!</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
