import streamlit as st

from theme import render_header


st.set_page_config(page_title="About Project", page_icon="📘", layout="wide")

render_header()

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
