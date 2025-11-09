import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

from tkinter import *
from tkinter import messagebox
from decimal import Decimal
from db.models import Product

class CashRegister:
    
    #Initializer for GUI window
    def __init__(self, master):
        
        #Define main scanner window
        self.master = master
        master.title("Cash Register (Django ORM + Tkinter)")
        master.geometry("400x400")
        master.resizable(0, 0)
    
        #Define text labels, text entry areas, buttons, and display areas
        self.label = Label(master, text="Enter UPC to Scan:", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.upcEntry = Entry(master, font=("Arial", 14))
        self.upcEntry.pack(pady=5)
        
        self.scanButton = Button(master, text="Scan", command=self.scanProduct, font=("Arial", 12))
        self.scanButton.pack(pady=10)
        
        self.subtotal = Decimal('0.00')
        self.subLabel = Label(master, text=f"Subtotal: ${self.subtotal:.2f}", font=("Arial", 14, "bold"))
        self.subLabel.pack(pady=10)
        
        self.bottomMargin = Label(master, text="")
        self.bottomMargin.pack(pady=5)
        
        
