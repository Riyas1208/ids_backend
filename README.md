# ids_api 

This repository is for an IDS + Vulnerability Scanner backend using FastAPI.

Features included:
- FastAPI app with versioned routers
- JWT auth (simple implementation)
- ML service scaffold for loading a joblib model
- Async scanning service wrappers (nmap, nikto, sqlmap)
- Background task queue using RQ + Redis
- Dockerfile + docker-compose for app + worker + redis
- Rate limiting (using slowapi)
- Logging config
- Basic tests

**Important:** This scaffold contains placeholders and example settings. Review and harden before production use.
