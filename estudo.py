"""
DOSSIÊ DE SETORES — Ferramenta de estudo fundamentalista por setor.
Separada do RADAR: aqui o foco é entender o negócio, não o preço.
"""

import streamlit as st

st.set_page_config(
    page_title="Dossiê de Setores",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# ESTILOS — tema claro, tipografia de leitura
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #F7F6F2;
    color: #1A1A1A;
}

/* Fundo das áreas principais */
[data-testid="stAppViewContainer"] {
    background-color: #F7F6F2;
}
[data-testid="stMain"] {
    background-color: #F7F6F2;
}
.main .block-container {
    background-color: #F7F6F2;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #EEECEA;
    border-right: 1px solid #DDDBD6;
}
[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    background: transparent;
    border: none;
    color: #374151;
    text-align: left;
    padding: 10px 16px;
    border-radius: 8px;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.15s;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(180,140,20,0.10);
    color: #8B6914;
}

/* Títulos */
h1 { font-family: 'Playfair Display', serif !important; color: #111 !important; }
h2, h3 { font-family: 'Inter', sans-serif !important; font-weight: 700 !important; color: #111 !important; }

/* Cards base */
.dossie-card {
    background: #FFFFFF;
    border: 1px solid #E5E2DC;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 14px;
}
.dossie-card-gold {
    background: #FFFBEF;
    border: 1px solid #D4AF37;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 14px;
}

/* Label de seção */
.section-label {
    font-size: 0.70rem;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #6B4F10;
    margin-bottom: 10px;
}

/* Battle card — colunas de empresa */
.battle-header {
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding: 8px 0 6px 0;
    border-bottom: 2px solid;
    margin-bottom: 14px;
}
.battle-row-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #4B5563;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 4px;
}
.battle-row-value {
    font-size: 0.92rem;
    font-weight: 500;
    color: #1A1A1A;
    line-height: 1.5;
    margin-bottom: 14px;
}
.badge {
    display: inline-block;
    font-size: 0.68rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 20px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
.badge-green  { background: rgba(34,197,94,0.12);  color: #166534; }
.badge-yellow { background: rgba(180,140,20,0.12); color: #8B6914; }
.badge-red    { background: rgba(239,68,68,0.10);  color: #991B1B; }
.badge-blue   { background: rgba(37,99,235,0.10);  color: #1D4ED8; }

/* Ticker tag */
.ticker-tag {
    display: inline-block;
    background: #FFFBEF;
    border: 1px solid #D4AF37;
    color: #8B6914;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 6px;
    letter-spacing: 0.5px;
    margin-right: 6px;
    margin-bottom: 6px;
}

/* Divider */
.thin-divider {
    border: none;
    border-top: 1px solid #E5E2DC;
    margin: 20px 0;
}

/* Risco / vantagem pills */
.pill-vantagem {
    background: #F0FDF4;
    border-left: 3px solid #22C55E;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 0.875rem;
    color: #166534;
    line-height: 1.5;
}
.pill-risco {
    background: #FEF2F2;
    border-left: 3px solid #EF4444;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 0.875rem;
    color: #991B1B;
    line-height: 1.5;
}
.pill-neutro {
    background: #FFFBEF;
    border-left: 3px solid #D4AF37;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 0.875rem;
    color: #8B6914;
    line-height: 1.5;
}

/* Tab styling */
[data-testid="stTabs"] button {
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: #6B7280 !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #8B6914 !important;
    border-bottom-color: #D4AF37 !important;
}

/* Selectbox */
[data-testid="stSelectbox"] { color: #1A1A1A; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #F7F6F2; }
::-webkit-scrollbar-thumb { background: #DDDBD6; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CONTEÚDO — SETORES E EMPRESAS
# ─────────────────────────────────────────────────────────────────────────────

SETORES = {
    "📄 Papel & Celulose": {
        "tickers": ["KLBN4", "SUZB3", "RANI3"],
        "tagline": "Três empresas, três matérias-primas, três lógicas econômicas completamente distintas.",
        "logica": {
            "titulo": "O que move esse setor",
            "texto": (
                "O mercado agrupa Klabin, Suzano e Irani sob o mesmo rótulo — papel e celulose — "
                "mas são negócios com DNA diferente. O ponto de partida é a matéria-prima: "
                "o tipo de madeira determina o produto, o produto determina o cliente, "
                "o cliente determina a volatilidade e a exposição ao câmbio."
            ),
            "drivers": [
                ("Preço da celulose (BHKP)", "Commodity global cotada em dólar. Ciclos de 2–5 anos. "
                 "Afeta diretamente Suzano. Klabin é parcialmente protegida. Irani tem exposição zero."),
                ("Taxa de câmbio (R$/USD)", "Receita de exportação de celulose é em dólar. "
                 "Dólar alto beneficia exportadoras (Suzano e parte da Klabin). Irani é imune — vende em reais."),
                ("Preço das aparas (OCC)", "Papel reciclado é a matéria-prima principal da Irani. "
                 "Variou de R$610 a R$1.300/tonelada. Cada R$100/t impacta diretamente a margem."),
                ("Custo da madeira", "Plantio próprio (Eucalipto ~7 anos, Pinus ~15 anos) é a principal "
                 "vantagem de custo. Quem tem floresta própria tem previsibilidade de custo por décadas."),
                ("Demanda doméstica de embalagens", "Ligada ao consumo interno, e-commerce e agronegócio. "
                 "Cresceu 2–5% ao ano mesmo em recessão. É o driver da Irani e da embalagem da Klabin."),
            ],
        },
        "comparativo": {
            "dimensoes": [
                "Matéria-prima principal",
                "Produto final",
                "Exposição ao dólar",
                "Exposição ao ciclo de celulose",
                "Mercado principal",
                "Barreira de entrada",
                "Risco-chave",
                "Perfil do investidor",
            ],
            "empresas": {
                "SUZB3": {
                    "nome": "Suzano",
                    "cor": "#63B3ED",
                    "Matéria-prima principal": ("Eucalipto", "fibra curta, crescimento de 7 anos"),
                    "Produto final": ("Celulose BHKP", "commodity global, exportado em fardo"),
                    "Exposição ao dólar": ("Alta", "~100% da receita em dólar", "badge-green"),
                    "Exposição ao ciclo de celulose": ("Máxima", "é o produto único", "badge-red"),
                    "Mercado principal": ("Global", "Europa, China, EUA"),
                    "Barreira de entrada": ("Escala e custo", "maior produtora global, custo entre os mais baixos do mundo"),
                    "Risco-chave": ("Ciclo da celulose", "preço pode cair 30–40% num ciclo negativo"),
                    "Perfil do investidor": ("Commodities + câmbio", "quer exposição a dólar e ciclo global"),
                },
                "KLBN4": {
                    "nome": "Klabin",
                    "cor": "#D4AF37",
                    "Matéria-prima principal": ("Pinus + Eucalipto", "fibra longa e curta — única no Brasil"),
                    "Produto final": ("Papel + Embalagem + Celulose", "portfólio diversificado, 23 plantas"),
                    "Exposição ao dólar": ("Parcial", "exporta celulose, vende embalagem no Brasil", "badge-yellow"),
                    "Exposição ao ciclo de celulose": ("Moderada", "embalagem amorte o ciclo", "badge-yellow"),
                    "Mercado principal": ("Brasil + exportação", "líder em papel para embalagem no Brasil"),
                    "Barreira de entrada": ("Integração vertical + Pinus único", "única com floresta de pinus em escala industrial no Brasil"),
                    "Risco-chave": ("Alavancagem + Capex pesado", "projetos intensivos em capital pressionam caixa por anos"),
                    "Perfil do investidor": ("Diversificação no setor", "menos puro que Suzano, mais estável"),
                },
                "RANI3": {
                    "nome": "Irani",
                    "cor": "#86EFAC",
                    "Matéria-prima principal": ("Aparas (OCC) + Pinus próprio", "70% reciclado, 30% fibra virgem própria"),
                    "Produto final": ("Papelão ondulado + Papel kraft", "embalagem doméstica pura"),
                    "Exposição ao dólar": ("Mínima", "só 15% da receita é exportação", "badge-green"),
                    "Exposição ao ciclo de celulose": ("Zero", "não exporta celulose, não depende do preço global", "badge-green"),
                    "Mercado principal": ("Brasil", "frigoríficos, agro, e-commerce, alimentos"),
                    "Barreira de entrada": ("Integração + localização", "floresta própria de pinus em SC/RS + posição logística"),
                    "Risco-chave": ("Preço das aparas (OCC)", "insumo externo que pode subir 100%+ em eventos climáticos/logísticos"),
                    "Perfil do investidor": ("Brasil puro", "quer crescimento doméstico sem exposição a câmbio ou commodities"),
                },
            },
        },
        "perfis": {
            "SUZB3": {
                "nome": "Suzano",
                "fundacao": "1924",
                "sede": "São Paulo, SP",
                "tagline": "A maior produtora mundial de celulose de eucalipto. Puro jogo de escala, custo e câmbio.",
                "modelo": (
                    "A Suzano planta eucalipto, processa em celulose de fibra curta (BHKP) e exporta "
                    "praticamente tudo em dólar. O produto é commodity global — o preço é dado pelo mercado "
                    "internacional, não pela empresa. Sua vantagem é ser a produtora de menor custo do "
                    "mundo, graças à produtividade do eucalipto brasileiro (o mais rápido do planeta — "
                    "7 anos do plantio ao corte) e à escala das operações após a fusão com a Fibria em 2019."
                ),
                "receita": [
                    ("Celulose BHKP", "~85%", "fibra curta de eucalipto, commodity global"),
                    ("Papel", "~10%", "papel para imprimir/escrever e tissue"),
                    ("Outros", "~5%", "energia, madeira, derivados"),
                ],
                "vantagens": [
                    "Menor custo de produção de celulose do mundo — floresta tropical de crescimento ultrarrápido",
                    "Escala de 10,9 milhões de toneladas/ano — nenhum concorrente chega perto no eucalipto",
                    "Hedge natural: receita em dólar vs. custos em real",
                    "Certificação FSC de toda a base florestal — acesso a mercados premium na Europa",
                ],
                "riscos": [
                    "Preço da celulose cai 30–40% num ciclo negativo — resultado despenca junto",
                    "Dívida em dólar: variação cambial pode gerar prejuízo contábil mesmo com caixa saudável",
                    "Projeto Cerrado (nova fábrica em GO) aumentou alavancagem — deleveraging levará anos",
                    "Produto único: sem diversificação que amortize o ciclo",
                ],
                "barreira": "Escala e custo. Construir uma fábrica de celulose de 2 milhões de toneladas custa ~US$ 5 bilhões e leva 5 anos. Nenhum novo entrante consegue competir no custo sem décadas de plantio próprio.",
            },
            "KLBN4": {
                "nome": "Klabin",
                "fundacao": "1899",
                "sede": "São Paulo, SP",
                "tagline": "A única produtora brasileira com pinus em escala. Integração do bosque à caixa.",
                "modelo": (
                    "A Klabin é a empresa mais complexa do trio. Planta pinus (fibra longa) e eucalipto "
                    "(fibra curta), produz celulose, papel e embalagens — e converte parte em produtos "
                    "acabados como sacos industriais, caixas de papelão e cartões. Vende celulose para "
                    "exportação, mas uma fatia relevante da receita é embalagem doméstica, o que amortece "
                    "o ciclo de commodity. É a maior produtora e exportadora de papel para embalagem do Brasil."
                ),
                "receita": [
                    ("Embalagens (papelão ondulado, caixas)", "~45%", "mercado doméstico, relativamente estável"),
                    ("Papel para embalagem (kraft, cartão)", "~25%", "Brasil e exportação"),
                    ("Celulose (fibra longa e fluff)", "~20%", "exportação, commodity"),
                    ("Sacos industriais", "~10%", "cimento, fertilizante, Brasil"),
                ],
                "vantagens": [
                    "Única produtora de pinus em escala industrial no Brasil — fibra longa que ninguém mais tem",
                    "Diversificação de produto: embalagem amorte o ciclo de celulose",
                    "Integração vertical completa: da floresta ao produto acabado",
                    "Celulose fluff (para fraldas e absorventes) — nicho de margem alta e demanda crescente",
                ],
                "riscos": [
                    "Capex intensivo e constante — projetos de expansão pressionam caixa por anos seguidos",
                    "Alavancagem historicamente alta (4–5x EBITDA em fases de investimento)",
                    "Complexidade operacional: 23 plantas, múltiplos produtos, margens diferentes por linha",
                    "Pinus tem ciclo de 15 anos — planejamento florestal é de altíssimo prazo",
                ],
                "barreira": "O pinus. Ninguém mais tem floresta de pinus em escala no Brasil. Plantar hoje para colher em 15 anos é uma barreira de entrada que efetivamente fecha o mercado para novos entrantes na fibra longa.",
            },
            "RANI3": {
                "nome": "Irani (Celulose Irani)",
                "fundacao": "1941",
                "sede": "Campina da Alegria, SC",
                "tagline": "A única empresa de embalagens sustentáveis pura listada na B3. Brasil puro, sem câmbio.",
                "modelo": (
                    "A Irani não é uma produtora de celulose de mercado. É uma fabricante de embalagens "
                    "que produz sua própria celulose — e usa tudo internamente. Pega aparas (papel "
                    "reciclado descartado por supermercados, e-commerce e frigoríficos), transforma em "
                    "papel kraft e papelão ondulado, e vende para o mercado doméstico. Também tem florestas "
                    "próprias de pinus no Sul (SC e RS), de onde extrai fibra virgem para complementar "
                    "a produção e resina de terebintina como subproduto (usada em tintas a óleo)."
                ),
                "receita": [
                    ("Embalagens de papelão ondulado", "~57%", "frigoríficos, agro, e-commerce, alimentos"),
                    ("Papel para embalagens (kraft)", "~37%", "sacolas, sacos, papel multiwall — Brasil e 15% exportação"),
                    ("Resinas e madeira", "~6%", "terebintina e venda de madeira — subproduto do pinus"),
                ],
                "vantagens": [
                    "Zero exposição ao câmbio e ao ciclo global de celulose — negócio 100% doméstico",
                    "Demanda por embalagem de papelão cresceu 2–5%/ano mesmo em recessão — setor defensivo",
                    "Floresta própria de pinus garante parte do custo estável e previsível",
                    "Capacidade de repasse de preço: quem compra caixa de papelão não tem substituto fácil",
                    "Plataforma Gaia (>R$1 bi investido): ganhos de eficiência ainda sendo colhidos",
                ],
                "riscos": [
                    "Preço das aparas (OCC): insumo externo que representa ~30% do custo — variou de R$610 a R$1.300/t",
                    "Eventos climáticos no Sul (enchentes RS/SC) disruptam o fornecimento de aparas",
                    "Small cap — menor liquidez, menor cobertura de analistas, mais suscetível a humor de mercado",
                    "Capex pesado recente (Gaia) ainda sendo digerido; FCF pressiona no curto prazo",
                ],
                "barreira": "Integração + localização + relacionamento com clientes industriais. No mercado de embalagens, o cliente (frigorífico, agro) não troca de fornecedor facilmente — logística, especificação técnica e volume criam um lock-in operacional relevante.",
            },
        },
    },
    # Placeholder — próximos setores aqui
    "🏦 Bancos": {"tickers": [], "em_construcao": True},
    "🛡️ Seguradoras": {"tickers": [], "em_construcao": True},
    "⚡ Utilities Elétricas": {"tickers": [], "em_construcao": True},
    "🏗️ Incorporadoras": {"tickers": [], "em_construcao": True},
    "💧 Saneamento": {"tickers": [], "em_construcao": True},
    "⛏️ Mineração": {"tickers": [], "em_construcao": True},
    "🛢️ Petróleo & Gás": {"tickers": [], "em_construcao": True},
    "🔩 Autopeças & Industrial": {"tickers": [], "em_construcao": True},
}


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 24px 16px 8px 16px;'>
        <div style='font-family: Playfair Display, serif; font-size: 1.3rem; font-weight: 800;
                    color: #1A1A1A; line-height: 1.2; margin-bottom: 4px;'>
            Dossiê de Setores
        </div>
        <div style='font-size: 0.72rem; color: #4B5563; letter-spacing: 0.5px;'>
            Estudo fundamentalista comparado
        </div>
    </div>
    <hr style='border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 12px 0;'>
    <div style='font-size: 0.65rem; font-weight: 700; letter-spacing: 1px;
                text-transform: uppercase; color: #374151; padding: 0 16px 8px 16px;'>
        Setores
    </div>
    """, unsafe_allow_html=True)

    if "setor_ativo" not in st.session_state:
        st.session_state.setor_ativo = "📄 Papel & Celulose"

    for nome_setor in SETORES:
        dados = SETORES[nome_setor]
        em_construcao = dados.get("em_construcao", False)
        label = nome_setor if not em_construcao else f"{nome_setor}  ·  em breve"
        if st.button(label, key=f"btn_{nome_setor}", disabled=em_construcao):
            st.session_state.setor_ativo = nome_setor
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='padding: 0 16px; font-size: 0.68rem; color: #374151; line-height: 1.6;'>
        Nenhuma empresa é igual à outra.<br>
        Aqui você estuda o negócio, não o preço.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CONTEÚDO PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
setor = st.session_state.setor_ativo
dados_setor = SETORES[setor]

# Header do setor
st.markdown(f"""
<div style='padding: 32px 0 20px 0; border-bottom: 1px solid rgba(255,255,255,0.06); margin-bottom: 28px;'>
    <div style='font-size: 0.70rem; font-weight: 700; letter-spacing: 1.5px;
                text-transform: uppercase; color: #8B6914; margin-bottom: 8px;'>
        Dossiê · {setor}
    </div>
    <h1 style='font-size: 2.0rem; color: #1A1A1A; margin: 0 0 10px 0; line-height: 1.2;'>
        {setor}
    </h1>
    <div style='font-size: 0.95rem; color: #374151; max-width: 680px; line-height: 1.6;'>
        {dados_setor.get("tagline", "")}
    </div>
    <div style='margin-top: 14px;'>
        {"".join(f"<span class='ticker-tag'>{t}</span>" for t in dados_setor.get("tickers", []))}
    </div>
</div>
""", unsafe_allow_html=True)

# Abas principais
tab1, tab2, tab3 = st.tabs(["🧠  Lógica do Setor", "⚔️  Comparativo", "🔍  Perfil Individual"])


# ─── ABA 1: LÓGICA DO SETOR ───────────────────────────────────────────────
with tab1:
    logica = dados_setor.get("logica", {})

    st.markdown(f"""
    <div class='section-label'>O que você precisa entender antes de qualquer número</div>
    <div class='dossie-card-gold'>
        <div style='font-size: 1.0rem; color: #1A1A1A; line-height: 1.7;'>
            {logica.get("texto", "")}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Drivers do setor — o que muda o resultado</div>",
                unsafe_allow_html=True)

    for driver, descricao in logica.get("drivers", []):
        st.markdown(f"""
        <div class='dossie-card' style='padding: 16px 20px;'>
            <div style='font-size: 0.80rem; font-weight: 700; color: #6B4F10;
                        margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;'>
                {driver}
            </div>
            <div style='font-size: 0.88rem; color: #374151; line-height: 1.6;'>
                {descricao}
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── ABA 2: COMPARATIVO (BATTLE CARD) ────────────────────────────────────
with tab2:
    comp = dados_setor.get("comparativo", {})
    empresas = comp.get("empresas", {})
    dimensoes = comp.get("dimensoes", [])

    if not empresas:
        st.info("Comparativo ainda não disponível para este setor.")
    else:
        tickers_comp = list(empresas.keys())
        # Header das colunas
        col_label, *cols_emp = st.columns([1.1] + [1] * len(tickers_comp))

        col_label.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        for col, tk in zip(cols_emp, tickers_comp):
            emp = empresas[tk]
            col.markdown(f"""
            <div class='battle-header' style='border-color: {emp["cor"]}; color: {emp["cor"]};'>
                {tk}<br>
                <span style='font-size: 0.62rem; font-weight: 500; color: #374151; letter-spacing: 0;
                            text-transform: none;'>
                    {emp["nome"]}
                </span>
            </div>
            """, unsafe_allow_html=True)

        # Linhas de comparação
        for dim in dimensoes:
            col_label, *cols_emp = st.columns([1.1] + [1] * len(tickers_comp))
            col_label.markdown(f"""
            <div class='battle-row-label' style='padding-top: 4px;'>{dim}</div>
            """, unsafe_allow_html=True)
            for col, tk in zip(cols_emp, tickers_comp):
                val = empresas[tk].get(dim, ("—", ""))
                if isinstance(val, tuple) and len(val) == 3:
                    # Com badge
                    badge_class = val[2]
                    col.markdown(f"""
                    <div class='battle-row-value'>
                        <span class='badge {badge_class}'>{val[0]}</span><br>
                        <span style='font-size: 0.80rem; color: #374151;'>{val[1]}</span>
                    </div>
                    """, unsafe_allow_html=True)
                elif isinstance(val, tuple) and len(val) == 2:
                    col.markdown(f"""
                    <div class='battle-row-value'>
                        <strong style='font-size: 0.88rem;'>{val[0]}</strong><br>
                        <span style='font-size: 0.80rem; color: #374151;'>{val[1]}</span>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    col.markdown(f"<div class='battle-row-value'>{val}</div>",
                                 unsafe_allow_html=True)

            st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)


# ─── ABA 3: PERFIL INDIVIDUAL ─────────────────────────────────────────────
with tab3:
    perfis = dados_setor.get("perfis", {})
    if not perfis:
        st.info("Perfis individuais ainda não disponíveis para este setor.")
    else:
        ticker_sel = st.selectbox(
            "Empresa:",
            list(perfis.keys()),
            format_func=lambda t: f"{t} — {perfis[t]['nome']}",
        )
        p = perfis[ticker_sel]

        # Cabeçalho do perfil
        st.markdown(f"""
        <div style='margin: 16px 0 24px 0; padding: 24px; background: #FFFFFF;
                    border: 1px solid #E5E2DC; border-radius: 12px;'>
            <div style='font-size: 0.65rem; font-weight: 700; color: #374151;
                        letter-spacing: 1px; text-transform: uppercase; margin-bottom: 6px;'>
                {ticker_sel} · Fundada em {p.get("fundacao","?")} · {p.get("sede","")}
            </div>
            <div style='font-size: 1.4rem; font-weight: 800; color: #1A1A1A;
                        margin-bottom: 6px; font-family: Playfair Display, serif;'>
                {p["nome"]}
            </div>
            <div style='font-size: 0.90rem; color: #8B6914; font-style: italic;'>
                {p.get("tagline","")}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Como funciona o negócio
        st.markdown("<div class='section-label'>Como funciona o negócio</div>",
                    unsafe_allow_html=True)
        st.markdown(f"""
        <div class='dossie-card'>
            <div style='font-size: 0.90rem; color: #111827; line-height: 1.75;'>
                {p.get("modelo","")}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # De onde vem a receita
        st.markdown("<div class='section-label' style='margin-top:20px;'>De onde vem a receita</div>",
                    unsafe_allow_html=True)
        for segmento, pct, detalhe in p.get("receita", []):
            st.markdown(f"""
            <div style='display: flex; align-items: flex-start; gap: 16px;
                        padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05);'>
                <div style='min-width: 52px; text-align: right; font-size: 1.1rem;
                            font-weight: 800; color: #8B6914; padding-top: 1px;'>
                    {pct}
                </div>
                <div>
                    <div style='font-size: 0.88rem; font-weight: 600; color: #1A1A1A;
                                margin-bottom: 2px;'>{segmento}</div>
                    <div style='font-size: 0.80rem; color: #374151;'>{detalhe}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        # Vantagens competitivas
        with c1:
            st.markdown("<div class='section-label' style='margin-top:24px;'>Vantagens competitivas</div>",
                        unsafe_allow_html=True)
            for v in p.get("vantagens", []):
                st.markdown(f"<div class='pill-vantagem'>✦ {v}</div>", unsafe_allow_html=True)

        # Riscos
        with c2:
            st.markdown("<div class='section-label' style='margin-top:24px;'>Riscos principais</div>",
                        unsafe_allow_html=True)
            for r in p.get("riscos", []):
                st.markdown(f"<div class='pill-risco'>⚠ {r}</div>", unsafe_allow_html=True)

        # Barreira de entrada
        st.markdown("<div class='section-label' style='margin-top:20px;'>Barreira de entrada</div>",
                    unsafe_allow_html=True)
        st.markdown(f"""
        <div class='pill-neutro'>
            🔒 {p.get("barreira","")}
        </div>
        """, unsafe_allow_html=True)
