# FastIA — Template minimal (Frontend Streamlit + API FastAPI)

## Architecture
- `frontend/` : Streamlit UI + Loguru
- `backend/` : FastAPI + Pydantic + Loguru + tests pytest
- `docker-compose.yml` : lance uniquement frontend + backend
- `.github/workflows/test.yml` : CI qui exécute pytest sur le backend

## Routes API
- `GET /` : message de bienvenue
- `GET /health` : status ok
- `POST /calcul` : renvoie le carré d’un entier

Exemple:
```bash
curl -X POST http://localhost:8000/calcul \
  -H "Content-Type: application/json" \
  -d '{"value": 7}'
```

Réponse JSON : 
```bash
{"result":49}
```

![Backend tests](https://github.com/<user>/<repo>/actions/workflows/test.yml/badge.svg)
