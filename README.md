# ETL Pipeline - Users & Posts (FastAPI + Local JSON fallback)

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

# 1. Crear entorno virtual
```bash
python -m venv venv
```

# 2. Activar entorno virtual
# Windows:
```bash
venv\Scripts\activate
```

# Mac / Linux:
```bash
source venv/bin/activate
```

# 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

# Ejecucion de la API
```bash
uvicorn api.server:app --reload
```

# La API quedará disponible en:
```bash
http://127.0.0.1:8000/users
http://127.0.0.1:8000/posts
http://127.0.0.1:8000/docs
```

# Ejecucion del ETL
```bash
python -m etl.main
```

## Tecnologías
- Python
- pandas
- FastAPI
- SQLite
- requests
