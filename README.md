## Q1 — Code Organization & Django ORM

### Repository Contents (Added)
- `db/models.py` — Product model (upc, name, price) using Django ORM.
- `main.py` - Main program - loads products into the databases and displays them in the terminal.
- `sampleProducts.txt` — List of product sample data including UPC code, name, and price.
- `Instructions.md ` - Assignment Part 1 instructions (originally the README file).
- `sampleproducts.txt` - List of sample products with upc, name, and price.
- `UI.py` - Tkinter-based GUI program - scans upc codes and stores them in the database.

### Environment Setup
1. python -m venv venv
2. venv\Scripts\activate (Windows)
3. pip install django
4. python manage.py makemigrations
5. python manage.py migrate

### Run Instructions
1. python main.py
2. python UI.py

### Django ORM Usage
![alt text](images/image-1.png)

### Screenshots
Imported Products
![alt text](images/image.png)

Scanner UI
![alt text](images/image-2.png)

Successful Scan
![alt text](images/image-3.png)
![alt text](images/image-4.png)

Unsuccessful Scan
![alt text](images/image-5.png)
![alt text](images/image-6.png)

Scrollbar Functionality
![alt text](images/image-7.png)