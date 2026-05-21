"""Inventory management system that handles all operations"""
from .items import * # PerishableItem, DigitalItem
from datetime import datetime

class InventoryPrinter:
    """Handles printing inventory and receipts to files"""
    
    @staticmethod
    def print_stock(inventory,filename= f"INV_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"):
        """Print current inventory to a text file"""

        with open(filename,'w') as f:
            f.write("===CURRENT INVENTOTY===\n")
            f.write(f"Generated: {datetime.now()}\n\n")

            if not inventory:
                f.write("Inventory is empty.\n")
            else:
                for item in inventory.values():
                    f.write(f"{str(item)}\n")
                    
            f.write("\n=== END of REPORT ===")
        
        print(f"Stock report saved to {filename}")


    @staticmethod
    def print_receipt(items_sold,filename= f"Receipt_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"):
        #Used chatgpt whiched showed the strftime code and i asked where to learn about it on https://www.w3schools.com/python/python_datetime.asp
        """Print current inventory to a text file"""

        with open(filename,'w') as f:
            f.write("===RECEIPT ===\n")
            f.write(f"Date: {datetime.now()}\n\n")
            f.write("ITEMS PURCHASED:\n")
            
            total = 0
            for name, qty in items_sold:
                price = qty * 1.00
                total += price

                f.write(f"{name.capitalize():<15} {qty:>3} x R1.00 = R{price:.2f}")

            f.write("\n")
            f.write(f"TOTAL: R{total:.2f}")       
            f.write("\n Thank you for your purchase!")
        
        print(f"Stock report saved to {filename}")


class InventoryManger:
    """Main inventory management system"""

    def __init__(self):
        """Initialize with empy inventory and sales"""
        self.inventory = {}
        self.sold_items = []

    def add_item(self,item):
        """Add an item to inv or update qty if exists"""
        name = item.get_name()

        if name in self.inventory:
            self.inventory[name].add_quantity(item.get_quantity())
        else:
            self.inventory[name] = item
        
        print(f" Added {item.get_quantity()} {name}(s)")
    
    def remove_item(self,name):
        """Completely remove an item from inv"""
        name = name.lower()

        if name in self.inventory:
            del self.inventory[name]
            print(f"Removed {name}")
        else:
            print(f"{name} not found")

    def sell_item(self,name,quantity):
        """Sell items and trace sales
        Return:
                True if sale was successeful, False otherwise
        """
        name = name.lower()

        if name not in self.inventory:
            print(f"{name} not found")
            return False
        
        removed = self.inventory[name].remove_quantity(quantity)

        if removed > 0:
            self.sold_items.append((name,removed))
            print(f"Sold {removed} {name}(s)")
            #       Sold      5     apple(s)
            
            #check if we need to print receipt
            if input("Print receipt? (Y/n):").lower() == 'y':
                
                InventoryPrinter.print_receipt([(name,removed)])
            
            if self.inventory[name].get_quantity() == 0:
                print(f"{name} is now out of stock.")
                return True
        else:
            print(f"{name} is now out of stock")
            return False


    def print_curr_stock(self):
        """Print current inv to file"""  
        InventoryPrinter.print_stock(self.inventory)
        
    def view_inv(self):
        """Display current inv to console"""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\n--- CURRENT INVENTORY ---")
            for item in self.inventory.values():
                print(item)
    
    def view_sold_items(self):
        """DIsplay sale history to console"""
        """Display current inv to console"""
        if not self.sold_items:
            print("No items sold yet.")
        else:
            print("\n--- SALES HISTORY ---")
            for name, qty in self.sold_items:
                print(f"{name.capitalize()}: {qty} sold")
                #        Apple                 4   sold
