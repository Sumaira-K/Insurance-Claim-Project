import joblib
import pandas as pd
import streamlit as st

from theme import ROOT_DIR, format_inr, render_header

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


@st.cache_resource(show_spinner="Loading saved prediction models...")
def load_models():
    try:
        preprocessor = joblib.load(ROOT_DIR / "preprocessor.pkl")
        premium_model = joblib.load(ROOT_DIR / "premium_prediction_model.pkl")
        claim_risk_model = joblib.load(ROOT_DIR / "claim_risk_model.pkl")
        return preprocessor, premium_model, claim_risk_model
    except Exception:
        st.error("The trained model files could not be loaded. Please confirm the project files are present.")
        return None, None, None


st.set_page_config(
    page_title="Insurance Claim Risk & Premium Predictor",
    page_icon="🛡️",
    layout="wide",
)

render_header()

form_column, results_column = st.columns([1, 1], gap="large")

with form_column:
    with st.container(border=True):
        st.markdown('<div class="section-heading">Customer Information</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-subtitle">Enter the customer’s details to generate predictions.</div>',
            unsafe_allow_html=True,
        )

        with st.form("prediction_form"):
            age_col, bmi_col = st.columns(2, gap="small")
            with age_col:
                age = st.number_input("Age", min_value=18, max_value=100, value=35, step=1, key="age")
            with bmi_col:
                bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=27.5, step=0.1, key="bmi")

            dependents_col, smoker_col = st.columns(2, gap="small")
            with dependents_col:
                dependents = st.number_input(
                    "Dependents", min_value=0, max_value=10, value=2, step=1, key="dependents"
                )
            with smoker_col:
                smoker = st.selectbox("Smoker", ["Yes", "No"], index=1, key="smoker")

            policy_col, history_col = st.columns(2, gap="small")
            with policy_col:
                policy_type = st.selectbox(
                    "Policy Type", ["Basic", "Standard", "Comprehensive"], index=1, key="policy_type"
                )
            with history_col:
                claim_history = st.selectbox("Claim History", [0, 1, 2, 3, 4], index=1, key="claim_history")

            income_col, coverage_col = st.columns(2, gap="small")
            with income_col:
                annual_income = st.number_input(
                    "Annual Income",
                    min_value=0,
                    value=1500000,
                    step=1000,
                    format="%d",
                    key="annual_income",
                )
                st.markdown(
                    f'<span class="field-caption">{format_inr(annual_income)}</span>',
                    unsafe_allow_html=True,
                )
            with coverage_col:
                coverage_amount = st.number_input(
                    "Coverage Amount",
                    min_value=0,
                    value=2500000,
                    step=1000,
                    format="%d",
                    key="coverage_amount",
                )
                st.markdown(
                    f'<span class="field-caption">{format_inr(coverage_amount)}</span>',
                    unsafe_allow_html=True,
                )

            st.markdown('<div class="primary-action"></div>', unsafe_allow_html=True)
            submitted = st.form_submit_button("✧  Predict Insurance Risk", use_container_width=True)

if submitted:
    input_df = pd.DataFrame(
        [
            {
                "age": age,
                "bmi": bmi,
                "dependents": dependents,
                "smoker": smoker,
                "policy_type": policy_type,
                "claim_history": claim_history,
                "annual_income": annual_income,
                "coverage_amount": coverage_amount,
            }
        ]
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
            "Annual Income": format_inr(annual_income),
            "Coverage Amount": format_inr(coverage_amount),
        },
    }

with results_column:
    if "prediction" not in st.session_state:
        st.markdown(
            """
            <div class="empty-state">
                <div class="empty-state-icon" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                         stroke-linecap="round" stroke-linejoin="round">
                        <rect x="6" y="4" width="12" height="17" rx="2"/>
                        <path d="M9 4.5h6M9 9h6M9 13h6M9 17h3"/>
                    </svg>
                </div>
                <strong>Ready to Predict</strong>
                <p>Enter customer information and click <strong>Predict Insurance Risk</strong>.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        prediction = st.session_state.prediction
        risk_class = prediction["risk_class"]
        risk_width = "27%" if risk_class == "low-risk" else "76%"
        risk_color = "var(--success)" if risk_class == "low-risk" else "var(--error)"
        premium_display = format_inr(prediction["premium"], decimals=2)
        summary_html = "".join(
            f"<div class='summary-item'><span>{label}</span><strong>{value}</strong></div>"
            for label, value in prediction["summary"].items()
        )

        st.markdown(
            f"""
            <div class="results-heading">Prediction Results</div>
            <div class="results-subtitle">Model-generated estimates for this customer.</div>
            <div class="result-metrics">
                <div class="result-metric">
                    <div class="result-metric-header">
                        <span>Predicted Premium</span>
                        <span class="result-icon" aria-hidden="true">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                 stroke-linecap="round" stroke-linejoin="round">
                                <rect x="4" y="6" width="16" height="14" rx="2"/>
                                <path d="M4 9h16M16 14h.01M7 6V4h10v2"/>
                            </svg>
                        </span>
                    </div>
                    <strong class="metric-value">{premium_display}</strong>
                    <span class="metric-caption">Estimated Annual Premium</span>
                    <div class="meter-track"><div class="meter-fill" style="width:66%"></div></div>
                </div>
                <div class="result-metric">
                    <div class="result-metric-header">
                        <span>Claim Risk</span>
                        <span class="result-icon" aria-hidden="true">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                 stroke-linecap="round" stroke-linejoin="round">
                                <path d="M12 3 19 6v5c0 4.8-2.9 8-7 10-4.1-2-7-5.2-7-10V6l7-3Z"/>
                                <path d="m9.3 12 1.8 1.8 3.8-4"/>
                            </svg>
                        </span>
                    </div>
                    <strong class="metric-value risk-value {risk_class}">{prediction["risk"]}</strong>
                    <span class="metric-caption">Predicted Claim Risk</span>
                    <div class="risk-meter-labels"><span>Low</span><span>High</span></div>
                    <div class="meter-track"><div class="meter-fill" style="width:{risk_width};background:{risk_color}"></div></div>
                </div>
            </div>
            <div class="summary-panel">
                <h3>Prediction Summary</h3>
                <p>Submitted customer information.</p>
                <div class="summary-grid">{summary_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="disclaimer">
        <span class="disclaimer-icon" aria-hidden="true">ⓘ</span>
        <div>
            <strong>Important Note</strong>
            This prediction is generated using a machine learning model trained on synthetic insurance data and is
            intended for demonstration and educational purposes only. It should not be used as a real insurance
            underwriting decision.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
