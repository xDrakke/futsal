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
st.markdown("<h1 style='color: MediumBlue;'>Campeonato de FutSal 2025</h1>", unsafe_allow_html=True)

# Legenda lateral colorida

def highlight_top_two(df):
    html = "<table style='border-collapse:collapse;'>"
    # Cabeçalho
    html += "<tr>" + "".join([f"<th style='padding:6px'>{col}</th>" for col in df.columns]) + "</tr>"
    # Linhas
    for i, row in df.iterrows():
        if i < 2:
            html += "<tr>" + "".join([f"<td style='font-weight:bold; padding:6px'>{cell}</td>" for cell in row]) + "</tr>"
        else:
            html += "<tr>" + "".join([f"<td style='padding:6px'>{cell}</td>" for cell in row]) + "</tr>"
    html += "</table>"
    return html


# Exibe as tabelas dos grupos (sem índice real)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h6 style='color: lightgreen;'>Grupo A</h6>", unsafe_allow_html=True)
    styled_df_a = grupo_a.style.set_properties(**{'background-color': '#343a40', 'color': 'white', 'font-size':'12px'})
    styled_df_a = styled_df_a.set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#4CAF50'), ('color', 'white'), ('font-weight', 'bold')]}
])
    html_table = styled_df_a.hide(axis="index").to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)
    
with col2:
    st.markdown("<h6 style='color: lightgreen;'>Grupo B</h6>", unsafe_allow_html=True)
    styled_df_b = grupo_b.style.set_properties(**{'background-color': '#343a40', 'color': 'white', 'font-size':'12px'})
    styled_df_b = styled_df_b.set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#4CAF50'), ('color', 'white'), ('font-weight', 'bold')]}
])
    html_table = styled_df_b.hide(axis="index").to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)

st.markdown("""
<span style='display: flex; flex-direction: row ; gap: 2px; font-size:10px'>
  <span><span style='color:#1565c0; font-weight:350;'>Cls</span> - <span style='color:#ff0000;'>Lugar na tabela</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Time</span> - <span style='color:#ff0000;'>Equipe</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Po</span> - <span style='color:#ff0000;'>Pontos</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>GP</span> - <span style='color:#ff0000;'>Gols Pró</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>GC</span> - <span style='color:#ff0000;'>Gols Sofridos</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Sa</span> - <span style='color:#ff0000;'>Saldo (GP - GC)</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Jo</span> - <span style='color:#ff0000;'>Jogos</span></span>
</span>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown("<h6 style='color: lightgreen;'>Grupo C</h6>", unsafe_allow_html=True)
    styled_df_c = grupo_c.style.set_properties(**{'background-color': '#343a40', 'color': 'white', 'font-size':'12px'})
    styled_df_c = styled_df_c.set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#4CAF50'), ('color', 'white'), ('font-weight', 'bold')]}
])
    html_table = styled_df_c.hide(axis="index").to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)

with col4:
    st.markdown("<h6 style='color: lightgreen;'>Grupo D</h6>", unsafe_allow_html=True)
    styled_df_d = grupo_d.style.set_properties(**{'background-color': '#343a40', 'color': 'white', 'font-size':'12px'})
    styled_df_d = styled_df_d.set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#4CAF50'), ('color', 'white'), ('font-weight', 'bold')]}
])
    html_table = styled_df_d.hide(axis="index").to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)

st.markdown("""
<span style='display: flex; flex-direction: row ; gap: 2px; font-size:10px'>
  <span><span style='color:#1565c0; font-weight:350;'>Cls</span> - <span style='color:#ff0000;'>Lugar na tabela</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Time</span> - <span style='color:#ff0000;'>Equipe</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Po</span> - <span style='color:#ff0000;'>Pontos</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>GP</span> - <span style='color:#ff0000;'>Gols Pró</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>GC</span> - <span style='color:#ff0000;'>Gols Sofridos</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Sa</span> - <span style='color:#ff0000;'>Saldo (GP - GC)</span></span>
  <span><span style='color:#1565c0; font-weight:350;'>Jo</span> - <span style='color:#ff0000;'>Jogos</span></span>
</span>
""", unsafe_allow_html=True)

# Seção de jogos e resultados
st.markdown("<h2 style='color: DarkOrange;'>Datas de Jogos e Resultados</h2>", unsafe_allow_html=True)

# Prepara e filtra os jogos
jogos['Status'] = jogos['Status'].fillna('Pendente').str.strip()
status_options = jogos['Status'].unique()
status_selecionado = st.selectbox('Veja os resultados ou consulte as datas dos próximos jogos', options=status_options)

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
