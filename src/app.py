import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Dashboard d'Educació Mundial", page_icon="🎓", layout="wide"
)

st.markdown(
    """
    <style>
        header[data-testid="stHeader"] {
            display: none !important;
        }
        div[data-testid="stDecoration"] {
            display: none !important;
        }
        .block-container {
            padding-top: 2rem !important;
        }
        .stApp {
            background-color: #ffffff !important;
            color: #0f172a !important;
        }
        
        .dashboard-title {
            text-align: center;
            color: #1e3a8a;
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 25px;
            letter-spacing: -0.5px;
        }
        
        .kpi-card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 16px 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e2e8f0;
            height: 100%;
        }
        
        .kpi-blue { border-left: 6px solid #2563eb; }
        .kpi-green { border-left: 6px solid #16a34a; }
        .kpi-amber { border-left: 6px solid #d97706; }
        
        .kpi-title {
            font-size: 15px;
            font-weight: 700;
            color: #334155;
            margin-bottom: 6px;
        }
        
        .kpi-value-blue { font-size: 30px; font-weight: 800; color: #2563eb; margin: 0; }
        .kpi-value-green { font-size: 30px; font-weight: 800; color: #16a34a; margin: 0; }
        .kpi-value-amber { font-size: 30px; font-weight: 800; color: #d97706; margin: 0; }
        
        .kpi-subtitle {
            font-size: 12px;
            color: #64748b;
            margin-top: 4px;
        }

        
        .footer-banner {
            background-color: #f0f9ff;
            border: 2px solid #38bdf8;
            border-radius: 30px;
            padding: 10px 20px;
            text-align: center;
            color: #0284c7;
            font-weight: 700;
            font-size: 14px;
            margin-top: 25px;
            margin-bottom: 15px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Primer pas: Carregar i preparar les dades
raw_data = pd.read_csv('data/literacy-rates-vs-average-years-of-schooling.csv')

data_paisos = raw_data.dropna(subset=['World region according to OWID']).copy()

data_literacy_education = data_paisos.dropna(
    subset=['Literacy rate', 'Average years of education for 15-64 years olds']
)

ultima_data_literacy_education = (
    data_literacy_education.sort_values('Year')
    .groupby('Entity')
    .last()
    .reset_index()
)

kpi_literacy_global = ultima_data_literacy_education['Literacy rate'].mean()
kpi_education_global = ultima_data_literacy_education[
    'Average years of education for 15-64 years olds'
].mean()

data_education = data_paisos.dropna(
    subset=['Average years of education for 15-64 years olds']
)
ultima_data_education = data_education.sort_values('Year').groupby('Entity').last()
primera_data_education = (
    data_education.sort_values('Year').groupby('Entity').first()
)

kpi_ultima_mitjana_education = ultima_data_education[
    'Average years of education for 15-64 years olds'
].mean()
kpi_primera_mitjana_education = primera_data_education[
    'Average years of education for 15-64 years olds'
].mean()

kpi_progres_historic_education = (
    kpi_ultima_mitjana_education - kpi_primera_mitjana_education
)

df_grafic_1 = ultima_data_literacy_education[[
    'Entity',
    'Literacy rate',
    'Average years of education for 15-64 years olds',
    'World region according to OWID',
    'Population',
]].copy()

df_grafic_2 = (
    ultima_data_education.reset_index()[[
        'Entity',
        'Code',
        'Year',
        'Average years of education for 15-64 years olds',
        'Literacy rate',
        'World region according to OWID',
    ]]
    .copy()
)

data_paisos['Decade'] = (data_paisos['Year'] // 10) * 10
df_grafic_3 = (
    data_paisos[
        (data_paisos['Decade'] >= 1960) & (data_paisos['Decade'] <= 2020)
    ]
    .groupby(['World region according to OWID', 'Decade'])
    .agg({
        'Average years of education for 15-64 years olds': 'mean',
        'Literacy rate': 'mean',
    })
    .reset_index()
)

data_recent = data_paisos[
    (data_paisos['Year'] >= 2000)
    & (data_paisos['Average years of education for 15-64 years olds'].notna())
].copy()
data_ultim_recent = (
    data_recent.sort_values('Year').groupby('Entity').last().reset_index()
)

llista_parelles = []
for region, group in data_ultim_recent.groupby(
    'World region according to OWID'
):
  max_row = group.loc[
      group['Average years of education for 15-64 years olds'].idxmax()
  ]
  min_row = group.loc[
      group['Average years of education for 15-64 years olds'].idxmin()
  ]

  llista_parelles.append({
      'Region': region,
      'Min_Country': min_row['Entity'],
      'Min_Value': min_row['Average years of education for 15-64 years olds'],
      'Max_Country': max_row['Entity'],
      'Max_Value': max_row['Average years of education for 15-64 years olds'],
      'Gap': (
          max_row['Average years of education for 15-64 years olds']
          - min_row['Average years of education for 15-64 years olds']
      ),
  })

df_grafic_4 = pd.DataFrame(llista_parelles).sort_values('Gap', ascending=False)

# Segon pas: Crear gràfics amb Plotly
DARK_BLUE = '#1e3a8a'

axis_style = dict(
    title_font=dict(color=DARK_BLUE, size=12, family='Arial'),
    tickfont=dict(color=DARK_BLUE, size=11, family='Arial'),
    gridcolor='#f1f5f9',
)

# Grafic 1: Taxa d'alfabetització vs anys d'escolarització
fig1 = px.scatter(
    df_grafic_1,
    x='Average years of education for 15-64 years olds',
    y='Literacy rate',
    color='World region according to OWID',
    size='Population',
    hover_name='Entity',
    trendline='ols',
    title="<b>Correlació: Anys d'Escolarització vs Alfabetització</b>",
)
fig1.update_layout(
    template='plotly_white',
    paper_bgcolor='#ffffff',
    plot_bgcolor='#ffffff',
    height=380,
    margin=dict(l=10, r=10, t=50, b=10),
    title_font=dict(color=DARK_BLUE, size=14),
    legend=dict(
        font=dict(color=DARK_BLUE, size=12),
        title=dict(font=dict(color=DARK_BLUE, size=12)),
    ),
)
fig1.update_xaxes(
    title_text="Anys Mitjans d'Educació", **axis_style
)
fig1.update_yaxes(
    title_text="Taxa d'Alfabetització (%)",range=[0, 102], **axis_style
)

# Grafic 2: Mapa mundial
fig2 = px.choropleth(
    df_grafic_2,
    locations='Code',
    color='Average years of education for 15-64 years olds',
    hover_name='Entity',
    color_continuous_scale='YlGnBu',
    title="<b>Distribució Mundial d'Anys d'Escolarització</b>",
)
fig2.update_layout(
    template='plotly_white',
    paper_bgcolor='#ffffff',
    plot_bgcolor='#ffffff',
    height=380,
    margin=dict(l=10, r=10, t=50, b=10),
    title_font=dict(color=DARK_BLUE, size=14),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        bgcolor='#ffffff',
        showland=True,
        landcolor='#f8fafc',
    ),
    coloraxis_colorbar=dict(
        title=dict(font=dict(color=DARK_BLUE, size=12)),
        tickfont=dict(color=DARK_BLUE, size=11),
    ),
)

# Grafic 3: Evolución temporal
fig3 = px.line(
    df_grafic_3,
    x='Decade',
    y='Average years of education for 15-64 years olds',
    color='World region according to OWID',
    markers=True,
    title="<b>Evolució Històrica per Continent (1960–2020)</b>",
)
fig3.update_layout(
    template='plotly_white',
    paper_bgcolor='#ffffff',
    plot_bgcolor='#ffffff',
    height=380,
    margin=dict(l=10, r=10, t=50, b=10),
    title_font=dict(color=DARK_BLUE, size=14),
    legend=dict(
        font=dict(color=DARK_BLUE, size=12),
        title=dict(font=dict(color=DARK_BLUE, size=12)),
    ),
)
fig3.update_xaxes(title_text='Dècada', **axis_style)
fig3.update_yaxes(
    title_text="Anys Mitjans d'Educació", range=[0, 16], **axis_style
)

# Grafic 4: Desigualtat educativa interna per continent
fig4 = go.Figure()

for _, row in df_grafic_4.iterrows():
  fig4.add_trace(
      go.Scatter(
          x=[row['Min_Value'], row['Max_Value']],
          y=[row['Region'], row['Region']],
          mode='lines',
          line=dict(color='#cbd5e1', width=3),
          showlegend=False,
          hoverinfo='none',
      )
  )

fig4.add_trace(
    go.Scatter(
        x=df_grafic_4['Min_Value'],
        y=df_grafic_4['Region'],
        mode='markers+text',
        name='Mínim',
        marker=dict(color='#e11d48', size=11),
        text=df_grafic_4['Min_Country']
        + ' ('
        + df_grafic_4['Min_Value'].round(1).astype(str)
        + 'a)',
        textposition='middle left',
        textfont=dict(color=DARK_BLUE, size=10),
        hovertemplate='<b>%{y} (Mínim)</b><br>%{text}<extra></extra>',
    )
)

fig4.add_trace(
    go.Scatter(
        x=df_grafic_4['Max_Value'],
        y=df_grafic_4['Region'],
        mode='markers+text',
        name='Màxim',
        marker=dict(color='#2563eb', size=11),
        text=df_grafic_4['Max_Country']
        + ' ('
        + df_grafic_4['Max_Value'].round(1).astype(str)
        + 'a)',
        textposition='middle right',
        textfont=dict(color=DARK_BLUE, size=10),
        hovertemplate='<b>%{y} (Màxim)</b><br>%{text}<extra></extra>',
    )
)

fig4.update_layout(
    title="<b>Desigualtat Educativa Interna per Continent</b>",
    template='plotly_white',
    paper_bgcolor='#ffffff',
    plot_bgcolor='#ffffff',
    height=380,
    margin=dict(l=10, r=10, t=50, b=10),
    title_font=dict(color=DARK_BLUE, size=14),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1,
        font=dict(color=DARK_BLUE, size=12),
        title=dict(font=dict(color=DARK_BLUE, size=12)),
    ),
)
fig4.update_xaxes(
    title_text="Anys Mitjans d'Escolarització", range=[0, 16], **axis_style
)
fig4.update_yaxes(title_text='', **axis_style)

# Tercer pas: Construir el dashboard amb Streamlit

st.markdown(
    "<div class='dashboard-title'>DASHBOARD D'EDUCACIÓ I ALFABETITZACIÓ MUNDIAL"
    '</div>',
    unsafe_allow_html=True,
)

# Fila de KPIs
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
  st.markdown(
      f"""
        <div class="kpi-card kpi-blue">
            <div class="kpi-title">Taxa d'Alfabetització Global</div>
            <div class="kpi-value-blue">{kpi_literacy_global:.1f} %</div>
            <div class="kpi-subtitle">Mitjana mundial actual de població adulta</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with kpi_col2:
  st.markdown(
      f"""
        <div class="kpi-card kpi-green">
            <div class="kpi-title">Anys Mitjans d'Escolarització</div>
            <div class="kpi-value-green">{kpi_education_global:.1f} anys</div>
            <div class="kpi-subtitle">Mitjana global per a adults (15–64 anys)</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with kpi_col3:
  st.markdown(
      f"""
        <div class="kpi-card kpi-amber">
            <div class="kpi-title">Progrés Històric Acumulat d'anys d'Escolarització</div>
            <div class="kpi-value-amber">+{kpi_progres_historic_education:.1f} anys</div>
            <div class="kpi-subtitle">Guany d'escolarització global des dels primers registres</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.write('')

# Matriz 2x2 de gráficos
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
  st.plotly_chart(fig1, use_container_width=True)
with row1_col2:
  st.plotly_chart(fig2, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
  st.plotly_chart(fig3, use_container_width=True)
with row2_col2:
  st.plotly_chart(fig4, use_container_width=True)

# Banner inferior
st.markdown(
    """
    <div class="footer-banner">
        Visualització Interactiva Activa: Feu clic a qualsevol regió o filtre per actualitzar la resta del panell | Font: Our World in Data (OWID)
    </div>
""",
    unsafe_allow_html=True,
)