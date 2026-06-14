# 🏦 Modélisation du Risque de Crédit & Optimisation de Portefeuille avec XGBoost


🚀 Testez l’application interactive de Credit Risk Scoring et explorez le modèle XGBoost en temps réel.

👉 https://https://credit-risk-portfolio.streamlit.app/


## 📌 Présentation du Projet

Ce projet porte sur la conception d’un pipeline complet de **modélisation du risque de crédit** visant à minimiser le risque de défaut tout en maximisant la rentabilité d’un portefeuille de prêts.

L’analyse va au-delà d’un simple problème de classification en intégrant un véritable cadre de **modélisation de la Probabilité de Défaut (Probability of Default – PD)** couplé à une stratégie d’optimisation financière du portefeuille.

À travers l’utilisation conjointe de la **Régression Logistique** et de **XGBoost**, ce projet démontre comment le Machine Learning peut être utilisé pour soutenir des décisions stratégiques dans les secteurs bancaire, assurantiel et financier.

Le livrable final est une **table stratégique dynamique** permettant de déterminer le seuil optimal d’acceptation des prêts afin d’équilibrer croissance du portefeuille et stabilité financière à long terme.

---

# 🎯 Objectif Métier

Les institutions financières sont confrontées à un compromis majeur :

* Rejeter trop de clients réduit le risque de défaut mais diminue les revenus générés par les intérêts.
* Accepter trop d’emprunteurs risqués augmente le volume de prêts mais entraîne d’importantes pertes financières liées aux défauts de remboursement.

L’objectif principal de ce projet est donc de :

✅ Réduire les pertes attendues
✅ Améliorer la détection des défauts de paiement
✅ Optimiser la stratégie d’acceptation des prêts
✅ Maximiser la rentabilité du portefeuille

---

# 📂 Présentation des Données

Le dataset contient des informations financières et comportementales sur les emprunteurs utilisées pour prédire le risque de défaut de crédit.

## Variables Principales

| Variable                    | Description                          |
| --------------------------- | ------------------------------------ |
| `person_income`             | Revenu annuel de l’emprunteur        |
| `person_emp_length`         | Ancienneté professionnelle           |
| `loan_amnt`                 | Montant du prêt demandé              |
| `loan_int_rate`             | Taux d’intérêt du prêt               |
| `loan_percent_income`       | Ratio prêt / revenu                  |
| `loan_grade`                | Niveau de risque attribué au prêt    |
| `person_home_ownership`     | Statut de propriété du logement      |
| `cb_person_default_on_file` | Historique de défaut                 |
| `loan_status`               | Variable cible (Défaut / Non-défaut) |

## Caractéristiques du Dataset

* 32 581 observations
* 12 variables
* Dataset déséquilibré :

  * 7 641 défauts
  * 24 940 non-défauts

---

# ⚙️ Pipeline du Projet

## 1️⃣ Nettoyage & Prétraitement des Données

* Détection des valeurs manquantes
* Imputation des données financières
* Détection des valeurs aberrantes
* Transformation des variables
* Encodage des variables catégorielles

---

## 2️⃣ Analyse Exploratoire des Données (EDA)

Une analyse approfondie a été réalisée afin d’identifier les principaux facteurs expliquant le risque de crédit :

* Analyse des montants de prêts
* Analyse des revenus des emprunteurs
* Étude des catégories de risque
* Analyse de la stabilité professionnelle
* Visualisation des taux de défaut
* Analyse des corrélations

---

## 3️⃣ Gestion du Déséquilibre des Classes

Le dataset présente un important déséquilibre entre les classes.

Afin d’améliorer la capacité du modèle à détecter les emprunteurs risqués :

* Une technique d’undersampling a été appliquée
* Un jeu d’entraînement équilibré a été construit
* L’optimisation du Recall est devenue un objectif stratégique

---

# 🤖 Modèles de Machine Learning

## 🔹 Régression Logistique (Modèle Baseline)

Une Régression Logistique a d’abord été implémentée afin d’établir un modèle de référence interprétable.

### Pourquoi la Régression Logistique ?

* Forte interprétabilité
* Analyse claire des coefficients
* Importance réglementaire dans les environnements bancaires
* Compréhension des relations linéaires entre les variables

### Limite Principale

Bien que le modèle obtienne une bonne accuracy globale, il reste limité dans la détection des relations complexes et non linéaires présentes dans les données financières.

---

## 🔹 XGBoost (Modèle Avancé)

Un classifieur XGBoost a ensuite été développé afin d’améliorer significativement les performances prédictives.

