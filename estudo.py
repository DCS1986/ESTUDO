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
    background-color: #0D1117;
    color: #E6E1D6;
}
[data-testid="stAppViewContainer"] { background-color: #0D1117; }
[data-testid="stMain"] { background-color: #0D1117; }
.main .block-container { background-color: #0D1117; }

[data-testid="stSidebar"] {
    background: #161B22;
    border-right: 1px solid rgba(255,255,255,0.06);
}
[data-testid="stSidebar"] .stButton > button {
    width: 100%; border: none; text-align: left;
    padding: 10px 14px; border-radius: 8px;
    font-size: 0.84rem; font-weight: 700;
    cursor: pointer; transition: all 0.15s;
    margin: 2px 0;
}
[data-testid="stSidebar"] .stButton > button:hover {
    filter: brightness(1.15);
}
[data-testid="stSidebar"] .stButton > button:focus {
    box-shadow: none !important; outline: none !important;
}

h1 { font-family: 'Playfair Display', serif !important; color: #E6E1D6 !important; }
h2, h3 { font-family: 'Inter', sans-serif !important; font-weight: 700 !important; color: #E6E1D6 !important; }

.dossie-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px; padding: 20px 24px; margin-bottom: 14px;
}
.dossie-card-gold {
    background: rgba(212,175,55,0.05);
    border: 1px solid rgba(212,175,55,0.20);
    border-radius: 12px; padding: 20px 24px; margin-bottom: 14px;
}

.section-label {
    font-size: 0.70rem; font-weight: 700; letter-spacing: 1.2px;
    text-transform: uppercase; color: #D4AF37; margin-bottom: 10px;
}

.battle-header {
    font-size: 0.78rem; font-weight: 800; letter-spacing: 0.5px;
    text-transform: uppercase; padding: 8px 0 6px 0;
    border-bottom: 2px solid; margin-bottom: 14px;
}
.battle-row-label {
    font-size: 0.72rem; font-weight: 600; color: #8A8580;
    text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px;
}
.battle-row-value {
    font-size: 0.92rem; font-weight: 500; color: #E6E1D6;
    line-height: 1.5; margin-bottom: 14px;
}
.badge { display: inline-block; font-size: 0.68rem; font-weight: 700;
    padding: 2px 8px; border-radius: 20px; letter-spacing: 0.5px; text-transform: uppercase; }
.badge-green  { background: rgba(34,197,94,0.15);  color: #22C55E; }
.badge-yellow { background: rgba(212,175,55,0.15); color: #D4AF37; }
.badge-red    { background: rgba(239,68,68,0.15);  color: #EF4444; }
.badge-blue   { background: rgba(99,179,237,0.15); color: #63B3ED; }

.ticker-tag {
    display: inline-block; background: rgba(212,175,55,0.12);
    border: 1px solid rgba(212,175,55,0.30); color: #D4AF37;
    font-size: 0.75rem; font-weight: 700; padding: 3px 10px;
    border-radius: 6px; letter-spacing: 0.5px; margin-right: 6px; margin-bottom: 6px;
}

.thin-divider { border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 20px 0; }

.pill-vantagem {
    background: rgba(34,197,94,0.08); border-left: 3px solid #22C55E;
    border-radius: 0 8px 8px 0; padding: 10px 14px; margin-bottom: 8px;
    font-size: 0.875rem; color: #D1FAE5; line-height: 1.5;
}
.pill-risco {
    background: rgba(239,68,68,0.08); border-left: 3px solid #EF4444;
    border-radius: 0 8px 8px 0; padding: 10px 14px; margin-bottom: 8px;
    font-size: 0.875rem; color: #FEE2E2; line-height: 1.5;
}
.pill-neutro {
    background: rgba(212,175,55,0.08); border-left: 3px solid #D4AF37;
    border-radius: 0 8px 8px 0; padding: 10px 14px; margin-bottom: 8px;
    font-size: 0.875rem; color: #FEF3C7; line-height: 1.5;
}

[data-testid="stTabs"] button { font-size: 0.82rem !important; font-weight: 600 !important; color: #6B7280 !important; }
[data-testid="stTabs"] button[aria-selected="true"] { color: #D4AF37 !important; border-bottom-color: #D4AF37 !important; }
[data-testid="stSelectbox"] { color: #E6E1D6; }
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0D1117; }
::-webkit-scrollbar-thumb { background: #374151; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CONTEÚDO — SETORES E EMPRESAS
# ─────────────────────────────────────────────────────────────────────────────

from setores_data import SETORES  # fonte única — edite em setores_data.py

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 24px 16px 8px 16px;'>
        <div style='font-family: Playfair Display, serif; font-size: 1.3rem; font-weight: 800;
                    color: #E6E1D6; line-height: 1.2; margin-bottom: 4px;'>
            Dossiê de Setores
        </div>
        <div style='font-size: 0.72rem; color: #4B5563; letter-spacing: 0.5px;'>
            Estudo fundamentalista comparado
        </div>
    </div>
    <hr style='border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 12px 0;'>
    <div style='font-size: 0.65rem; font-weight: 700; letter-spacing: 1px;
                text-transform: uppercase; color: #6B7280; padding: 0 16px 8px 16px;'>
        Setores
    </div>
    """, unsafe_allow_html=True)

    if "setor_ativo" not in st.session_state:
        st.session_state.setor_ativo = "📄 Papel & Celulose"

    # CSS: colorir cada botão da sidebar pela sua posição (nth-of-type)
    # Ordem: Papel(1) Bancos(2) Seguradoras(3) Utilities(4) Incorporadoras(5)
    #        Saneamento(6) Mineração(7) Petróleo(8) Agro(9) Autopeças(10) Shoppings(11)
    st.markdown("""<style>
[data-testid="stSidebar"] .stButton:nth-of-type(1) > button
  { background:#1A3320 !important; color:#6EE37A !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(2) > button
  { background:#0F2540 !important; color:#60A5FA !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(3) > button
  { background:#251640 !important; color:#A78BFA !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(4) > button
  { background:#2E2400 !important; color:#FCD34D !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(5) > button
  { background:#2E1010 !important; color:#F87171 !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(6) > button
  { background:#0A2535 !important; color:#38BDF8 !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(7) > button
  { background:#251C08 !important; color:#FBBF24 !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(8) > button
  { background:#1A1208 !important; color:#FB923C !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(9) > button
  { background:#122510 !important; color:#86EFAC !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(10) > button
  { background:#1A1A1A !important; color:#D1D5DB !important; }
[data-testid="stSidebar"] .stButton:nth-of-type(11) > button
  { background:#251025 !important; color:#E879F9 !important; }
[data-testid="stSidebar"] .stButton > button:hover
  { filter: brightness(1.2) !important; }
[data-testid="stSidebar"] .stButton > button:focus
  { box-shadow: none !important; outline: none !important; }
</style>""", unsafe_allow_html=True)

    for nome_setor in SETORES:
        dados = SETORES[nome_setor]
        em_construcao = dados.get("em_construcao", False)
        if em_construcao:
            st.markdown(
                f"<div style='margin:2px 0;padding:10px 14px;border-radius:8px;"
                f"background:#111827;opacity:0.35;font-size:0.82rem;color:#6B7280;'>"
                f"{nome_setor} <span style='font-size:0.65rem;'>· em breve</span></div>",
                unsafe_allow_html=True,
            )
        else:
            if st.button(nome_setor, key=f"btn_{nome_setor}",
                         use_container_width=True):
                st.session_state.setor_ativo = nome_setor
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='padding: 0 16px; font-size: 0.68rem; color: #6B7280; line-height: 1.6;'>
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
_sub_html = ""
if dados_setor.get("tickers_sub"):
    _sub_html = (
        "<br><span style='font-size:0.65rem;color:#6B7280;text-transform:uppercase;"
        "letter-spacing:0.8px;margin-right:6px;'>"
        + dados_setor.get("label_sub", "") + ":</span>"
        + "".join(
            f"<span class='ticker-tag' style='opacity:0.65;'>{t}</span>"
            for t in dados_setor.get("tickers_sub", [])
        )
    )
_tickers_html = "".join(
    f"<span class='ticker-tag'>{t}</span>"
    for t in dados_setor.get("tickers", [])
)
st.markdown(
    f"<div style='padding:32px 0 8px 0;'>"
    f"<span style='font-size:0.70rem;font-weight:700;letter-spacing:1.5px;"
    f"text-transform:uppercase;color:#D4AF37;'>"
    f"Dossiê · {setor}</span></div>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<h1 style='font-size:2.0rem;color:#E6E1D6;margin:0 0 10px 0;line-height:1.2;'>"
    f"{setor}</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p style='font-size:0.95rem;color:#6B7280;max-width:680px;line-height:1.6;"
    f"margin-bottom:14px;'>{dados_setor.get('tagline', '')}</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<div style='margin-bottom:28px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:16px;background:transparent;'>"
    f"{_tickers_html}{_sub_html}</div>",
    unsafe_allow_html=True,
)

# Abas principais
tab1, tab2, tab3 = st.tabs(["🧠  Lógica do Setor", "⚔️  Comparativo", "🔍  Perfil Individual"])


# ─── ABA 1: LÓGICA DO SETOR ───────────────────────────────────────────────
with tab1:
    logica = dados_setor.get("logica", {})

    st.markdown(
        "<div class='section-label'>O que você precisa entender antes de qualquer número</div>"
        f"<div class='dossie-card-gold'><div style='font-size:1.0rem;color:#E6E1D6;line-height:1.7;'>"
        f"{logica.get('texto', '')}</div></div>",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Drivers do setor — o que muda o resultado</div>",
                unsafe_allow_html=True)

    for driver, descricao in logica.get("drivers", []):
        st.markdown(
            f"<div class='dossie-card' style='padding:16px 20px;'>"
            f"<div style='font-size:0.80rem;font-weight:700;color:#D4AF37;"
            f"margin-bottom:6px;text-transform:uppercase;letter-spacing:0.5px;'>{driver}</div>"
            f"<div style='font-size:0.88rem;color:#CFCAC0;line-height:1.6;'>{descricao}</div>"
            f"</div>",
            unsafe_allow_html=True,
        )


# ─── ABA 2: COMPARATIVO (BATTLE CARD) ────────────────────────────────────
with tab2:
    comp = dados_setor.get("comparativo", {})
    empresas = comp.get("empresas", {})
    dimensoes = comp.get("dimensoes", [])
    grupos = comp.get("grupos")   # opcional — se existir, divide em grupos

    def _render_battle_group(tickers_grupo, empresas, dimensoes, label=None):
        """Renderiza um grupo de colunas do battle card."""
        if label:
            st.markdown(
                f"<div style='font-size:0.75rem;font-weight:700;color:#D4AF37;"
                f"text-transform:uppercase;letter-spacing:1px;margin:18px 0 10px 0;'>"
                f"{label}</div>",
                unsafe_allow_html=True,
            )
        col_label, *cols_emp = st.columns([1.1] + [1] * len(tickers_grupo))
        col_label.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        for col, tk in zip(cols_emp, tickers_grupo):
            emp = empresas[tk]
            cor = emp['cor']
            col.markdown(
                f"<div style='font-size:0.78rem;font-weight:800;letter-spacing:0.5px;"
                f"text-transform:uppercase;padding:8px 0 6px 0;"
                f"border-bottom:2px solid {cor};margin-bottom:14px;color:{cor};'>"
                f"{tk}<br>"
                f"<span style='font-size:0.62rem;font-weight:500;color:#6B7280;"
                f"letter-spacing:0;text-transform:none;'>{emp['nome']}</span></div>",
                unsafe_allow_html=True,
            )
        for dim in dimensoes:
            col_label, *cols_emp = st.columns([1.1] + [1] * len(tickers_grupo))
            col_label.markdown(
                f"<div class='battle-row-label' style='padding-top:4px;'>{dim}</div>",
                unsafe_allow_html=True,
            )
            for col, tk in zip(cols_emp, tickers_grupo):
                val = empresas[tk].get(dim, ("—", ""))
                if isinstance(val, tuple) and len(val) == 3:
                    col.markdown(
                        f"<div class='battle-row-value'>"
                        f"<span class='badge {val[2]}'>{val[0]}</span><br>"
                        f"<span style='font-size:0.80rem;color:#CFCAC0;'>{val[1]}</span></div>",
                        unsafe_allow_html=True,
                    )
                elif isinstance(val, tuple) and len(val) == 2:
                    col.markdown(
                        f"<div class='battle-row-value'>"
                        f"<strong style='font-size:0.88rem;'>{val[0]}</strong><br>"
                        f"<span style='font-size:0.80rem;color:#CFCAC0;'>{val[1]}</span></div>",
                        unsafe_allow_html=True,
                    )
                else:
                    col.markdown(
                        f"<div class='battle-row-value'>{val}</div>",
                        unsafe_allow_html=True,
                    )
            st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

    if not empresas:
        st.info("Comparativo ainda não disponível para este setor.")
    elif grupos:
        # Setor com subgrupos (ex.: Bancos grandes vs regionais)
        for g in grupos:
            tks = [tk for tk in g["tickers"] if tk in empresas]
            if tks:
                _render_battle_group(tks, empresas, dimensoes, label=g.get("label"))
    else:
        # Setor sem subgrupos — comportamento original
        _render_battle_group(list(empresas.keys()), empresas, dimensoes)


# ─── ABA 3: PERFIL INDIVIDUAL ─────────────────────────────────────────────
with tab3:
    perfis = dados_setor.get("perfis", {})
    if not perfis:
        st.info("Perfis individuais ainda não disponíveis para este setor.")
    else:
        grupos_perfil = dados_setor.get("comparativo", {}).get("grupos")
        if grupos_perfil:
            # Monta lista ordenada: grandes primeiro, depois subgrupo
            ordem = []
            for g in grupos_perfil:
                ordem += [tk for tk in g["tickers"] if tk in perfis]
            # Qualquer ticker não listado vai no fim
            ordem += [tk for tk in perfis if tk not in ordem]
        else:
            ordem = list(perfis.keys())

        ticker_sel = st.selectbox(
            "Empresa:",
            ordem,
            format_func=lambda t: f"{t} — {perfis[t]['nome']}",
        )
        p = perfis[ticker_sel]

        # Cor da empresa (vem do comparativo se existir)
        _emp_data = dados_setor.get("comparativo", {}).get("empresas", {}).get(ticker_sel, {})
        _cor_empresa = _emp_data.get("cor", "#8B6914")

        # Cabeçalho do perfil
        st.markdown(
            f"<div style='margin:16px 0 24px 0;padding:24px;background:rgba(255,255,255,0.03);"
            f"border:1px solid rgba(255,255,255,0.07);border-radius:12px;border-left:4px solid {_cor_empresa};'>"
            f"<div style='font-size:0.65rem;font-weight:700;color:#6B7280;"
            f"letter-spacing:1px;text-transform:uppercase;margin-bottom:6px;'>"
            f"{ticker_sel} · Fundada em {p.get('fundacao','?')} · {p.get('sede','')}</div>"
            f"<div style='font-size:1.4rem;font-weight:800;color:#E6E1D6;"
            f"margin-bottom:6px;color:#E6E1D6;font-family:Playfair Display,serif;'>{p['nome']}</div>"
            f"<div style='font-size:0.90rem;color:{_cor_empresa};font-style:italic;"
            f"font-weight:700;filter:brightness(0.72);'>{p.get('tagline','')}</div>"
            f"</div>",
            unsafe_allow_html=True,
        )

        # Como funciona o negócio
        st.markdown("<div class='section-label'>Como funciona o negócio</div>",
                    unsafe_allow_html=True)
        st.markdown(
            f"<div class='dossie-card'>"
            f"<div style='font-size:0.90rem;color:#E8E3D9;line-height:1.75;'>"
            f"{p.get('modelo','')}</div></div>",
            unsafe_allow_html=True,
        )

        # De onde vem a receita
        st.markdown("<div class='section-label' style='margin-top:20px;'>De onde vem a receita</div>",
                    unsafe_allow_html=True)
        for segmento, pct, detalhe in p.get("receita", []):
            st.markdown(
                f"<div style='display:flex;align-items:flex-start;gap:16px;"
                f"padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.06);'>"
                f"<div style='min-width:52px;text-align:right;font-size:1.1rem;"
                f"font-weight:800;color:#D4AF37;padding-top:1px;'>{pct}</div>"
                f"<div><div style='font-size:0.88rem;font-weight:600;color:#E6E1D6;"
                f"margin-bottom:2px;'>{segmento}</div>"
                f"<div style='font-size:0.80rem;color:#CFCAC0;'>{detalhe}</div></div></div>",
                unsafe_allow_html=True,
            )

        # Composição por segmento (aparece só quando o dado existe)
        if p.get("composicao"):
            st.markdown(
                "<div class='section-label' style='margin-top:20px;'>Composição por segmento</div>",
                unsafe_allow_html=True,
            )
            for _seg, _num, _obs in p["composicao"]:
                st.markdown(
                    f"<div style='display:flex;align-items:flex-start;gap:14px;"
                    f"padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.06);'>"
                    f"<div style='min-width:160px;text-align:right;font-size:0.78rem;"
                    f"font-weight:700;color:#D4AF37;padding-top:2px;'>{_num}</div>"
                    f"<div><div style='font-size:0.85rem;font-weight:600;color:#E6E1D6;"
                    f"margin-bottom:1px;'>{_seg}</div>"
                    f"<div style='font-size:0.78rem;color:#6B7280;'>{_obs}</div></div></div>",
                    unsafe_allow_html=True,
                )

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
        st.markdown(
            f"<div class='pill-neutro'>🔒 {p.get('barreira','')}</div>",
            unsafe_allow_html=True,
        )


