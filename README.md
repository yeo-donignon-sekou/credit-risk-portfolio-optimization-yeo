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



```

---

## Préparation des données

La préparation des données comprend plusieurs étapes destinées à obtenir un
jeu de données exploitable pour la modélisation :

- contrôle des valeurs manquantes ;
- traitement des variables numériques et catégorielles ;
- analyse des valeurs atypiques ;
- encodage des variables catégorielles ;
- préparation des variables explicatives et de la variable cible.

Une attention particulière est portée à la distribution de `loan_status`,
le nombre de prêts en défaut étant inférieur au nombre de prêts sans défaut.

---

## Analyse exploratoire

L'analyse exploratoire permet d'étudier les caractéristiques des emprunteurs
et des prêts ainsi que leurs relations avec le défaut.

L'analyse porte notamment sur :

- le revenu des emprunteurs ;
- le montant des prêts ;
- le taux d'intérêt ;
- le ratio prêt/revenu ;
- le grade du prêt ;
- l'ancienneté professionnelle ;
- l'historique de défaut.

Cette étape permet également d'identifier les différences de distribution
entre les prêts en défaut et les prêts sans défaut.

---

## Gestion du déséquilibre des classes

La variable cible présente un déséquilibre entre les défauts et les
non-défauts.

Une stratégie d'**undersampling** est appliquée aux données d'entraînement
afin de construire un échantillon plus équilibré et d'améliorer la détection
de la classe défaut.

L'évaluation des modèles ne repose donc pas uniquement sur l'accuracy.
Le rappel de la classe défaut, la précision et la capacité de discrimination
du modèle sont également pris en compte.

---

## Modélisation

### Régression Logistique

La Régression Logistique est utilisée comme modèle de référence.

Elle fournit une première estimation du risque de défaut et permet d'établir
une baseline avant l'utilisation d'un modèle plus flexible.

Les performances sont évaluées sur les données de test à l'aide de plusieurs
métriques de classification.

### XGBoost

Un modèle **XGBoost** est ensuite entraîné afin de prendre en compte des
relations non linéaires et des interactions plus complexes entre les
caractéristiques des emprunteurs.

L'objectif est de comparer ses performances à celles de la Régression
Logistique, en particulier pour la détection des prêts en défaut.

---

## Évaluation des modèles

Les modèles sont comparés à partir de plusieurs indicateurs :

- Accuracy ;
- Précision ;
- Rappel ;
- F1-score ;
- ROC-AUC ;
- Matrice de confusion.

Une attention particulière est accordée au **rappel de la classe défaut**.
Dans un problème de risque de crédit, un faux négatif correspond à un prêt
en défaut que le modèle classe comme non défaillant.

Les résultats montrent une amélioration de la détection des défauts avec
XGBoost par rapport au modèle de référence.

---

## Analyse des probabilités prédites

Les probabilités produites par XGBoost sont utilisées pour classer les prêts
selon leur niveau de risque.

Un **Reliability Diagram** est également utilisé afin d'étudier la relation
entre les probabilités prédites et les fréquences de défaut observées.

L'utilisation de l'undersampling lors de l'entraînement modifie la proportion
de défauts observée par le modèle. Les probabilités obtenues doivent donc
être interprétées avec prudence lorsqu'elles sont utilisées directement
comme estimations du risque de défaut.

---

## Simulation du portefeuille de prêts

Les scores produits par le modèle sont ensuite utilisés pour simuler
différentes politiques d'acceptation.

Les prêts sont classés selon leur niveau de risque estimé, puis plusieurs
taux d'acceptation sont étudiés.

Pour chaque stratégie, l'analyse porte notamment sur :

- le nombre de prêts acceptés ;
- le taux d'acceptation ;
- le nombre de défauts observés ;
- le Bad Rate du portefeuille ;
- le résultat financier estimé.

Cette approche permet de relier les performances du modèle de scoring à la
composition du portefeuille de prêts.

---

## Analyse du seuil d'acceptation

La simulation permet d'étudier l'évolution du risque du portefeuille lorsque
le taux d'acceptation varie.

Dans le scénario étudié, un **taux d'acceptation de 70 %** conduit à un
**Bad Rate de 3,98 %**.

| Indicateur | Résultat |
|---|---:|
| Taux d'acceptation | 70 % |
| Bad Rate | 3,98 % |

Ce résultat illustre le compromis entre le volume de prêts acceptés et la
qualité du portefeuille.

Le seuil obtenu reste spécifique aux données et aux hypothèses retenues dans
la simulation ; il ne constitue pas une règle générale d'octroi de crédit.

---

## Principaux résultats

Le projet permet de mettre en évidence plusieurs éléments :

- comparaison d'une **Régression Logistique** et de **XGBoost** pour la
  classification du risque de défaut ;
- prise en compte du déséquilibre des classes par undersampling ;
- analyse des performances au-delà de la seule accuracy ;
- utilisation des probabilités prédites pour classer les demandes selon
  leur niveau de risque ;
- simulation de plusieurs politiques d'acceptation ;
- analyse de l'évolution du Bad Rate en fonction du volume de prêts retenus ;
- obtention d'un **Bad Rate de 3,98 % pour un taux d'acceptation de 70 %**
  dans le scénario étudié.

---

## Limites

Les résultats doivent être interprétés en tenant compte de plusieurs limites :

- l'undersampling modifie la distribution des classes pendant
  l'entraînement ;
- les probabilités prédites nécessitent une analyse de calibration avant
  d'être assimilées à des probabilités de défaut directement exploitables ;
- les résultats dépendent des caractéristiques et de la représentativité
  du jeu de données ;
- la simulation financière repose sur des hypothèses simplifiées ;
- le seuil d'acceptation identifié est propre au portefeuille et au cadre
  de simulation étudiés.

---

## Technologies utilisées

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **XGBoost**
- **Matplotlib**
- **Seaborn**
- **Streamlit**
- **Jupyter Notebook**

---

## Pistes d'amélioration

Plusieurs extensions peuvent être envisagées :

- calibration des probabilités prédites ;
- optimisation des hyperparamètres ;
- analyse de l'interprétabilité des prédictions ;
- validation temporelle du modèle ;
- étude de la stabilité des variables et des performances ;
- enrichissement de la simulation financière ;
- suivi de la performance du portefeuille dans le temps.

---

## Auteur

**YEO Donignon Sékou**  
Master 2 Ingénierie Mathématique — Science des données  
Université Côte d'Azur