### Avantages de XGBoost

✅ Capture des relations non linéaires
✅ Gestion des interactions complexes entre variables
✅ Fort pouvoir prédictif
✅ Robustesse face aux différences d’échelle des variables
✅ Excellentes performances sur les données tabulaires financières

---

# 📊 Comparaison des Performances

| Métrique         | Régression Logistique | XGBoost |
| ---------------- | --------------------- | ------- |
| Accuracy         | 0.87                  | 0.89    |
| Recall (Défauts) | 0.55                  | 0.83    |
| ROC-AUC          | 0.76                  | 0.95    |

---

# 📈 Résultats Clés

## Résultats de la Régression Logistique

Le modèle baseline met en évidence le phénomène classique du **“Accuracy Trap”** dans les datasets de crédit déséquilibrés.

Bien que l’accuracy globale soit élevée, le modèle échoue à détecter une grande partie des emprunteurs réellement risqués.

### Interprétation Métier

Le modèle détecte principalement les défauts “évidents” mais ne parvient pas à capturer les profils de risque plus complexes.

---

## Résultats de XGBoost

XGBoost améliore considérablement la détection des prêts défaillants.

### Amélioration Stratégique

✅ +51 % d’amélioration du Recall
✅ Forte augmentation du score ROC-AUC
✅ Meilleure séparation entre emprunteurs risqués et non risqués

Cette amélioration réduit directement les pertes potentielles liées aux défauts de paiement.

---

# 📉 Calibration des Probabilités & Fiabilité du Modèle

Un diagramme de fiabilité (*Reliability Diagram*) a été utilisé afin d’évaluer la calibration des probabilités prédites.

## Observation

Étant donné que le modèle a été entraîné sur un dataset équilibré via undersampling, les probabilités prédites apparaissent légèrement surévaluées.

## Point Important

Même si XGBoost reste excellent pour classer les niveaux de risque, les probabilités brutes doivent être interprétées avec prudence lors de la mise en œuvre d’une stratégie financière réelle.

---

# 💰 Optimisation du Portefeuille de Prêts

Une simulation financière complète a été développée afin d’évaluer la rentabilité du portefeuille selon différents seuils d’acceptation des prêts.

L’analyse montre que :

* Un taux d’acceptation de 100 % maximise le volume de prêts
* Mais augmente fortement les pertes attendues

---

# ✅ Stratégie Optimale Identifiée

## 📌 Seuil Optimal de Maximisation du Profit : 70 % d’Acceptation

| Indicateur         | Valeur      |
| ------------------ | ----------- |
| Taux d’acceptation | 70 %        |
| Bad Rate           | 3.98 %      |
| Profit Net Estimé  | 7 133 604 € |

---

# 🧠 Impact Business

Ce projet démontre comment le Machine Learning peut être transformé en véritable outil d’aide à la décision financière.

## Bénéfices Stratégiques

✅ Amélioration de la gestion du risque crédit
✅ Meilleure qualité du portefeuille de prêts
✅ Réduction des pertes attendues
✅ Augmentation de la rentabilité
✅ Stratégie de crédit pilotée par la donnée
✅ Optimisation de l’allocation du capital

---

# 🛠️ Stack Technologique

## Programmation & Analyse

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost

## Visualisation de Données

* Matplotlib
* Seaborn

## Concepts de Machine Learning

* Probability of Default (PD)
* ROC-AUC
* Optimisation du Recall
* Feature Importance
* Reliability Diagram
* Simulation Financière

---

# 📌 Perspectives d’Amélioration

Plusieurs extensions pourraient renforcer davantage le projet :

* Analyse d’explicabilité avec SHAP
* Calibration avancée des probabilités
* Optimisation des hyperparamètres
* Déploiement avec Streamlit
* API de scoring en temps réel
* Intégration de métriques réglementaires Bâle II / III

---

# 📚 Conclusion

Ce projet illustre un workflow complet de **Credit Risk Analytics** combinant :

* Modélisation financière
* Machine Learning
* Stratégie métier
* Optimisation de portefeuille

Le passage d’un simple modèle prédictif à un véritable moteur stratégique de décision financière démontre comment les techniques avancées de Data Science peuvent créer une forte valeur ajoutée dans les secteurs bancaire et financier.

---

# 👤 Auteur

**YEO Donignon Sékou**
Master 2 – Data Science & Intelligence Artificielle
Ingénierie Mathématique | Machine Learning | Finance Quantitative | Risk Analytics
