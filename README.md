# Modélisation du risque de crédit et optimisation d'un portefeuille de prêts

## Application

Une application Streamlit permet d'explorer les résultats du modèle et
d'analyser l'effet du seuil d'acceptation sur le portefeuille de prêts.

[Accéder à l'application](https://credit-risk-portfolio.streamlit.app/)

---

## Présentation

Ce projet porte sur la modélisation du risque de défaut à partir de données
relatives aux caractéristiques des emprunteurs et des prêts.

L'analyse poursuit deux objectifs complémentaires :

- estimer le risque de défaut à l'aide de modèles de classification ;
- étudier l'impact des décisions d'acceptation sur la qualité et la
  rentabilité du portefeuille.

Une Régression Logistique est utilisée comme modèle de référence, puis
comparée à XGBoost. Les probabilités produites par le modèle sont ensuite
utilisées dans une simulation de portefeuille afin d'étudier différents
seuils de décision.

---

## Problématique

Dans une décision de crédit, le seuil d'acceptation influence directement
la composition du portefeuille.

Un seuil trop permissif augmente le nombre de prêts accordés, mais peut
également augmenter la proportion de défauts. À l'inverse, une politique
plus restrictive réduit l'exposition au risque mais limite le volume
d'activité.

Le projet cherche donc à étudier le compromis entre :

- taux d'acceptation ;
- taux de défaut du portefeuille ;
- performance du modèle de scoring ;
- résultat financier estimé.

---

## Données

Le jeu de données contient des informations sur les emprunteurs et les
caractéristiques des prêts.

Les principales variables utilisées sont :

| Variable | Description |
|---|---|
| `person_income` | Revenu annuel de l'emprunteur |
| `person_emp_length` | Ancienneté professionnelle |
| `loan_amnt` | Montant du prêt |
| `loan_int_rate` | Taux d'intérêt |
| `loan_percent_income` | Ratio entre le montant du prêt et le revenu |
| `loan_grade` | Grade associé au prêt |
| `person_home_ownership` | Statut d'occupation du logement |
| `cb_person_default_on_file` | Présence d'un défaut dans l'historique |
| `loan_status` | Variable cible : défaut / non-défaut |

Le jeu de données présente un déséquilibre entre les deux classes, ce qui
nécessite de compléter l'accuracy par des métriques spécifiques à la
détection des défauts.

---

## Méthodologie

Le projet suit le pipeline suivant :

```text
Données emprunteurs et prêts
            │
            ▼
 Préparation des données
            │
            ▼
 Analyse exploratoire
            │
            ▼
Traitement du déséquilibre
            │
            ▼
 ┌──────────┴──────────┐
 ▼                     ▼
Régression          XGBoost
Logistique
 └──────────┬──────────┘
            ▼
 Évaluation des modèles
            │
            ▼
Analyse des probabilités
            │
            ▼
Simulation du portefeuille
            │
            ▼
Analyse des seuils d'acceptation
