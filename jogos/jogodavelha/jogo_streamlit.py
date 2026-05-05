import streamlit as st

# Configuração da página
st.set_page_config(page_title="Jogo da Velha", page_icon="🎮")

st.title("Jogo da Velha em Streamlit")

# Inicializando o "cérebro" do jogo (Session State) para não esquecer os dados ao recarregar a página
if 'tabuleiro' not in st.session_state:
    st.session_state.tabuleiro = [''] * 9
if 'jogador_atual' not in st.session_state:
    st.session_state.jogador_atual = 'X'
if 'vencedor' not in st.session_state:
    st.session_state.vencedor = None
if 'fim_de_jogo' not in st.session_state:
    st.session_state.fim_de_jogo = False

# Função para verificar se alguém ganhou
def verificar_vitoria():
    linhas_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    tabuleiro = st.session_state.tabuleiro
    
    for a, b, c in linhas_vencedoras:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != '':
            return tabuleiro[a]
    
    if '' not in tabuleiro:
        return 'Empate'
    
    return None

# Função que roda quando um botão é clicado
def clicar(index):
    if st.session_state.tabuleiro[index] == '' and not st.session_state.fim_de_jogo:
        # Marca a jogada
        st.session_state.tabuleiro[index] = st.session_state.jogador_atual
        
        # Checa vitória ou empate
        resultado = verificar_vitoria()
        if resultado:
            st.session_state.vencedor = resultado
            st.session_state.fim_de_jogo = True
        else:
            # Troca de jogador
            st.session_state.jogador_atual = 'O' if st.session_state.jogador_atual == 'X' else 'X'

# Função para resetar o jogo
def reiniciar_jogo():
    st.session_state.tabuleiro = [''] * 9
    st.session_state.jogador_atual = 'X'
    st.session_state.vencedor = None
    st.session_state.fim_de_jogo = False

# ----------------- INTERFACE ----------------- #

# Mostra de quem é a vez ou quem ganhou
if st.session_state.vencedor:
    if st.session_state.vencedor == 'Empate':
        st.warning("Deu Velha! O jogo empatou.")
    else:
        st.success(f"🎉 O jogador {st.session_state.vencedor} venceu!")
else:
    st.info(f"Vez do jogador: **{st.session_state.jogador_atual}**")

# Desenhando o tabuleiro 3x3 usando colunas do Streamlit
st.write("---")
# Cria 3 linhas
for i in range(3):
    # Divide a tela em 3 colunas para cada linha
    col1, col2, col3 = st.columns([1, 1, 1])
    colunas = [col1, col2, col3]
    
    for j in range(3):
        indice_real = i * 3 + j
        valor_casa = st.session_state.tabuleiro[indice_real]
        
        # Cria um botão dentro de cada coluna
        with colunas[j]:
            # Se a casa estiver vazia, mostra um espaço invisível (para manter o tamanho do botão)
            texto_botao = valor_casa if valor_casa != '' else '\u2001' 
            st.button(
                texto_botao, 
                key=indice_real, 
                on_click=clicar, 
                args=(indice_real,),
                use_container_width=True
            )

st.write("---")

# Botão de reiniciar
if st.button("Reiniciar Jogo", type="primary"):
    reiniciar_jogo()
    st.rerun()