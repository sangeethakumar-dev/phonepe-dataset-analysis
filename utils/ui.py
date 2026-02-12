from pathlib import Path
import streamlit as st

def load_phonepe_theme():
    base_dir = Path(__file__).resolve().parent.parent
    css_path = base_dir / "styles" / "phonepe_theme.css"

    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
