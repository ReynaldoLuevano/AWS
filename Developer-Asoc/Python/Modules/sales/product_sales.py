"""
This module contains classes for tracking
product and sales data
"""
class Product:

    def __init__(self, name, price, inventory):
        self.name = name
        self.price =  price
        self.inventory = inventory

    def __str__(self):
        return f"{self.name} - (${self.price})"          
                
class Sales:

    def __init__(self):
        self.sales_data = []
    
    def add_sale(product, quantity):
        sale = {'product': product, 'quantity': quantity} 
        self.sales_data.append(sale)

    def generate_report():