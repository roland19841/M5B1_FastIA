import os
import requests
import streamlit as st
from loguru import logger

API_URL = os.getenv("API_URL", "http://backend:8000")

st.set_page_config(page_title="FastIA Template", page_icon="🧮")
st.title("🧮 FastIA — Template IA (Minimal)")
st.write("Entrez un entier, l'API renvoie son carré.")

value = st.number_input("Entier", step=1, value=2, format="%d")

if st.button("Calculer le carré"):
    try:
        logger.info(f"Frontend: envoi valeur={value} vers API {API_URL}/calcul")
        resp = requests.post(f"{API_URL}/calcul", json={"value": int(value)}, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        st.success(f"Résultat : {data['result']}")
        logger.info(f"Frontend: résultat reçu={data}")
    except Exception as e:
        logger.exception("Frontend: erreur appel API")
        st.error(f"Erreur : {e}")
