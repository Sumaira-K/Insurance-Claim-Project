from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT_DIR / "style.css"


def load_css(theme: str):
    css = CSS_PATH.read_text(encoding="utf-8")
    if theme == "dark":
        css += """
        .stApp { background: #0b1220; color: #f8fafc; }
        [data-testid="stSidebar"] { background: rgba(15, 23, 42, 0.96); border-right: 1px solid rgba(251, 146, 60, 0.2); }
        div[data-testid="stSidebarNav"] a { color: #e5e7eb !important; }
        .hero-panel, .feature-card, .section-card, .result-card, .summary-card, .info-card, .footer-card {
            background: #111827;
            border-color: rgba(251, 146, 60, 0.18);
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.24);
        }
        .hero-visual { background: linear-gradient(135deg, rgba(251, 146, 60, 0.10), rgba(17, 24, 39, 0.72)); }
        .hero-stat, .amount-box, .risk-box, .summary-item, .workflow-step { background: rgba(17, 24, 39, 0.9); }
        .stTextInput > div > div > input, .stNumberInput > div > div > input, .stSelectbox > div > div > select, [data-baseweb="select"] {
            background: #111827 !important; color: #f8fafc !important; border-color: rgba(251, 146, 60, 0.2) !important;
        }
        .stButton > button, .stDownloadButton > button, .stLinkButton > button {
            box-shadow: 0 10px 18px rgba(251, 146, 60, 0.18);
        }
        .empty-state { background: rgba(17, 24, 39, 0.8); border-color: rgba(251, 146, 60, 0.18); }
        p, li, h1, h2, h3, h4, span, strong { color: #f8fafc; }
        .hero-stat span, .summary-item span, .empty-state, .stAlert, .stCaption, .stMarkdown p { color: #d1d5db !important; }
        """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="Insurance Claim Risk & Premium Predictor", page_icon="🛡️", layout="wide")

if "theme" not in st.session_state:
    st.session_state.theme = "light"

with st.sidebar:
    st.markdown('<div class="sidebar-brand">Insurance Risk</div>', unsafe_allow_html=True)
    theme_choice = st.radio(
        "Theme",
        ["☀️ Light", "🌙 Dark"],
        index=0 if st.session_state.theme == "light" else 1,
        horizontal=True,
        label_visibility="collapsed",
        key="theme_switch_home",
    )
    st.session_state.theme = "light" if theme_choice == "☀️ Light" else "dark"

load_css(st.session_state.theme)

hero_left, hero_right = st.columns([1.2, 0.8])
with hero_left:
    st.markdown('<h1>Insurance, made predictable.</h1>', unsafe_allow_html=True)
    st.write("Estimate your annual premium and understand your claim risk using customer and policy information.")
    if st.button("Start Prediction", use_container_width=True):
        st.switch_page("pages/2_Predict.py")

with hero_right:
    st.markdown(
        """
        <div class="hero-visual">
            <div class="hero-badge">Risk Profile</div>
            <div class="hero-stat">
                <strong>₹43,402</strong>
                <span>Estimated annual premium</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-title">Why it matters</div>', unsafe_allow_html=True)
feature_cols = st.columns(3)
features = [
    ("💰", "Premium Estimation", "Estimate the customer's annual insurance premium."),
    ("🛡️", "Claim Risk", "Predict whether the customer falls into a higher or lower claim-risk category."),
    ("⚙️", "Machine Learning", "Predictions are generated using trained machine learning models."),
]
for col, (icon, title, body) in zip(feature_cols, features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{body}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer-card">
        <strong>Insurance Claim Risk & Premium Predictor</strong>
        <span>Machine Learning Project</span><br>
        <a href="https://github.com/Sumaira-K/Insurance-Claim-Project" target="_blank">GitHub Repository →</a>
    </div>
    """,
    unsafe_allow_html=True,
)
