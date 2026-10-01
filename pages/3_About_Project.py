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


st.set_page_config(page_title="About Project", page_icon="📘", layout="wide")

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
        key="theme_switch_about",
    )
    st.session_state.theme = "light" if theme_choice == "☀️ Light" else "dark"

load_css(st.session_state.theme)

st.title("About the Project")
st.caption("Insurance Claim Risk & Premium Predictor")

st.markdown(
    """
    <div class="section-card">
        <h3>Project Overview</h3>
        <p>This project uses machine learning to predict:</p>
        <ol>
            <li>Insurance premium amount</li>
            <li>Insurance claim risk</li>
        </ol>
        <p>The dataset is synthetic and contains customer, policy and financial information.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">Machine Learning Workflow</div>', unsafe_allow_html=True)
workflow = ["Data Generation", "EDA", "Preprocessing", "Model Training", "Evaluation", "Prediction"]
workflow_html = "".join(f"<span class='workflow-step'>{step}</span>" for step in workflow)
workflow_html = workflow_html.replace("</span>", "</span> <span class='workflow-arrow'>→</span> ")
st.markdown(f"<div class='workflow-flow'>{workflow_html}</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="info-card">
        <h3>Models</h3>
        <p><strong>Premium Prediction:</strong> Gradient Boosting Regressor</p>
        <p><strong>Classification:</strong> Logistic Regression</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="info-card">
        <h3>Input Features</h3>
        <ul>
            <li>Age</li>
            <li>BMI</li>
            <li>Dependents</li>
            <li>Smoker</li>
            <li>Policy Type</li>
            <li>Claim History</li>
            <li>Annual Income</li>
            <li>Coverage Amount</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="info-card">
        <h3>Technologies</h3>
        <ul>
            <li>Python</li>
            <li>Pandas</li>
            <li>NumPy</li>
            <li>Scikit-learn</li>
            <li>Matplotlib / Seaborn</li>
            <li>Streamlit</li>
            <li>Joblib</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-card">
        <h3>View the Source Code</h3>
        <p>Explore the complete machine learning project and implementation on GitHub.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.link_button("View GitHub Repository →", "https://github.com/Sumaira-K/Insurance-Claim-Project")

st.markdown(
    """
    <div class="disclaimer">
        This prediction is generated using a machine learning model trained on synthetic insurance data and is intended for demonstration and educational purposes only. It should not be used as a real insurance underwriting decision.
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
