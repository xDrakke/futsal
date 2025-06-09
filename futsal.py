import pandas as pd
import streamlit as st

# Leitura dos dados
grupo = pd.read_excel('grupos.xlsx')
jogos = pd.read_excel('partidas.xlsx')

# Função para processar cada grupo individualmente e garantir que saldo é GP - GC
def processa_grupo(grupo_df, grupo_nome):
    df = grupo_df[grupo_df['G'] == grupo_nome].copy()
    # Calcula saldo corretamente
    df['Sa'] = df['GP'] - df['GC']
    # Ordena por pontos e nome do time
    df = df.sort_values(['Po', 'Time'], ascending=[False, True]).reset_index(drop=True)
    # Cria coluna de Cls (1º, 2º, ...)
    df.insert(0, 'Cls', [f"{i}º" for i in range(1, len(df)+1)])
    # Ajusta capitalização para nomes dos times
    df['Time'] = df['Time'].str.title()
    # Garante tipos e formatação
    df['Po'] = df['Po'].astype(int)
    df['GP'] = df['GP'].astype(int)
    df['GC'] = df['GC'].astype(int)
    df['Sa'] = df['Sa'].apply(lambda x: f"{x:+d}")  # saldo sempre com sinal
    df['Jo'] = df['Jo'].astype(int)
    # Seleciona a ordem das colunas
    return df[['Cls', 'Time', 'Po', 'GP', 'GC', 'Sa', 'Jo']]

grupo_a = processa_grupo(grupo, 'A')
grupo_b = processa_grupo(grupo, 'B')
grupo_c = processa_grupo(grupo, 'C')
grupo_d = processa_grupo(grupo, 'D')

# Título principal
st.title("Campeonato de FutSal 2025")

# Legenda lateral colorida
st.sidebar.markdown("""
#### Legenda:
<span style='display: flex; flex-direction: column; gap: 4px; font-size:15px'>
  <span><span style='color:#1565c0; font-weight:700;'>Cls</span> - <span style='color:#ff0000;'>Lugar na tabela</span></span>
  <span><span style='color:#1565c0; font-weight:700;'>Time</span> - <span style='color:#ff0000;'>Equipe</span></span>
  <span><span style='color:#1565c0; font-weight:700;'>Po</span> - <span style='color:#ff0000;'>Pontos</span></span>
  <span><span style='color:#1565c0; font-weight:700;'>GP</span> - <span style='color:#ff0000;'>Gols Pró</span></span>
  <span><span style='color:#1565c0; font-weight:700;'>GC</span> - <span style='color:#ff0000;'>Gols Contra</span></span>
  <span><span style='color:#1565c0; font-weight:700;'>Sa</span> - <span style='color:#ff0000;'>Saldo (GP - GC)</span></span>
  <span><span style='color:#1565c0; font-weight:700;'>Jo</span> - <span style='color:#ff0000;'>Jogos</span></span>
</span>
""", unsafe_allow_html=True)

# Exibe as tabelas dos grupos (sem índice real)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Grupo A")
    st.dataframe(grupo_a, hide_index=True, use_container_width=True)
with col2:
    st.subheader("Grupo B")
    st.dataframe(grupo_b, hide_index=True, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.subheader("Grupo C")
    st.dataframe(grupo_c, hide_index=True, use_container_width=True)
with col4:
    st.subheader("Grupo D")
    st.dataframe(grupo_d, hide_index=True, use_container_width=True)

# Seção de jogos e resultados
st.title("Datas de Jogos e Resultados")

# Prepara e filtra os jogos
jogos['Status'] = jogos['Status'].fillna('Pendente').str.strip()
status_options = jogos['Status'].unique()
status_selecionado = st.selectbox('Filtrar por Status do Jogo', options=status_options)

# Para evitar SettingWithCopyWarning, use .copy()
jogos_filtrados = jogos[jogos['Status'] == status_selecionado].copy()

# Formata a data para o formato desejado (dia-mês abreviado com inicial maiúscula)
jogos_filtrados['Data'] = pd.to_datetime(jogos_filtrados['Data'], errors='coerce')
jogos_filtrados['Data'] = jogos_filtrados['Data'].dt.strftime('%d-%b')
jogos_filtrados['Data'] = jogos_filtrados['Data'].str.replace(
    r'-(.)', lambda m: '-' + m.group(1).upper(), regex=True)

# Ajusta nomes dos times para melhor visualização
jogos_filtrados['Time_1'] = jogos_filtrados['Time_1'].astype(str).str.title()
jogos_filtrados['Time_2'] = jogos_filtrados['Time_2'].astype(str).str.title()
if 'Rodada' in jogos_filtrados.columns:
    jogos_filtrados['Rodada'] = jogos_filtrados['Rodada'].astype(str)

# Exibe a tabela de jogos filtrados conforme o status
if status_selecionado == 'Finalizado':
    st.dataframe(
        jogos_filtrados[['Data', 'Time_1', 'RF', 'Time_2', 'Rodada']].reset_index(drop=True),
        hide_index=True, use_container_width=True
    )
else:
    jogos_filtrados_temp = jogos_filtrados.copy()
    jogos_filtrados_temp['RF'] = '-'
    st.dataframe(
        jogos_filtrados_temp[['Data', 'Time_1', 'RF', 'Time_2', 'Rodada']].reset_index(drop=True),
        hide_index=True, use_container_width=True
    )
