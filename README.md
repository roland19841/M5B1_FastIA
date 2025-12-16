# FastIA – Template MLOps minimal (Streamlit + FastAPI + Docker + CI)

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

Lancement local :
```bash
streamlit run frontend/app.py
```

---

## 🔧 Backend (FastAPI)

### Routes disponibles
| Méthode | Route      | Description |
|------|------------|------------|
| GET  | `/`        | Message de bienvenue |
| GET  | `/health`  | Vérification de l’état de l’API |
| POST | `/calcul`  | Retourne le carré d’un entier |

### Exemple d’appel
```bash
curl -X POST http://localhost:8000/calcul \
  -H "Content-Type: application/json" \
  -d '{"value": 5}'
```

Réponse :
```json
{ "result": 25 }
```

- Validation des entrées via **Pydantic**
- Logique métier isolée dans `modules/calcul.py`
- Logs via **Loguru**

---

## 🧪 Tests

Les tests unitaires sont écrits avec **pytest** et couvrent la fonction `calcul()`.

Lancement local :
```bash
cd backend
python -m pytest -q
```

---

## 🐳 Docker & Docker Compose

Lancer l’application complète :
```bash
docker compose up --build
```

Services exposés :
- Frontend : http://localhost:8501
- Backend : http://localhost:8000
- Healthcheck : http://localhost:8000/health

Logs :
```bash
docker compose logs -f
```

---

## 🔄 CI/CD – GitHub Actions

- Exécution automatique des tests à chaque push sur `main` ou `dev`
- Vérification continue de la qualité du code backend

---

## 📦 Versioning

Le projet suit la convention **Semantic Versioning (SemVer)** :
```
vMAJOR.MINOR.PATCH
```

---

## ✅ Conformité aux exigences pédagogiques

- Frontend Streamlit fonctionnel
- API FastAPI avec 3 routes
- Logique métier isolée et testée
- Logs via Loguru
- Tests automatisés avec pytest
- Docker & Docker Compose opérationnels
- CI GitHub Actions fonctionnelle
- Structure claire et maintenable

---

Projet réalisé dans le cadre d’un exercice MLOps – FastIA
