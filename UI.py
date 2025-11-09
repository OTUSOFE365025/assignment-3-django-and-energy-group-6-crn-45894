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
        
        #Spacer moves elements down
        self.topSpacer = Label(master, text="")
        self.topSpacer.pack(pady=10)  # adjust this value to move down

        #Text label
        self.label = Label(master, text="Enter UPC to Scan:", font=("Times New Roman", 14))
        self.label.pack(pady=5)
        
        #Scan button
        self.upcEntry = Entry(master, font=("Times New Roman", 14))
        self.upcEntry.pack(pady=3)
        
        self.scanButton = Button(master, text="Scan", command=self.scanProduct, font=("Times New Roman", 12))
        self.scanButton.pack(pady=3)
        
        #Subtotal
        self.subtotal = Decimal('0.00')
        self.subLabel = Label(master, text=f"Subtotal: ${self.subtotal:.2f}", font=("Times New Roman", 14, "bold"))
        self.subLabel.pack(pady=5)
        
        #Display area with scrollbar
        self.textFrame = Frame(master)
        self.textFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        
        self.display = Text(self.textFrame, height=12, width=45, font=("Courier New", 11))
        self.display.grid(row=0, column=0, sticky="nsew")
        
        self.scrollbar = Scrollbar(self.textFrame, command=self.display.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.display.config(yscrollcommand=self.scrollbar.set)
        self.display.config(state=NORMAL)
        
        self.textFrame.grid_rowconfigure(0, weight=1)
        self.textFrame.grid_columnconfigure(0, weight=1)
    
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