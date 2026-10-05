from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent
CSS_PATH = ROOT_DIR / "style.css"

THEMES = {
    "light": {
        "background": "#faf8f5",
        "background-secondary": "#f5f2ee",
        "surface": "#ffffff",
        "surface-raised": "#ffffff",
        "surface-inset": "#fcfbf9",
        "text": "#1e1b18",
        "text-secondary": "#716a64",
        "text-tertiary": "#928a83",
        "border": "#ebe7e2",
        "border-strong": "#ded8d1",
        "accent": "#f97316",
        "accent-hover": "#ea580c",
        "accent-soft": "#fff2e9",
        "accent-contrast": "#ffffff",
        "success": "#16855b",
        "success-soft": "#e9f7ef",
        "warning": "#bd7800",
        "warning-soft": "#fff5db",
        "error": "#c24132",
        "error-soft": "#fff0ed",
        "shadow": "0 2px 5px rgba(48, 35, 22, 0.04)",
        "shadow-raised": "0 8px 24px rgba(48, 35, 22, 0.07)",
        "shadow-accent": "0 8px 18px rgba(249, 115, 22, 0.18)",
        "chart-1": "#f97316",
        "chart-2": "#16855b",
        "chart-3": "#4f7cac",
        "chart-4": "#bd7800",
        "chart-grid": "#ebe7e2",
        "color-scheme": "light",
    },
    "dark": {
        "background": "#14110f",
        "background-secondary": "#1b1715",
        "surface": "#25201d",
        "surface-raised": "#2b2521",
        "surface-inset": "#1e1a17",
        "text": "#f7f3ef",
        "text-secondary": "#b1a69d",
        "text-tertiary": "#91857c",
        "border": "#3a322d",
        "border-strong": "#4b4039",
        "accent": "#fb7920",
        "accent-hover": "#ff8a36",
        "accent-soft": "#442a19",
        "accent-contrast": "#ffffff",
        "success": "#58c98e",
        "success-soft": "#193b2a",
        "warning": "#f2bf5b",
        "warning-soft": "#463817",
        "error": "#ff8677",
        "error-soft": "#482421",
        "shadow": "0 2px 5px rgba(0, 0, 0, 0.16)",
        "shadow-raised": "0 8px 24px rgba(0, 0, 0, 0.22)",
        "shadow-accent": "0 8px 18px rgba(0, 0, 0, 0.22)",
        "chart-1": "#fb7920",
        "chart-2": "#58c98e",
        "chart-3": "#79aee8",
        "chart-4": "#f2bf5b",
        "chart-grid": "#3a322d",
        "color-scheme": "dark",
    },
}


def load_theme() -> str:
    theme = st.session_state.get("theme", "light")
    tokens = ";".join(f"--{name}:{value}" for name, value in THEMES[theme].items())
    css = CSS_PATH.read_text(encoding="utf-8")
    st.markdown(
        f"<style>:root,.stApp{{{tokens}}}{css}</style>",
        unsafe_allow_html=True,
    )
    return theme


def render_header() -> str:
    st.session_state.setdefault("theme", "light")

    def toggle_theme() -> None:
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

    left, predict_link, about_link, right = st.columns(
        [7.1, 1.2, 1.2, 0.65],
        vertical_alignment="center",
    )
    with left:
        st.markdown(
            """
            <div class="app-header">
                <div class="brand-mark" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                         stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 3 19 6v5c0 4.8-2.9 8-7 10-4.1-2-7-5.2-7-10V6l7-3Z"/>
                        <path d="m9.3 12 1.8 1.8 3.8-4"/>
                    </svg>
                </div>
                <div class="brand-copy">
                    <strong>Insurance Claim Risk &amp; Premium Predictor</strong>
                    <span>AI-powered insurance prediction based on customer and policy information</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with predict_link:
        st.page_link("pages/1_Predict.py", label="Predict")
    with about_link:
        st.page_link("pages/2_About_Project.py", label="About")
    with right:
        next_theme = "light" if st.session_state.theme == "dark" else "dark"
        icon = "☀" if next_theme == "light" else "☾"
        st.button(
            icon,
            key="theme_toggle",
            help=f"Switch to {next_theme} mode",
            on_click=toggle_theme,
        )
    return load_theme()


def format_inr(value: float, decimals: int = 0) -> str:
    formatted = f"{abs(value):.{decimals}f}"
    whole, separator, fraction = formatted.partition(".")
    groups = [whole[-3:]] if len(whole) > 3 else [whole]
    whole = whole[:-3] if len(whole) > 3 else ""
    while whole:
        groups.insert(0, whole[-2:])
        whole = whole[:-2]
    amount = ",".join(groups)
    if separator:
        amount = f"{amount}.{fraction}"
    if value < 0:
        amount = f"-{amount}"
    return f"₹{amount}"
