import streamlit as st
import random

# PAINEL DE CONTROLE DA ESTAÇÃO ORBITAL
st.set_page_config(layout="wide")

st.title("Painel de Controle: Estação Orbital")
st.write("Monitoramento em tempo real dos sistemas energéticos e vitais.")
st.markdown("---")

# BOTÃO DE ATUALIZAÇÃO DE DADOS DOS SENSORES
if st.button("Atualizar Sensores"):
    
    # 1. SIMULAÇÃO DE DADOS DOS SENSORES VITAIS
    bateria = random.randint(10, 100)
    temperatura = random.randint(20, 70)
    comunicacao = random.randint(40, 100)
    
    # 2. CÁLCULO DE ENERGIA E SUSTENTABILIDADE
    incidencia_solar = random.choice(["Sol Pleno", "Sombra (Eclipse)"])
    
    if incidencia_solar == "Sol Pleno":
        geracao_energia = random.randint(80, 100)
    else:
        geracao_energia = random.randint(0, 10)
        
    consumo_suporte_vida = 30
    consumo_laboratorio = random.randint(10, 60)
    consumo_total = consumo_suporte_vida + consumo_laboratorio
    
    saldo_energetico = geracao_energia - consumo_total
    
    # 3. ORGANIZAÇÃO DOS SENSORES VITAIS
    st.subheader("Sensores Vitais")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Nível de Bateria", value=f"{bateria}%")
    with col2:
        st.metric(label="Temperatura do Laboratório", value=f"{temperatura} °C")
    with col3:
        st.metric(label="Sinal de Comunicação", value=f"{comunicacao}%")
    with col4:
        st.metric(label="Status Geral", value="OPERACIONAL" if bateria > 40 and temperatura < 50 and comunicacao > 60 else "CRÍTICO" if bateria < 40 else "ALERTA")
        
    st.markdown("---")
    
    # 4. ORGANIZAÇÃO DA MATRIZ ENERGÉTICA
    st.subheader("Matriz Energética (Geração vs Consumo)")
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.metric(label="Incidência Solar", value=incidencia_solar)
    with col6:
        st.metric(label="Geração Solar", value=f"{geracao_energia} kW")
    with col7:
        # Adicionei o "delta" aqui para mostrar o quanto o laboratório está pesando no consumo total
        st.metric(label="Consumo Total", value=f"{consumo_total} kW", delta=f"{consumo_laboratorio} kW (Lab)", delta_color="inverse")
    with col8:
        st.metric(label="Saldo Energético", value=f"{saldo_energetico} kW")
        
    st.markdown("---")
    
    # 5. LÓGICA DE DECISÃO
    st.subheader("Sistema de Decisão Automática")
    
    # BALANÇO ENERGÉTICO
    if saldo_energetico < 0:
        st.warning(f"AVISO ENERGÉTICO: Déficit de {saldo_energetico} kW. A estação está consumindo mais do que gera. Baterias em uso.")
        if bateria < 40:
            st.error("CRÍTICO: Bateria abaixo de 40% durante déficit energético! Desligando Laboratório de Pesquisa imediatamente.")
    else:
        st.success(f"SUSTENTABILIDADE: Saldo positivo de +{saldo_energetico} kW. Excedente sendo redirecionado para carregamento das baterias.")

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