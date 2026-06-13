import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle
model = joblib.load("model/xgboost_model.pkl")
model_columns = joblib.load("model/model_columns.pkl")
strategy_table = joblib.load("model/strategy_table.pkl")

# Configuration
st.set_page_config(page_title="Credit Risk App", layout="wide")

# Titre
st.title("🏦 Credit Risk Scoring & Portfolio Optimisation")

st.write(
    "Application de prédiction du risque de défaut de crédit "
    "utilisant XGBoost et la modélisation de la Probabilité de Défaut (PD)."
)

# Sidebar
st.sidebar.header("Informations de l'emprunteur")

person_age = st.sidebar.number_input(
    "Âge", min_value=18, max_value=100, value=30
)

person_income = st.sidebar.number_input(
    "Revenu annuel (€)", min_value=0, value=50000
)

person_emp_length = st.sidebar.number_input(
    "Ancienneté professionnelle", min_value=0.0, value=5.0
)

loan_amnt = st.sidebar.number_input(
    "Montant du prêt (€)", min_value=0, value=10000
)

loan_int_rate = st.sidebar.number_input(
    "Taux d'intérêt (%)", min_value=0.0, value=10.0
)

cb_person_cred_hist_length = st.sidebar.number_input(
    "Historique de crédit", min_value=0, value=5
)

person_home_ownership = st.sidebar.selectbox(
    "Statut logement",
    ["RENT", "OWN", "MORTGAGE", "OTHER"]
)

loan_intent = st.sidebar.selectbox(
    "Objectif du prêt",
    [
        "EDUCATION",
        "MEDICAL",
        "VENTURE",
        "PERSONAL",
        "DEBTCONSOLIDATION",
        "HOMEIMPROVEMENT"
    ]
)

loan_grade = st.sidebar.selectbox(
    "Grade du prêt",
    ["A", "B", "C", "D", "E", "F", "G"]
)

cb_person_default_on_file = st.sidebar.selectbox(
    "Historique de défaut",
    ["N", "Y"]
)

# Feature engineering
loan_percent_income = (
    loan_amnt / person_income if person_income > 0 else 0
)

# DataFrame utilisateur
input_data = pd.DataFrame({
    "person_age": [person_age],
    "person_income": [person_income],
    "person_emp_length": [person_emp_length],
    "loan_amnt": [loan_amnt],
    "loan_int_rate": [loan_int_rate],
    "loan_percent_income": [loan_percent_income],
    "cb_person_cred_hist_length": [cb_person_cred_hist_length],
    "person_home_ownership": [person_home_ownership],
    "loan_intent": [loan_intent],
    "loan_grade": [loan_grade],
    "cb_person_default_on_file": [cb_person_default_on_file]
})

# Encodage
input_encoded = pd.get_dummies(input_data, dtype=int)

# Alignement des colonnes
input_encoded = input_encoded.reindex(
    columns=model_columns,
    fill_value=0
)

# Bouton prédiction
if st.button("Prédire le risque de défaut"):

    probability = model.predict_proba(input_encoded)[0][1]

    st.subheader("📊 Résultat du scoring")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Probabilité de défaut",
        f"{probability:.2%}"
    )

    col2.metric(
        "Ratio prêt/revenu",
        f"{loan_percent_income:.2%}"
    )

    if probability < 0.30:
        col3.success("✅ Prêt accepté")
        st.success("Profil à risque faible.")

    elif probability < 0.70:
        col3.warning("⚠️ Analyse complémentaire")
        st.warning("Profil à risque modéré.")

    else:
        col3.error("❌ Prêt rejeté")
        st.error("Profil à risque élevé.")

    st.markdown("### Interprétation métier")

    st.write(
        f"Le modèle estime une probabilité de défaut "
        f"de **{probability:.2%}**."
    )

# Strategy Table
st.markdown("---")

st.subheader("💰 Strategy Table — Optimisation du portefeuille")

st.dataframe(strategy_table)
