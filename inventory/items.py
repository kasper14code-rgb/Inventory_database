from .base import Item

"""Concrete item classes that inherit from base  Item class"""

class PerishableItem(Item):
    """A perishable item that has an expiration date."""

    def __init__(self,name,quantity,exp_date):
        super().__init__(name,quantity)# Initialize parant class
        self.exp_date = exp_date
    
    def get_type(self):
        """Returns item type(Implementation of abstract metho)"""
        
        return "Perishable"
    
    def __str__(self):
        return f"{super().__str__()} | Expires: {self.exp_date}"


class DigitalItem(Item):
    """A digital item doesn't have physical stock. Show simple inheritance without additionl attributes"""
    # def __init__(self, name,quantity,):
    #     super().__init__(name,quantity)

    def get_type(self):
        return "Digital"
    
    def __str__(self):
         return f"{super().__str__()} | Downloadble"

    