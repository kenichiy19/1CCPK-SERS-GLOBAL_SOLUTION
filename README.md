# SISTEMA DE MONITORAMENTO: ESTAÇÃO ORBITAL DE PESQUISA

Global Solution - Ciência da Computação | 1CCPK 2026 

Disciplina: Soluções em Energias Renováveis e Sustentáveis

## Sobre o Projeto

Este projeto simula o ambiente de uma Estação Orbital de Pesquisa, utilizando da linguagem Python para desenvolver um sistema inteligente de controle básico para uma missão espacial experimental. A aplicação recebe, interpreta e exibe dados simulados em tempo real, aplicando conceitos de eficiencia energetica e sustentabilidade.

O foco principal do sistema é garantir o 'Suporte à Vida'. Para isso, o programa toma decisões automáticas de balanceamento de energia, desligando módulos não essenciais da nave. Essa lógica permite poupar as baterias da estação durante a passagem pela zona de sombra da Terra, onde não há incidência de luz solar para recarga.

## Funcionalidades

- **Atualização de sensores** sob demanda via botão interativo
- **Sensores Vitais** — monitoramento de 4 métricas em tempo real:
  - Nível de Bateria (%)
  - Temperatura do Laboratório (°C)
  - Sinal de Comunicação (%)
  - Status Geral (OPERACIONAL / ALERTA / CRÍTICO)
- **Matriz Energética** — cálculo dinâmico de geração vs. consumo:
  - Incidência Solar (Sol Pleno / Sombra por Eclipse)
  - Geração Solar (kW)
  - Consumo Total com destaque do consumo do laboratório (kW)
  - Saldo Energético (kW)
- **Sistema de decisão automática** com alertas visuais categorizados por severidade

## Lógica Energética
 
A geração solar varia conforme a posição orbital:
 
| Condição Solar | Geração Estimada |
|---|---|
| Sol Pleno | 80 – 100 kW |
| Sombra (Eclipse) | 0 – 10 kW |
 
O consumo é composto por:
- **Suporte de vida:** 30 kW (fixo)
- **Laboratório de pesquisa:** 10 – 60 kW (variável)

O **Saldo Energético** = Geração Solar − Consumo Total. Um saldo negativo indica que as baterias estão sendo utilizadas.

## Lógica de Alertas
 
| Sistema | Condição | Severidade | Ação |
|---|---|---|---|
| Saldo Energético | < 0 kW | 🟡 AVISO | Notificação de déficit; baterias em uso |
| Bateria + Déficit | < 40% durante déficit | 🔴 CRÍTICO | Desligamento imediato do Laboratório |
| Temperatura | > 50 °C | 🟡 AVISO | Acionamento do resfriamento de emergência |
| Comunicação | < 60% | 🟡 AVISO | Redirecionamento de energia para as antenas |
| Saldo Energético | ≥ 0 kW | 🟢 OK | Excedente redirecionado para carregar as baterias |
 
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

## Observações
 
- Todos os dados são **simulados aleatoriamente** a cada atualização, dentro dos seguintes intervalos:
  - Bateria: 10% – 100%
  - Temperatura: 20 °C – 70 °C
  - Comunicação: 40% – 100%
  - Geração Solar: 0 – 10 kW (eclipse) ou 80 – 100 kW (sol pleno)
  - Consumo do Laboratório: 10 – 60 kW
- O painel utiliza layout wide para melhor visualização das métricas.


## Integrantes do Grupo

Kenichi Caio Yamamoto - RM: 569815

Rodger Costa Rios - RM: 571438

*Projeto acadêmico desenvolvido para a avaliação de Global Solution.*