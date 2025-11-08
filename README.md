## Q1 — Code Organization & Django ORM

### Files
- `db/models.py` — Product model (upc, name, price) using Django ORM.
- `main.py` - Main program - loads products into the databases and displays them in the terminal.
- `sampleProducts.txt` — List of product sample data including UPC code, name, and price.

### Setup
1. python -m venv venv
2. venv\Scripts\activate (Windows)
3. pip install django
4. python manage.py makemigrations
5. python manage.py migrate
6. python main.py

