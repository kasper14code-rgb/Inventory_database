"""This module contains the base Item class that all other items will inherit from """

from abc import ABC, abstractmethod

class Item(ABC):
    """Abstract base class for all inventory items"""

    def __init__(self,name, quantity):
        self.name = name.lower()
        self.quantity = quantity
    
    def add_quantity(self, amount):
        """Increase item quantity by specified amount"""
        if amount > 0:
            self.quantity += amount
        else:
            print("Amount must be positive")
    
    def remove_quantity(self,amount):
        """ Decrease item quantity"""
        if amount <= 0:
            print("Amonut must be positive")
            return 0
        
        removed = min(amount,self.quantity)# so we can't remove more than we have
        self.quantity -= removed
        return removed
    
    def get_quantity(self):
        """Get the current quantity in stock"""
        return self.quantity
    def get_name(self):
        """Get the item's name"""
        return self.name
    def __str__(self):
        """String representation of the item for display"""
        return f"{self.name.capitalize()} ({self.get_type()}): {self.quantity}"
      

    @abstractmethod
    def get_type(self):
        """Abstract method that child classes must implement"""
        pass
    