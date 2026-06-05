# SISTEMA DE MONITORAMENTO: ESTAÇÃO ORBITAL DE PESQUISA

Global Solution - Ciência da Computação | 1CCPK 2026 

Disciplina: Soluções em Energias Renováveis e Sustentáveis

## Sobre o Projeto

Este projeto simula o ambiente de uma Estação Orbital de Pesquisa, utilizando da linguagem Python para desenvolver um sistema inteligente de controle básico para uma missão espacial experimental. A aplicação recebe, interpreta e exibe dados simulados em tempo real, aplicando conceitos de eficiencia energetica e sustentabilidade.

O foco principal do sistema é garantir o 'Suporte à Vida'. Para isso, o programa toma decisões automáticas de balanceamento de energia, desligando módulos não essenciais da nave. Essa lógica permite poupar as baterias da estação durante a passagem pela zona de sombra da Terra, onde não há incidência de luz solar para recarga.

## Funcionalidades

- **Atualização de sensores** sob demanda via botão interativo
- **Monitoramento de 4 métricas** em tempo real:
  - Nível de Bateria (%)
  - Temperatura do Laboratório (°C)
  - Sinal de Comunicação (%)
  - Status Geral (OPERACIONAL / ALERTA / CRÍTICO)
- **Sistema de decisão automática** com alertas visuais categorizados por severidade

## Lógica de Alertas

| Sensor | Condição | Ação |
|---|---|---|
| Bateria | < 40% | 🔴 CRÍTICO — Desligamento do Laboratório de Pesquisa |
| Temperatura | > 50 °C | 🟡 AVISO — Acionamento do resfriamento de emergência |
| Comunicação | < 60% | 🟡 AVISO — Redirecionamento de energia para as antenas |

O **Status Geral** é calculado da seguinte forma:
- `OPERACIONAL` — Bateria ≥ 40%, Temperatura ≤ 50 °C e Comunicação ≥ 60%
- `CRÍTICO` — Bateria < 40%
- `ALERTA` — Qualquer outra condição fora do padrão

## Tecnologias Utilizadas

- Python 3.14+

- Streamlit 

## Instalação e configuração

**1. Baixe o arquivo ``codigo-fonte.py`` e abra em um IDE**

**2. Abra o terminal e instale a biblioteca ``Streamlit`` com o seguinte comando:**
```bash
pip install streamlit
```

**3. Após a instalação da biblioteca Streamlit, rode o seguinte comando abaixo no terminal**
```bash
python -m streamlit run codigo-fonte.py
```

A aplicação estará disponível em `http://localhost:8501`.

## Integrantes do Grupo

Kenichi Caio Yamamoto - RM: 569815

Rodger Costa Rios - RM: 571438

*Projeto acadêmico desenvolvido para a avaliação de Global Solution.*