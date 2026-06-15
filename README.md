# ETL Pipeline - Users & Posts (JSONPlaceholder + FastAPI Mock)

Pipeline de ETL en Python que extrae datos de una API REST (FastAPI local)
con fallback a archivos JSON mock, los transforma usando pandas y los carga
en una base de datos SQLite para análisis posterior mediante SQL.

## Flujo
1. **Extract**:
    - Obtiene datos desde una API REST local (FastAPI)
    - Si la API no esta disponible, usa archivos JSON como fallback
2. **Transform**:
    - users:
        - Aplana columnas anidadas (`address` -> `city`, `company` -> `company_name`)
        - Detecta y elimina emails nulos/duplicados
    - posts:
        - Renombrado de columnas (`userId` -> `user_id`)
        - Eliminación de títulos nulos.
3. **Load**:
    - Inserta los datos en una base de datos SQLite
    - Crea las tablas `users` y `posts`

## Base de datos

Se crean dos tablas:
- users
- posts

Relación:
- users.id -> posts.user_id

## Cómo correrlo

```bash
pip install -r requirements.txt
uvicorn api.server:app --reload
python main.py
```

## Tecnologías
- Python
- pandas
- FastAPI
- SQLite
- requests
