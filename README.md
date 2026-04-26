<div align="center">

# 🏪 Automatisation des Ventes
### Projet de Fin d'Année — Faculté des Sciences de Tunis

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c?style=for-the-badge)
![CSV](https://img.shields.io/badge/CSV-Module-green?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![Status](https://img.shields.io/badge/Status-✅%20Complet-success?style=for-the-badge)

</div>

---

## 📋 Description

> **Problématique** : Une entreprise de e-commerce utilisait un fichier Excel pour suivre ses ventes. Le volume de données devenait trop important pour un tableur classique.

**Solution** : Un script Python complet et modulaire qui automatise entièrement l'analyse des données de ventes — depuis la lecture du fichier CSV jusqu'à la génération de graphiques professionnels.

---

## 👥 Équipe du Projet

| Nom | Rôle |
|-----|------|
| **Maher Zouari** | Développeur principal |
| **Nadine Naoui** | Développeur |
| **Amal Guebli** | Développeur |

> 👩‍🏫 **Encadrante** : Mme. Imene Amira  
> 🏛️ **Établissement** : Faculté des Sciences de Tunis — Département Mathématique  
> 📅 **Année universitaire** : 2025 / 2026  
> 📚 **Matière** : Logiciels  

---

## ✅ Travail Réalisé

| # | Fonctionnalité | Statut |
|---|---------------|--------|
| 1 | Génération automatique du fichier `ventes.csv` | ✅ Réalisé |
| 2 | Calcul du Chiffre d'Affaires Brut (Prix × Quantité) | ✅ Réalisé |
| 3 | Application des remises → CA Net | ✅ Réalisé |
| 4 | Calcul de la TVA à 20% sur le CA Net | ✅ Réalisé |
| 5 | Affichage du CA Total de l'entreprise | ✅ Réalisé |
| 6 | Identification du produit le plus performant | ✅ Réalisé |
| 7 | Export automatique vers `resultats_final.csv` | ✅ Réalisé |
| 8 | 📊 Graphiques Matplotlib *(Bonus 1)* | ✅ Réalisé |
| 9 | 📂 Lecture dynamique de fichiers CSV *(Bonus 2)* | ✅ Réalisé |

---

## 📁 Structure du Projet
📁 PFA-Ventes/
├── 📄 Main.py                 → Script principal Python
├── 📄 ventes.csv              → Données d'entrée (généré automatiquement)
├── 📄 resultats_final.csv     → Résultats calculés et exportés
├── 📄 graphique_ca.png        → 3 graphiques générés par Matplotlib
├── 📄 .gitignore              → Exclut .venv et pycache
└── 📄 README.md               → Documentation du projet

---

## 🧮 Formules Mathématiques Utilisées
CA_Brut  =  Prix × Quantité
CA_Net   =  CA_Brut × (1 - Remise / 100)
TVA      =  CA_Net × 0.20
TTC      =  CA_Net + TVA
CA_Total =  Σ( CA_Net_i )   pour i = 1 à n

---

## 🏗️ Architecture du Code
main()
├── generer_ventes_csv()    → Génère le fichier CSV automatiquement
├── lire_ventes()           → Lecture du CSV avec DictReader
├── calculer()              → CA Brut, CA Net, TVA, TTC
├── ca_total()              → Somme des CA Net
├── tva_totale()            → Somme des TVA
├── ttc_total()             → Somme des TTC
├── meilleur_produit()      → argmax(CA_Net) via lambda
├── exporter()              → Export CSV avec DictWriter
└── afficher_graphiques()   → 3 graphiques Matplotlib

---

## ▶️ Installation et Exécution

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/maherzouari0/PFA-Ventes.git
cd PFA-Ventes
```

### 2️⃣ Créer l'environnement virtuel
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Installer les dépendances
```bash
pip install matplotlib
```

### 4️⃣ Lancer le script
```bash
py Main.py
```

---

## 📊 Résultats Obtenus
=======================================================
PFA — Automatisation des Ventes
Maher Zouari | Nadine Naoui | Amal Guebli
✅ Fichier 'ventes.csv' généré automatiquement
✅ 10 produits chargés depuis 'ventes.csv'
ID     Prix   Qté   Remise   CA Brut   CA Net    TVA     TTC
101   15.00     3     10%     45.00    40.50     8.10   48.60
102   25.00     2      5%     50.00    47.50     9.50   57.00
103   10.00     5      0%     50.00    50.00    10.00   60.00
104   50.00     1     20%     50.00    40.00     8.00   48.00
105   30.00     4     15%    120.00   102.00    20.40  122.40
106   45.00     3     10%    135.00   121.50    24.30  145.80
107   20.00     6      0%    120.00   120.00    24.00  144.00
108   60.00     2     25%    120.00    90.00    18.00  108.00
109   35.00     4      5%    140.00   133.00    26.60  159.60
110   80.00     1     30%     80.00    56.00    11.20   67.20
💰 CA Total (HT)  : 800.50 €
🧾 TVA Totale     : 160.10 €
💳 Total TTC      : 960.60 €
🏆 Meilleur produit : ID 109 avec un CA Net de 133.00 €
✅ Résultats exportés dans 'resultats_final.csv'
✅ Graphiques sauvegardés dans 'graphique_ca.png'
✅ Analyse terminée avec succès !

---

## 📈 Graphiques Générés

Le script génère automatiquement **3 graphiques** dans `graphique_ca.png` :

| Graphique | Type | Description |
|-----------|------|-------------|
| Graphique 1 | Bar chart comparatif | CA Brut vs CA Net par produit |
| Graphique 2 | Bar chart | Montant TVA par produit |
| Graphique 3 | Pie chart | Répartition du CA Net (%) |

---

## 🔬 Analyse des Résultats

- 🥇 **Produit ID 109** est le meilleur : prix raisonnable (35€), volume élevé (4 unités) et faible remise (5%)
- ⚠️ **ID 108 et ID 110** ont des prix élevés mais leurs remises importantes (25% et 30%) réduisent significativement leur CA Net
- 📊 Les **3 meilleurs produits** (ID 109, 106, 107) représentent **46.8%** du CA Total

---

## ⚡ Complexité Algorithmique

Le script utilise une seule boucle sur n produits → **Complexité O(n)**
Volume          Temps estimé
10 produits  →  < 0.01 seconde
1 000        →  < 0.1 seconde
100 000      →  < 2 secondes
1 000 000+   →  Recommandé : passer à pandas

---

## 🛠️ Technologies Utilisées

| Technologie | Version | Utilisation |
|-------------|---------|-------------|
| Python 3 | 3.x | Langage principal |
| VS Code | 1.x | Environnement de développement |
| Matplotlib | 3.x | Génération des graphiques |
| Module csv | stdlib | Lecture/écriture CSV |
| Module os | stdlib | Vérification des fichiers |
| Git | 2.x | Gestion de version |
| GitHub | — | Hébergement du projet |

---

## 🚀 Perspectives d'Évolution

- 🖥️ Interface graphique avec **Tkinter** ou **PyQt**
- 🗄️ Base de données **SQLite** ou **PostgreSQL**
- 🌐 Tableau de bord web avec **Streamlit** ou **Flask**
- ⏰ Automatisation schedulée avec **Cron** / **Task Scheduler**
- 📦 Traitement de très grands volumes avec **pandas** + **numpy**

---

<div align="center">

**Faculté des Sciences de Tunis — 2025/2026**  
*Département Mathématique — Matière : Logiciels*

</div>
