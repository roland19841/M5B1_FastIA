# FastIA – Template MLOps minimal (Streamlit + FastAPI + Docker + CI)

## 🚀 Démarrage rapide

### Prérequis
- **Git** installé → https://git-scm.com/
- **Docker Desktop** (avec Docker Compose)
- **Python 3.11** (pour exécution locale sans Docker, optionnel)

---

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/<USER>/<REPO>.git
cd <REPO>
```

---

### 2️⃣ Lancer avec Docker (recommandé)
Cette méthode garantit un environnement **identique pour tous**.

```bash
docker compose up --build
```

Accès :
- Frontend : http://localhost:8501
- Backend : http://localhost:8000
- Healthcheck : http://localhost:8000/health

Arrêter :
```bash
docker compose down
```

---

### 3️⃣ Lancer en local sans Docker (optionnel)

#### Backend
```bash
cd backend
python3.11 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q
uvicorn main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
python3.11 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
Puis :
```bash
streamlit run app.py
```

---

Ce dépôt fournit une **architecture de base reproductible** pour les projets IA de FastIA.  
Il propose un frontend simple, une API FastAPI structurée, des tests automatisés et une chaîne CI/CD via GitHub Actions.

---

## 🎯 Objectifs du projet

- Mettre en place une architecture logicielle propre et extensible
- Séparer clairement frontend, backend et logique métier
- Conteneuriser l’environnement avec Docker
- Automatiser les tests backend via GitHub Actions
- Servir de **template réutilisable** pour de futurs projets IA

---

## 🧱 Architecture du projet

```
.
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── backend/
│   ├── main.py
│   ├── modules/
│   │   ├── __init__.py
│   │   └── calcul.py
│   ├── tests/
│   │   └── test_calcul.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 🖥️ Frontend (Streamlit)

- Interface utilisateur simple
- Champ de saisie d’un entier
- Appel REST vers l’API backend
- Affichage du résultat (carré de l’entier)
- Logs via **Loguru**

---

## 🔧 Backend (FastAPI)

### Routes disponibles
| Méthode | Route      | Description |
|------|------------|------------|
| GET  | `/`        | Message de bienvenue |
| GET  | `/health`  | Vérification de l’état de l’API |
| POST | `/calcul`  | Retourne le carré d’un entier |

---

## 🧪 Tests

Les tests unitaires sont écrits avec **pytest** et couvrent la fonction `calcul()`.

```bash
cd backend
python -m pytest -q
```

---

## 🐳 Docker & Docker Compose

```bash
docker compose up --build
```

---

## 🔄 CI/CD – GitHub Actions

- Tests automatisés à chaque push sur `main` ou `dev`
- Validation continue du backend

---

## 📦 Versioning

Le projet suit la convention **Semantic Versioning (SemVer)** :
```
vMAJOR.MINOR.PATCH
```

---

Projet réalisé dans le cadre d’un exercice MLOps – FastIA
