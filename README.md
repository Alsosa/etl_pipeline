# ETL Pipeline - JSONPlaceholder Users & Posts

Pipeline simple de ETL que extrae datos usando archivos JSON como mock
de una API, los transforma con pandas (limpieza de duplicados y nulos,
normalización de columnas anidadas) y los exporta a una base de datos SQLite.

## Flujo
1. **Extract**: obtiene datos de usuarios y posteos desde el JSON local
2. **Transform**:
    - users:
        - Aplana columnas anidadas (`address` -> `city`, `company` -> `company_name`)
        - Detecta y elimina emails nulos/duplicados
    - posts:
        - Renombrado de columnas (`userId` -> `user_id`)
        - Eliminación de títulos nulos.
3. **Load**: inserta los datos en una base de datos SQLite

## Base de datos

Se crean dos tablas:
- users
- posts

Relación:
- users.id -> posts.user_id

## Cómo correrlo

```bash
pip install -r requirements.txt
python main.py
```

## Tecnologías
- Python
- pandas
