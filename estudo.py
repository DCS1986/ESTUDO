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
    "🏦 Bancos": {
        "tickers": ["ITUB4", "BBAS3", "BBDC3", "BPAC11", "SANB3", "ABCB4", "BRSR6", "BMGB4"],
        "tagline": "Mesma licença bancária, oito modelos de negócio completamente distintos. Quem entende a diferença lê o balanço em 10 minutos.",
        "logica": {
            "titulo": "O que move o setor bancário",
            "texto": (
                "Todo banco capta dinheiro a um custo e empresta a um preço maior — a diferença é o spread. "
                "Mas a forma como cada banco capta, para quem empresta e com qual risco é onde os modelos "
                "divergem radicalmente. ITUB e Bradesco são bancões de varejo. BBAS domina o agro e o "
                "funcionalismo. BTG é banco de investimento e wealth. ABC serve exclusivamente empresas. "
                "Banrisul é o banco do RS. BMG só faz consignado para aposentados do INSS. Entender o nicho "
                "de cada um é entender por que um vai bem quando o outro vai mal."
            ),
            "drivers": [
                ("Spread (NIM — Margem Financeira Líquida)", "A diferença entre o juro cobrado do cliente e o juro pago na captação. "
                 "Selic alta aumenta o custo de captação, mas nem sempre aumenta o spread — depende do perfil da carteira. "
                 "Consignado tem spread baixo mas risco também baixo. Crédito pessoal tem spread alto e inadimplência alta."),
                ("Inadimplência (NPL)", "O grande vilão do resultado bancário. Varia por segmento: consignado INSS tem inadimplência "
                 "< 3%, crédito pessoal pode chegar a 10-15%. Banco com carteira concentrada em baixa renda sofre mais em recessão."),
                ("Selic e ciclo de juros", "Juro alto comprime a demanda por crédito mas remunera melhor o PL e a tesouraria. "
                 "Cada banco reage diferente: BTG ama juro alto (tesouraria e renda fixa); varejo de baixa renda sofre "
                 "(inadimplência sobe, demanda cai)."),
                ("Eficiência operacional", "Custo de servir o cliente. Banco digital tem custo por transação próximo de zero. "
                 "Bancão com 4.000 agências tem custo fixo pesado. O índice de eficiência (despesas/receitas) é o termômetro — "
                 "abaixo de 40% é excelente; acima de 60% é ineficiente."),
                ("Qualidade e crescimento da carteira de crédito", "Carteira crescendo é bom sinal, mas só se a qualidade "
                 "se mantiver. O BB errou ao crescer no agro sem critérios — a conta chegou no 1T26 com inadimplência "
                 "saltando de 1% para 6%. Crescimento sem qualidade é receita de provisão futura."),
                ("ROE (Retorno sobre Patrimônio)", "A métrica-rei do setor. Acima de 20% é excepcional (BTG, Itaú). "
                 "Entre 15-20% é sólido. Abaixo de 12% o banco não cobre o custo de capital e destrói valor. "
                 "Bradesco ficou abaixo do custo de capital por dois anos — foi a crise de 2023-2024."),
            ],
        },
        "comparativo": {
            "dimensoes": [
                "Modelo de negócio",
                "Cliente principal",
                "Principal produto de crédito",
                "Exposição ao ciclo econômico",
                "Exposição à política/regulação",
                "Sensibilidade à Selic",
                "ROE atual (ref.)",
                "Risco principal",
                "Perfil do investidor",
            ],
            "empresas": {
                "ITUB4": {
                    "nome": "Itaú Unibanco",
                    "cor": "#F97316",
                    "Modelo de negócio": ("Varejo premium + atacado + seguros", "maior banco privado da AL"),
                    "Cliente principal": ("Alta e média renda", "6 de cada 10 brasileiros de alta renda são clientes"),
                    "Principal produto de crédito": ("Cartão + crédito imobiliário + consignado privado", "mix diversificado"),
                    "Exposição ao ciclo econômico": ("Moderada", "foco em alta renda protege da inadimplência", "badge-yellow"),
                    "Exposição à política/regulação": ("Baixa", "banco privado, sem interferência estatal", "badge-green"),
                    "Sensibilidade à Selic": ("Alta positiva", "tesouraria + PL remunera bem; spread se mantém", "badge-green"),
                    "ROE atual (ref.)": ("~24-26%", "o maior entre os incumbentes"),
                    "Risco principal": ("Competição com fintechs e digitalização do varejo massificado", ""),
                    "Perfil do investidor": ("Qualidade e crescimento previsível", "paga prêmio, mas entrega consistência"),
                },
                "BBAS3": {
                    "nome": "Banco do Brasil",
                    "cor": "#EAB308",
                    "Modelo de negócio": ("Banco estatal universal", "líder em agro, funcionalismo e gestão de ativos"),
                    "Cliente principal": ("Agricultor, servidor público, governo", "processa metade das folhas do setor público"),
                    "Principal produto de crédito": ("Crédito rural + consignado público + crédito governo", "53% do crédito rural do Brasil"),
                    "Exposição ao ciclo econômico": ("Alta", "agro é cíclico — inadimplência rural saltou de 1% para 6% em 2026", "badge-red"),
                    "Exposição à política/regulação": ("Muito alta", "estatal — governo pode intervir na política de crédito", "badge-red"),
                    "Sensibilidade à Selic": ("Alta", "PL e tesouraria remuneram bem; agro sensível a custo de captação", "badge-yellow"),
                    "ROE atual (ref.)": ("~7-8% (1T26)", "pressionado pela crise do agro — era 16% em 2025"),
                    "Risco principal": ("Interferência política + concentração no agro", "inadimplência rural 2025-2026"),
                    "Perfil do investidor": ("Dividendos + tese contrarian", "compra desconto e upside de normalização"),
                },
                "BBDC3": {
                    "nome": "Bradesco",
                    "cor": "#EF4444",
                    "Modelo de negócio": ("Varejo universal", "terceiro maior banco privado, em reestruturação"),
                    "Cliente principal": ("Massa + média renda + PME", "historicamente forte no interior do Brasil"),
                    "Principal produto de crédito": ("Crédito pessoal + PME + consignado", "diversificado mas com foco no varejo"),
                    "Exposição ao ciclo econômico": ("Alta", "massa e PME sofrem mais em recessão e juro alto", "badge-red"),
                    "Exposição à política/regulação": ("Baixa", "banco privado", "badge-green"),
                    "Sensibilidade à Selic": ("Negativa parcial", "custo de captação sobe; cliente de menor renda inadimple mais", "badge-red"),
                    "ROE atual (ref.)": ("~14-15%", "recuperando — era abaixo do custo de capital em 2023-2024"),
                    "Risco principal": ("Execução da reestruturação e concorrência de fintechs no varejo massificado", ""),
                    "Perfil do investidor": ("Tese de turnaround", "aposta na recuperação do ROE; maior upside se entregar"),
                },
                "BPAC11": {
                    "nome": "BTG Pactual",
                    "cor": "#3B82F6",
                    "Modelo de negócio": ("Banco de investimento + wealth + crédito corporativo", "único modelo de atacado puro entre os grandes"),
                    "Cliente principal": ("Grandes empresas + ultra-high net worth", "wealth: R$1,28 tri sob gestão"),
                    "Principal produto de crédito": ("Corporate lending + M&A + mercado de capitais", "crescimento de 22% a/a na carteira"),
                    "Exposição ao ciclo econômico": ("Moderada", "mercado de capitais oscila, mas recorrência do wealth protege", "badge-yellow"),
                    "Exposição à política/regulação": ("Baixa", "banco privado, foco em atacado", "badge-green"),
                    "Sensibilidade à Selic": ("Positiva", "juro alto favorece renda fixa, tesouraria e gestão de ativos", "badge-green"),
                    "ROE atual (ref.)": ("~26-27%", "o mais alto do setor — modelo asset-light e alta alavancagem operacional"),
                    "Risco principal": ("Volatilidade de mercado comprime investment banking; já negocia a P/VP elevado", ""),
                    "Perfil do investidor": ("Crescimento + qualidade", "paga prêmio alto; dividend yield baixo mas crescimento forte"),
                },
                "SANB3": {
                    "nome": "Santander Brasil",
                    "cor": "#EF4444",
                    "Modelo de negócio": ("Varejo universal com matriz global", "único banco internacional com escala no Brasil"),
                    "Cliente principal": ("Varejo PF + PME + atacado", "foco crescente em alta renda"),
                    "Principal produto de crédito": ("Crédito imobiliário + cartão + PME", "diversificado"),
                    "Exposição ao ciclo econômico": ("Alta", "PME e varejo sofrem em recessão e juro elevado", "badge-red"),
                    "Exposição à política/regulação": ("Baixa/Moderada", "banco privado, mas depende da matriz espanhola", "badge-yellow"),
                    "Sensibilidade à Selic": ("Negativa parcial", "custo de captação sobe mais rápido que o spread no varejo", "badge-yellow"),
                    "ROE atual (ref.)": ("~13-15%", "abaixo dos pares — ROE mais fraco do grupo dos grandes privados"),
                    "Risco principal": ("ROE estruturalmente mais baixo; dependência de decisões da matriz espanhola", ""),
                    "Perfil do investidor": ("Dividendos + recuperação", "valuation descontado, mas exige provas de melhora"),
                },
                "ABCB4": {
                    "nome": "ABC Brasil",
                    "cor": "#22C55E",
                    "Modelo de negócio": ("Banco de atacado puro", "sem varejo — 100% crédito para médias e grandes empresas"),
                    "Cliente principal": ("Médias e grandes empresas (middle + corporate)", "sem pessoa física"),
                    "Principal produto de crédito": ("Crédito corporativo + trade finance + derivativos", "inadimplência histórica < 1%"),
                    "Exposição ao ciclo econômico": ("Moderada", "atacado é mais resiliente que varejo; cliente corporativo é mais solvente", "badge-yellow"),
                    "Exposição à política/regulação": ("Baixa", "banco privado, controlado pelo Arab Banking Corporation", "badge-green"),
                    "Sensibilidade à Selic": ("Positiva", "juro alto aumenta spread do crédito corporativo; PL remunera bem", "badge-green"),
                    "ROE atual (ref.)": ("~14-16%", "consistente e previsível — modelo de negócio não muda com o ciclo"),
                    "Risco principal": ("Concentração no atacado — grandes perdas pontuais impactam mais que a inadimplência pulverizada do varejo", ""),
                    "Perfil do investidor": ("Qualidade e estabilidade", "dividend yield consistente; cresce sem surpresas"),
                },
                "BRSR6": {
                    "nome": "Banrisul",
                    "cor": "#A78BFA",
                    "Modelo de negócio": ("Banco regional estatal gaúcho", "vive de funcionalismo público do RS"),
                    "Cliente principal": ("Servidor público e varejo do RS", "294 mil servidores estaduais na folha"),
                    "Principal produto de crédito": ("Consignado público + varejo PF + PME regional", "folha do Estado é o coração do negócio"),
                    "Exposição ao ciclo econômico": ("Moderada", "consignado público é defensivo; PME regional é mais sensível", "badge-yellow"),
                    "Exposição à política/regulação": ("Muito alta", "estatal — governo do RS controla e renova (ou não) o contrato da folha", "badge-red"),
                    "Sensibilidade à Selic": ("Positiva moderada", "juro alto aumenta spread; mas custo de captação também sobe", "badge-yellow"),
                    "ROE atual (ref.)": ("~7-9%", "pressionado — ROE mais baixo do grupo; abaixo do custo de capital"),
                    "Risco principal": ("Dependência total do governo gaúcho; contrato de folha renovado a custo crescente (R$1,26 bi por 5 anos)", ""),
                    "Perfil do investidor": ("Dividendos regionais", "dividend yield atrativo mas com risco político e de execução"),
                },
                "BMGB4": {
                    "nome": "Banco BMG",
                    "cor": "#F97316",
                    "Modelo de negócio": ("Banco mono-produto de consignado INSS", "88% da carteira é aposentado/pensionista"),
                    "Cliente principal": ("Aposentados e pensionistas do INSS", "segmento com menor inadimplência do Brasil"),
                    "Principal produto de crédito": ("Consignado INSS + cartão consignado", "desconto direto no benefício"),
                    "Exposição ao ciclo econômico": ("Muito baixa", "benefício do INSS não cai em recessão — renda garantida", "badge-green"),
                    "Exposição à política/regulação": ("Alta", "governo regula a taxa máxima do consignado INSS (hoje 1,85%/mês)", "badge-red"),
                    "Sensibilidade à Selic": ("Negativa", "teto de taxa regulado não sobe com a Selic — spread comprime", "badge-red"),
                    "ROE atual (ref.)": ("~10-12%", "limitado pelo teto regulatório da taxa"),
                    "Risco principal": ("Teto regulatório de juros + CPI do INSS investigando fraudes no consignado (biometria obrigatória)", ""),
                    "Perfil do investidor": ("Dividendos defensivos", "carteira resiliente, mas crescimento limitado pelo regulador"),
                },
            },
        },
        "perfis": {
            "ITUB4": {
                "nome": "Itaú Unibanco",
                "fundacao": "1945 (fusão Itaú+Unibanco em 2008)",
                "sede": "São Paulo, SP",
                "tagline": "O maior banco privado da América Latina. Disciplina de capital, foco em alta renda e o melhor ROE entre os incumbentes.",
                "modelo": (
                    "O Itaú opera em quatro frentes: varejo (conta corrente, cartão, crédito e seguros para pessoas físicas), "
                    "atacado (crédito para grandes empresas, mercado de capitais, tesouraria), gestão de ativos (fundos, previdência) "
                    "e atividades internacionais (América Latina). O diferencial não é o tamanho — é a seletividade. O Itaú "
                    "deliberadamente abandonou segmentos de menor renda e maior inadimplência, concentrando a carteira em alta e "
                    "média renda. 6 de cada 10 brasileiros de alta renda têm relacionamento com o banco. Isso gera spreads "
                    "melhores, inadimplência menor e fee de serviços mais alto (asset management, corretagem, seguros). "
                    "No 1T26 entregou lucro recorrente de R$ 12,3 bi e ROE de 24,8% — o mais alto entre os incumbentes."
                ),
                "receita": [
                    ("Margem financeira (NII)", "~50%", "spread de crédito e resultado de tesouraria"),
                    ("Receitas de serviços e tarifas", "~25%", "cartão, asset management, advisory, corretagem"),
                    ("Seguros", "~12%", "Itaú Seguros — vida, prestamista, imobiliário"),
                    ("Outros", "~13%", "câmbio, derivativos, international"),
                ],
                "vantagens": [
                    "Melhor ROE entre os bancões incumbentes (~24-26%) — sustentado por décadas, não é pico de ciclo",
                    "Foco na alta renda cria um flywheel: menor inadimplência → menor provisão → mais capital disponível para crescer",
                    "Escala de distribuição: rede própria + parcerias + digital permitem cross-sell sem aumentar custo proporcional",
                    "Transformação digital avançada — 75% das transações já são digitais, com meta de 75% dos clientes em modelo digital-first até 2027",
                    "Seguros e asset management são negócios capital-light dentro do banco, com margens muito mais altas que o crédito",
                ],
                "riscos": [
                    "Valuation premium (P/L ~8x, P/VP ~2x) não tolera decepções — qualquer deterioração é punida",
                    "Competição crescente de BTG no wealth management e de fintechs no varejo digital",
                    "Regulação bancária pode aumentar requisitos de capital, pressionando distribuição de dividendos",
                    "Expansão na América Latina (Chile, Argentina, Colômbia) adiciona risco cambial e político",
                ],
                "barreira": (
                    "A combinação de marca, rede de distribuição, base de dados de clientes e capital regulatório "
                    "cria uma barreira de entrada que nenhuma fintech conseguiu transpor em décadas. "
                    "Nubank chegou a 100 milhões de clientes — mas em rentabilidade por cliente ainda está longe do Itaú."
                ),
            },
            "BBAS3": {
                "nome": "Banco do Brasil",
                "fundacao": "1808 (fundado por Dom João VI)",
                "sede": "Brasília, DF",
                "tagline": "O banco do agro e do funcionalismo. Líder incontestável no crédito rural, mas pagando o preço de uma carteira concentrada.",
                "modelo": (
                    "O BB tem três pilares que nenhum banco privado consegue replicar: o crédito rural (53% do crédito "
                    "agro brasileiro passa pelo BB, com funding subsidiado via FCO e PRONAF), o funcionalismo público "
                    "(processa metade das folhas do setor público federal e estadual — base de consignado captiva), e o "
                    "Tesouro Nacional (agente financeiro do governo federal). Fora isso, é um banco universal com "
                    "seguros (BB Seguridade, controlada listada separadamente) e gestão de ativos. O problema de 2025-2026 "
                    "é exatamente essa concentração: o agro sofreu com El Niño, preços baixos de grãos e endividamento "
                    "acumulado. A inadimplência rural saltou de 1% para 6%, o lucro caiu 54% no 1T26 e o ROE colapsou "
                    "para 7,3%. A BB Seguridade, contudo, continua entregando — o banco dentro do banco que o mercado "
                    "frequentemente esquece."
                ),
                "receita": [
                    ("Margem financeira (NII)", "~45%", "crédito rural + consignado + corporate"),
                    ("BB Seguridade (resultado de equivalência patrimonial)", "~20%", "seguros, previdência e capitalização"),
                    ("Receitas de serviços e tarifas", "~20%", "folha de pagamento, asset management, tarifas"),
                    ("Tesouraria e mercado", "~15%", "títulos públicos e operações com o governo"),
                ],
                "vantagens": [
                    "Monopólio prático no crédito agro — nenhum banco privado tem a rede, o funding subsidiado e a expertise",
                    "Folha do setor público: base captiva de consignado com inadimplência próxima de zero",
                    "BB Seguridade: motor de resultado capital-light e recorrente dentro do conglomerado",
                    "Valuation de desconto (P/L ~4x, P/VP ~0,6x) embute a percepção de risco estatal",
                    "Gestão de ativos: 24,9% de market share — o maior gestor de recursos do Brasil",
                ],
                "riscos": [
                    "Interferência política: governo pode forçar crédito subsidiado, reduzir spread e comprometer rentabilidade",
                    "Concentração no agro: ciclos negativos (clima, preço de commodities) impactam desproporcionalmente",
                    "Inadimplência rural 2025-2026: ainda longe do pico — pode demorar 2-3 anos para normalizar",
                    "Menor eficiência operacional que bancos privados — custo de servir é mais alto",
                ],
                "barreira": (
                    "O acesso ao funding subsidiado (FCO, PRONAF, recursos do Tesouro) é uma barreira que nenhum banco "
                    "privado pode replicar. Quem financia agricultura a taxa de 7-8% a.a. quando o custo de mercado é 14%+ "
                    "está usando um subsídio que só o banco estatal acessa. Isso cria uma vantagem competitiva no agro "
                    "que é, literalmente, impossível de replicar sem ser banco público."
                ),
            },
            "BBDC3": {
                "nome": "Bradesco",
                "fundacao": "1943",
                "sede": "Osasco, SP",
                "tagline": "O gigante em reestruturação. Construído no interior do Brasil, foi o maior banco privado por décadas — agora recupera a rentabilidade.",
                "modelo": (
                    "O Bradesco é o único entre os grandes privados que foi construído de dentro para fora do Brasil — "
                    "nasceu em Marília (SP) e cresceu pelo interior antes de chegar às capitais. Essa origem explica "
                    "sua exposição à massa e às PMEs do interior, que são mais vulneráveis a ciclos de juros altos. "
                    "Em 2022-2024, o banco pagou o preço: inadimplência subindo, provisões estourando, ROE colapsando "
                    "para abaixo do custo de capital. A reestruturação de Marcelo Noronha (CEO desde 2023) levou o banco "
                    "a ser mais seletivo no crédito, a fechar agências, digitalizar e focar em alta renda e crédito "
                    "com garantia. O resultado começou a aparecer em 2025: lucro crescendo, ROE recuperando, ação "
                    "subindo 60% no ano. Em 2026, a tese é de quanto esse ROE ainda pode subir — e se chegará ao "
                    "nível de Itaú, ou ficará estacionado nos 15-17%."
                ),
                "receita": [
                    ("Margem financeira (NII)", "~50%", "spread de crédito PF + PME + corporativo"),
                    ("Seguros (Bradesco Seguros)", "~20%", "vida, saúde, automóvel — joint venture com Munich Re"),
                    ("Receitas de serviços e tarifas", "~18%", "cartão, previdência, corretagem"),
                    ("Outros", "~12%", "mercado de capitais, câmbio, gestão de ativos"),
                ],
                "vantagens": [
                    "Bradesco Seguros: uma das maiores seguradoras do Brasil — negócio capital-light com margens altas",
                    "Rede capilar no interior: presença onde grandes bancos e fintechs chegam com mais dificuldade",
                    "Reestruturação em curso: se o ROE normalizar para 18-20%, o valuation atual (P/L ~6x) está barato",
                    "Cielo integrada: adquirência + produtos bancários criam potencial de cross-sell",
                ],
                "riscos": [
                    "Execução: a reestruturação pode demorar mais ou entregar menos que o prometido",
                    "Concorrência de fintechs no varejo massificado — o segmento que o Bradesco depende mais",
                    "Exposição residual à massa de baixa renda, mais sensível a inadimplência em juro alto",
                    "Valuation não é mais óbvio — após alta de 60% em 2025, o desconto já fechou parcialmente",
                ],
                "barreira": (
                    "A rede de distribuição no interior do Brasil é o ativo mais difícil de replicar. "
                    "Cidades de 30.000 habitantes onde o Bradesco é o único banco presente — e onde "
                    "a fintech não chega sem agência ou correspondente. Mais a Bradesco Seguros, que tem "
                    "escala e relacionamento de décadas com corretores."
                ),
            },
            "BPAC11": {
                "nome": "BTG Pactual",
                "fundacao": "1983",
                "sede": "São Paulo, SP",
                "tagline": "O maior banco de investimento da América Latina. Não é um banco de varejo — é uma máquina de alocar capital.",
                "modelo": (
                    "O BTG é estruturalmente diferente dos outros: não tem agência, não quer o cliente de massa, "
                    "não cresce emprestando para pessoa física no cartão. Ele ganha dinheiro sendo o intermediário "
                    "entre quem tem capital (grandes fortunas, fundos) e quem precisa de capital (grandes empresas, governos). "
                    "A receita tem seis pilares: corporate lending (crédito para grandes empresas, ~R$2,3 bi/tri), "
                    "sales & trading (mesa proprietária e corretagem institucional), investment banking (IPOs, M&As, emissões), "
                    "asset management (R$2,5 tri sob gestão/administração), wealth management (R$1,28 tri — clientes private) "
                    "e consumer finance (Banco PAN + Too Seguros, consignado privado). "
                    "No 1T26 entregou lucro de R$4,8 bi (+42% a/a) e ROAE de 26,6%. "
                    "O modelo de partnership (sócios compram ações — alinhamento total) é um diferencial cultural único."
                ),
                "receita": [
                    ("Corporate Lending", "~23%", "crédito corporativo de alta qualidade — crescimento de 22% a/a"),
                    ("Wealth Management", "~15%", "R$ 1,28 tri sob gestão — crescimento recorde"),
                    ("Sales & Trading", "~19%", "mesa proprietária + corretagem institucional — volátil"),
                    ("Asset Management", "~12%", "R$ 2,5 tri total — taxas de gestão e performance"),
                    ("Consumer Finance & Banking", "~11%", "Banco PAN + Too Seguros — consignado privado"),
                    ("Investment Banking", "~10%", "IPOs, M&As, emissões de dívida — cíclico"),
                    ("Outros (juros e outros)", "~10%", ""),
                ],
                "vantagens": [
                    "Modelo de partnership: sócios são donos — incentivos alinhados, execução consistente há 40 anos",
                    "Wealth Management: R$1,28 tri em assets com crescimento de 44,6% a/a — receita recorrente e crescente",
                    "Corporate Lending: inadimplência próxima de zero em crédito para grandes empresas com garantias robustas",
                    "Marca BTG no mercado de capitais: quando uma empresa quer captar R$1 bi+, o BTG está na lista curta",
                    "Único entre os grandes a ter ROE acima de 26% de forma sustentada",
                ],
                "riscos": [
                    "Valuation elevado (P/VP ~9x) não tolera desaceleração — crescimento tem que ser entregue",
                    "Investment banking é cíclico — em mercados fechados (sem IPOs, sem M&A), essa linha murcha",
                    "Dividend yield baixo (~2%) — não é banco de renda; é banco de crescimento e reinvestimento",
                    "Risco-chave concentrado em poucos sócios-chave — risco de sucessão no longo prazo",
                ],
                "barreira": (
                    "A marca e o relacionamento de décadas com os grandes CEOs e CFOs do Brasil. "
                    "Não é possível construir isso da noite para o dia. Quando a Vale vai emitir uma debênture "
                    "ou o governo quer estruturar um projeto de infraestrutura, o BTG está na mesa. "
                    "Isso vem de 40 anos de execução impecável e de uma cultura de partnership que "
                    "atrai os melhores profissionais do mercado financeiro."
                ),
            },
            "SANB3": {
                "nome": "Santander Brasil",
                "fundacao": "1982 (chegou ao Brasil)",
                "sede": "São Paulo, SP",
                "tagline": "O único banco internacional com escala no Brasil. Terceiro maior privado, mas ainda procurando o modelo certo para o mercado local.",
                "modelo": (
                    "O Santander é um banco universal (PF + PME + atacado), mas com uma particularidade: "
                    "é subsidiária de um grupo global espanhol. Isso tem vantagens (acesso a tecnologia, "
                    "melhores práticas globais, plataforma de câmbio internacional) e desvantagens "
                    "(decisões estratégicas feitas em Madri podem não se adaptar à realidade brasileira, "
                    "e parte do lucro 'vaza' para a matriz). Historicamente, o Santander teve dificuldade "
                    "de encontrar seu nicho no Brasil: não tem o foco em alta renda do Itaú, não tem o "
                    "agro do BB, não tem o interior do Bradesco, não tem o atacado do BTG. "
                    "Em 2026, está buscando diferenciação em crédito imobiliário, alta renda e PME. "
                    "O ROE ainda é o mais baixo entre os grandes privados — o mercado cobra prova."
                ),
                "receita": [
                    ("Margem financeira (NII)", "~52%", "crédito PF + PME + corporate"),
                    ("Receitas de serviços e tarifas", "~22%", "cartão, seguros, corretagem"),
                    ("Seguros e previdência", "~12%", ""),
                    ("Mercado de capitais e câmbio", "~14%", ""),
                ],
                "vantagens": [
                    "Plataforma global: câmbio, trade finance e operações internacionais para clientes com negócios no exterior",
                    "Acesso à tecnologia e melhores práticas do grupo global — Openbank (banco digital do grupo) chegando ao Brasil",
                    "Valuation descontado em relação aos pares: se o ROE normalizar, há upside relevante",
                    "Histórico consistente de pagamento de JCP — yield atrativo dado o valuation baixo",
                ],
                "riscos": [
                    "ROE estruturalmente mais baixo que os pares privados — sem nicho definido que justifique prêmio",
                    "Decisões estratégicas dependem da matriz espanhola — nem sempre otimizadas para o Brasil",
                    "Exposição a PME e varejo de menor renda em ciclo de juro alto e inadimplência elevada",
                    "Competição intensa: Itaú na alta renda, BTG no atacado, Nubank/Inter no varejo digital",
                ],
                "barreira": (
                    "A plataforma global é a barreira real. Para uma empresa brasileira que exporta, "
                    "importa ou tem sócios internacionais, ter um banco com presença em 10 países na mesa "
                    "é conveniente. Mas no varejo PF doméstico, essa vantagem não aparece — o que explica "
                    "o ROE mais baixo: a barreira não se traduz em rentabilidade no negócio principal."
                ),
            },
            "ABCB4": {
                "nome": "ABC Brasil",
                "fundacao": "1989",
                "sede": "São Paulo, SP",
                "tagline": "O banco que nunca atendeu pessoa física. 100% atacado, 100% foco em empresa — e a menor inadimplência do setor.",
                "modelo": (
                    "O ABC Brasil é o mais puro exemplo de especialização no setor bancário brasileiro. "
                    "Não tem agência para pessoa física. Não tem conta corrente de varejo. Não tem cartão de crédito PF. "
                    "Atende exclusivamente médias e grandes empresas (segmento middle market, corporate e large corporate) "
                    "com crédito, trade finance (financiamento ao comércio exterior), câmbio, derivativos, "
                    "banco de investimento e seguros corporativos. "
                    "Controlado pelo Arab Banking Corporation (banco árabe do Barein), tem acesso facilitado "
                    "a funding internacional e a uma rede de relacionamentos no Oriente Médio que "
                    "nenhum banco brasileiro replica. "
                    "A inadimplência histórica abaixo de 1% é o resultado de 35 anos atendendo quem "
                    "tem balanço para mostrar — empresas com faturamento mínimo de R$30 mi anuais."
                ),
                "receita": [
                    ("Margem com clientes (crédito corporativo)", "~55%", "spread sobre carteira de R$32+ bi"),
                    ("Margem com mercado e tesouraria", "~20%", "PL remunerado ao CDI + operações de mercado"),
                    ("Receitas de serviços", "~15%", "banco de investimento, tarifas, câmbio"),
                    ("Seguros e outros", "~10%", ""),
                ],
                "vantagens": [
                    "Inadimplência histórica < 1% — resultado de 35 anos emprestando apenas para empresas com balanço",
                    "Sem exposição ao varejo PF: não sofre com inadimplência de cartão, crédito pessoal ou PME de baixa renda",
                    "Funding internacional (via Arab Banking Corp) com custo menor que captação doméstica — vantagem de spread",
                    "Modelo de negócio simples, previsível e escalável — sem a complexidade operacional de um banco universal",
                    "Alta correlação de receitas com o CDI: PL remunerado a CDI + margem com clientes = proteção natural em juro alto",
                ],
                "riscos": [
                    "Concentração: poucas carteiras grandes — uma inadimplência relevante pontual impacta mais que num banco pulverizado",
                    "Crescimento limitado: não tem varejo para escalar rapidamente — cresce no ritmo das empresas que serve",
                    "Controlador estrangeiro: decisões podem ser influenciadas por dinâmicas do Arab Banking Corporation",
                    "Exposição ao ciclo corporativo: recessão severa aumenta inadimplência mesmo no atacado",
                ],
                "barreira": (
                    "35 anos de relacionamento com o middle e large corporate brasileiro. "
                    "Empresa de faturamento R$300 mi não troca de banco por conveniência — "
                    "o relacionamento, o limite de crédito aprovado e as operações estruturadas em curso "
                    "criam um lock-in real. Mais o funding árabe, que nenhum banco brasileiro vai replicar."
                ),
            },
            "BRSR6": {
                "nome": "Banrisul",
                "fundacao": "1928",
                "sede": "Porto Alegre, RS",
                "tagline": "O banco do Rio Grande do Sul. Seu destino é o destino do RS — e do contrato com o governo estadual.",
                "modelo": (
                    "O Banrisul é um banco estatal regional — o que significa que seu modelo de negócio "
                    "é fundamentalmente diferente de todos os outros nesta lista. "
                    "Ele existe porque o governo do RS quer um banco público estadual. "
                    "O coração do negócio é a folha de pagamento dos servidores públicos gaúchos: "
                    "294 mil servidores ativos, inativos e pensionistas cujo salário passa pelo Banrisul, "
                    "gerando uma base captiva de consignado, conta corrente e produtos financeiros. "
                    "Em julho de 2026, renovou esse contrato por R$1,26 bi — pago à vista, reconhecido como "
                    "intangível e amortizado ao longo de 5 anos. O custo dobrou em relação à renovação "
                    "anterior (que era de 10 anos). Fora a folha, atende PMEs gaúchas e o varejo do RS. "
                    "Toda a sua força e seu risco estão concentrados em um único estado."
                ),
                "receita": [
                    ("Crédito consignado público (servidores RS)", "~40%", "base captiva da folha estadual"),
                    ("Varejo PF e PME gaúcha", "~35%", "clientes pessoas físicas e pequenas empresas do RS"),
                    ("Receitas de serviços", "~15%", "tarifas, previdência, seguros"),
                    ("Tesouraria", "~10%", "títulos públicos e operações de mercado"),
                ],
                "vantagens": [
                    "Base captiva de consignado público — 294 mil servidores estaduais com desconto em folha",
                    "Valuation muito barato (P/VP ~0,5x, P/L ~3x) — desconta o risco político e o ROE baixo",
                    "Dividend yield alto (~9-11%) — governo precisa do dividendo do banco para compor receitas estaduais",
                    "Presença capilar no interior do RS onde os grandes bancos privados não chegam",
                ],
                "riscos": [
                    "100% concentrado no RS — enchentes, seca, recessão regional batem direto no resultado",
                    "Dependência do contrato de folha: renovado a custo crescente (dobrou por ano de contrato na última renovação)",
                    "ROE cronicamente baixo (~7-9%) — estruturalmente abaixo do custo de capital",
                    "Risco político: troca de governo estadual pode mudar a relação ou condições do contrato",
                    "Qualidade de crédito pressionada em PF e PME, com inadimplência subindo em 2026",
                ],
                "barreira": (
                    "O contrato com o governo do RS é a barreira — e também o risco. "
                    "Nenhum banco privado vai entrar no estado para fazer o que o Banrisul faz "
                    "sem o benefício do funding barato do servidor e a capilaridade de 500+ agências no interior. "
                    "Mas essa barreira tem preço: R$1,26 bi a cada 5 anos só para manter o que já tem."
                ),
            },
            "BMGB4": {
                "nome": "Banco BMG",
                "fundacao": "1930 (família Pentagna Guimarães)",
                "sede": "Belo Horizonte, MG",
                "tagline": "O especialista em consignado INSS. Enquanto outros bancões atendem todo mundo, o BMG só atende aposentado — e isso é sua maior força.",
                "modelo": (
                    "O BMG é o banco mais nichado desta lista: 88% da carteira de crédito é formada "
                    "por aposentados e pensionistas do INSS. "
                    "O produto central é o empréstimo consignado, onde as parcelas são descontadas "
                    "diretamente do benefício do INSS — a inadimplência é estruturalmente baixa porque "
                    "o pagador não é a pessoa, é o governo federal. "
                    "A distribuição é feita por correspondentes bancários (terceiros que originam o crédito), "
                    "lojas próprias 'help! Loja de Crédito' (na cor laranja, reconhecível pelo público), "
                    "e canais digitais. "
                    "O desafio é que o governo regula a taxa máxima (hoje 1,85%/mês para o empréstimo e "
                    "2,46%/mês para o cartão). Quando a Selic sobe, o custo de captação sobe, "
                    "mas o teto de taxa não — o spread comprime. "
                    "Em 2025-2026, a CPI do INSS investigando fraudes no consignado criou obrigação de "
                    "biometria facial para cada contratação — adiciona fricção e pode frear a originação."
                ),
                "receita": [
                    ("Empréstimo consignado INSS", "~55%", "produto principal — taxa máxima 1,85%/mês"),
                    ("Cartão consignado INSS", "~25%", "desconto direto no benefício — taxa máxima 2,46%/mês"),
                    ("Consignado privado (CLT)", "~10%", "iniciado em 2025 — menor escala, maior risco"),
                    ("Seguros e outros produtos", "~10%", "Bmg Seguradora — vida, acidentes pessoais"),
                ],
                "vantagens": [
                    "Inadimplência estruturalmente baixa: parcelas descontadas direto do INSS — o devedor não pode deixar de pagar",
                    "Base de aposentados é demograficamente crescente — 35 milhões de beneficiários do INSS e crescendo",
                    "Reconhecimento de marca no público INSS: a cor laranja é sinônimo de consignado no interior do Brasil",
                    "Correspondentes bancários capilarizados onde bancos tradicionais não chegam",
                ],
                "riscos": [
                    "Teto regulatório de taxa: Selic sobe, mas o banco não consegue repassar — spread comprime estruturalmente",
                    "CPI do INSS e fraudes no consignado: biometria obrigatória adiciona fricção e pode reduzir origação",
                    "Concentração extrema em um segmento: qualquer mudança regulatória no consignado INSS impacta 88% da carteira",
                    "ROE limitado pelo teto de taxa: difícil escalar margem acima de 12-14% com spread comprimido",
                    "Consignado privado (CLT) em expansão — risco maior que o INSS, e o banco ainda está aprendendo o segmento",
                ],
                "barreira": (
                    "O reconhecimento de marca no público INSS e a rede de correspondentes são difíceis de replicar. "
                    "O aposentado do interior que reconhece a loja laranja e confia no 'consignado BMG' "
                    "não troca facilmente de banco. Além disso, os correspondentes que originam crédito "
                    "têm relacionamentos de anos com o BMG — e comissões que constroem lealdade. "
                    "A barreira não é tecnológica; é de relacionamento e presença física em regiões remotas."
                ),
            },
        },
    },
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


