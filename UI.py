import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
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
        self.label = Label(master, text="Enter UPC to Scan:", font=("Lato", 14))
        self.label.pack(pady=10)
        
        self.upcEntry = Entry(master, font=("Open Sans", 14))
        self.upcEntry.pack(pady=5)
        
        self.scanButton = Button(master, text="Scan", command=self.scanProduct, font=("Lato", 12))
        self.scanButton.pack(pady=10)
        
        self.subtotal = Decimal('0.00')
        self.subLabel = Label(master, text=f"Subtotal: ${self.subtotal:.2f}", font=("Lato", 14, "bold"))
        self.subLabel.pack(pady=10)
        
        self.bottomMargin = Label(master, text="")
        self.bottomMargin.pack(pady=5)
        
        self.display = Text(master, height=10, width=40)
        self.display.pack()
    
    #Function to scan products and output them to display
    def scanProduct(self):
        
        #Takes in upc code and performs error handling
        upc = self.upcEntry.get().strip()
        if not upc:
            messagebox.showwarning("Warning", "Enter a UPC code.")
            return
        
        #Scanning sequence with error handling
        try:
            prod = Product.objects.get(upc=upc)
            self.display.config(state=NORMAL)
            self.display.insert(END, f"Scanned: {prod.name} - ${prod.price}\n")
            self.display.config(state=DISABLED)
            self.subtotal += prod.price
            self.subLabel.config(text=f"Subtotal: ${self.subtotal:.2f}")
        except Product.DoesNotExist:
            messagebox.showerror("Error", f"Product with UPC {upc} not found")
        
        #Input cleared after scan
        self.upcEntry.delete(0, END)
        self.upcEntry.focus()

root = Tk()
program = CashRegister(root)
root.mainloop()