import streamlit as st
import random

# PAINEL DE CONTROLE DA ESTAÇÃO ORBITAL
st.set_page_config(layout="wide")

st.title("Painel de Controle: Estação Orbital")
st.write("Monitoramento em tempo real dos sistemas energéticos e vitais.")
st.markdown("---")

# BOTÃO DE ATUALIZAÇÃO DE DADOS DOS SENSORES
if st.button("Atualizar Sensores"):
    
    # SIMULAÇÃO DE DADOS DOS SENSORES
    bateria = random.randint(10, 100)
    temperatura = random.randint(20, 70)
    comunicacao = random.randint(40, 100)
    
    # ORGANIZAÇÃO DOS SENSORES EM COLUNAS
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Nível de Bateria", value=f"{bateria}%")
        
    with col2:
        st.metric(label="Temperatura do Lab", value=f"{temperatura} °C")
        
    with col3:
        st.metric(label="Sinal de Comunicação", value=f"{comunicacao}%")
        
    with col4:
        st.metric(label="Status Geral", value="OPERACIONAL" if bateria > 40 and temperatura < 50 and comunicacao > 60 else "CRÍTICO" if bateria < 40 else "ALERTA")
        
    st.markdown("---")
    
    # LÓGICA DE DECISÃO
    st.subheader("Sistema de Decisão Automática")
    
    # error = vermelho, warning = amarelo, success = verde

    # BATERIA
    if bateria < 40:
        st.error("CRÍTICO: Bateria abaixo de 40%. Desligando Laboratório de Pesquisa para economizar energia.")
    else:
        st.success("Bateria: Nível operacional seguro.")
        
    # TEMPERATURA
    if temperatura > 50:
        st.warning("AVISO: Superaquecimento no laboratório! Acionando resfriamento de emergência.")
    else:
        st.success("Temperatura: Estável.")
        
    # COMUNICAÇÃO
    if comunicacao < 60:
        st.warning("AVISO: Sinal com a base terrestre fraco. Redirecionando energia para as antenas principais.")
    else:
        st.success("Comunicação: Conexão com a Terra estabelecida.")