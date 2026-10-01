from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT_DIR / "style.css"

FEATURE_COLUMNS = [
    "age",
    "bmi",
    "dependents",
    "smoker",
    "policy_type",
    "claim_history",
    "annual_income",
    "coverage_amount",
]


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


@st.cache_resource
def load_models():
    try:
        preprocessor = joblib.load(ROOT_DIR / "preprocessor.pkl")
        premium_model = joblib.load(ROOT_DIR / "premium_prediction_model.pkl")
        claim_risk_model = joblib.load(ROOT_DIR / "claim_risk_model.pkl")
        return preprocessor, premium_model, claim_risk_model
    except Exception:
        st.error("The trained model files could not be loaded. Please confirm the project files are present.")
        return None, None, None


st.set_page_config(page_title="Insurance Prediction", page_icon="🧮", layout="wide")

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
        key="theme_switch_predict",
    )
    st.session_state.theme = "light" if theme_choice == "☀️ Light" else "dark"

load_css(st.session_state.theme)

st.title("Insurance Prediction")
st.caption("Enter the customer's information to generate an estimated premium and claim-risk assessment.")

st.markdown('<div class="section-title">Personal Details</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=35, step=1, key="age")
with col2:
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=27.5, step=0.1, key="bmi")

col3, col4 = st.columns(2)
with col3:
    dependents = st.number_input("Dependents", min_value=0, max_value=10, value=2, step=1, key="dependents")
with col4:
    smoker = st.selectbox("Smoker", ["Yes", "No"], index=1, key="smoker")

st.markdown('<div class="section-title">Policy Details</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    policy_type = st.selectbox("Policy Type", ["Basic", "Standard", "Comprehensive"], index=1, key="policy_type")
with col6:
    claim_history = st.selectbox("Claim History", [0, 1, 2, 3, 4], index=1, key="claim_history")

st.markdown('<div class="section-title">Financial Details</div>', unsafe_allow_html=True)
col7, col8 = st.columns(2)
with col7:
    annual_income = st.number_input("Annual Income", min_value=0, value=1500000, step=1000, format="%d", key="annual_income")
with col8:
    coverage_amount = st.number_input("Coverage Amount", min_value=0, value=2500000, step=1000, format="%d", key="coverage_amount")

sample_button = st.button("Load sample profile", use_container_width=True)
if sample_button:
    st.session_state.age = 35
    st.session_state.bmi = 27.5
    st.session_state.dependents = 2
    st.session_state.smoker = "No"
    st.session_state.policy_type = "Standard"
    st.session_state.claim_history = 1
    st.session_state.annual_income = 1500000
    st.session_state.coverage_amount = 2500000

form = st.form("prediction_form")
with form:
    submitted = st.form_submit_button("Calculate Prediction", use_container_width=True)

if submitted:
    input_df = pd.DataFrame(
        [{
            "age": age,
            "bmi": bmi,
            "dependents": dependents,
            "smoker": smoker,
            "policy_type": policy_type,
            "claim_history": claim_history,
            "annual_income": annual_income,
            "coverage_amount": coverage_amount,
        }]
    )

    preprocessor, premium_model, claim_risk_model = load_models()
    if preprocessor is None or premium_model is None or claim_risk_model is None:
        st.stop()

    processed = preprocessor.transform(input_df[FEATURE_COLUMNS])
    premium_value = float(premium_model.predict(processed)[0])
    risk_value = int(claim_risk_model.predict(processed)[0])
    risk_label = "Low Risk" if risk_value == 0 else "High Risk"
    risk_class = "low-risk" if risk_value == 0 else "high-risk"

    st.session_state.prediction = {
        "premium": premium_value,
        "risk": risk_label,
        "risk_class": risk_class,
        "summary": {
            "Age": age,
            "BMI": bmi,
            "Dependents": dependents,
            "Smoker": smoker,
            "Policy Type": policy_type,
            "Claim History": claim_history,
            "Annual Income": f"₹{annual_income:,.2f}",
            "Coverage Amount": f"₹{coverage_amount:,.2f}",
        },
    }

if "prediction" in st.session_state:
    premium_value = st.session_state.prediction["premium"]
    risk_label = st.session_state.prediction["risk"]
    risk_class = st.session_state.prediction["risk_class"]
    st.markdown(
        """
        <div class="result-card">
            <div class="result-header">
                <h3>Results</h3>
            </div>
            <div class="result-panel">
                <div class="amount-box">
                    <span>Estimated Annual Premium</span>
                    <strong>₹%s</strong>
                </div>
                <div class="risk-box">
                    <span>Claim Risk</span>
                    <div class="risk-badge %s">%s</div>
                </div>
            </div>
        </div>
        """ % (f"{premium_value:,.2f}", risk_class, risk_label),
        unsafe_allow_html=True,
    )

    st.markdown('<div class="summary-card"><h3>Prediction Summary</h3></div>', unsafe_allow_html=True)
    summary_items = st.session_state.prediction["summary"].items()
    summary_html = "".join(
        f"<div class='summary-item'><span>{label}</span><strong>{value}</strong></div>" for label, value in summary_items
    )
    st.markdown(f"<div class='summary-card'><div class='summary-grid'>{summary_html}</div></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-card">
            <h3>About the prediction</h3>
            <p>The application uses two trained machine learning models from the existing project.</p>
            <ul>
                <li><strong>Gradient Boosting Regressor</strong> — Used for premium prediction.</li>
                <li><strong>Logistic Regression</strong> — Used for claim-risk classification.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="empty-state">
            <strong>Your prediction will appear here</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
