# GitHub Actions Workshop

**CI/CD, Docker, Docker Hub y despliegue por ambientes con Render**

Este repositorio es una aplicación de ejemplo en Python que demuestra los fundamentos de **CI/CD** utilizando GitHub Actions, Docker y Render.

## Enlaces de acceso

| Ambiente | URL | Swagger |
|----------|-----|---------|
| **Prod** | [https://github-actions-workshop-0zoi.onrender.com](https://github-actions-workshop-0zoi.onrender.com) | [Docs](https://github-actions-workshop-0zoi.onrender.com/docs) |
| **Dev** | [https://github-actions-workshop-dev-7jdm.onrender.com](https://github-actions-workshop-dev-7jdm.onrender.com) | [Docs](https://github-actions-workshop-dev-7jdm.onrender.com/docs) |

## Características

- Validación de código con **ruff** (linter)
- Pruebas automáticas con **pytest**
- Construcción de imagen **Docker**
- Push a **Docker Hub**
- Despliegue automático a **Render**
  - Rama `master` → Prod
  - Rama `dev` → Dev

## Requisitos del desarrollo

- Python 3.10+
- Docker
- Git

## Cómo ejecutar localmente

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest

# Ejecutar linting
ruff check .

# Ejecutar aplicación
python app/main.py
```