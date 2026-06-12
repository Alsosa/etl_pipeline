# ETL Pipeline - JSONPlaceholder Users

Pipeline simple de ETL que extrae datos de una API REST, los transforma
con pandas (limpieza de duplicados y nulos, normalización de columnas
anidadas) y los exporta a CSV.

## Flujo
1. **Extract**: obtiene datos de usuarios desde `jsonplaceholder.typicode.com/users`
2. **Transform**: 
   - Aplana columnas anidadas (`address` -> `city`, `company` -> `company_name`)
   - Detecta y elimina emails nulos/duplicados
3. **Load**: guarda el resultado en `employees_df.csv`

## Cómo correrlo

```bash
pip install -r requirements.txt
python main.py
```

## Tecnologías
- Python
- pandas
- requests
