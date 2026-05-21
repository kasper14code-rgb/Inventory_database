""" Main application with simple menu systems"""
from inventory.manager import InventoryManger
from inventory.items import *


def display_menu():
    """Display the main menu options"""
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Add Perishable Item")
    print("2. Add Digital Item")
    print("3. Remove Item")
    print("4. Sell Item")
    print("5. View Current Inventory")
    print("6. View Sale History")
    print("7. Print Current Stock")
    print("8. Exit")

def get_pInt(prompt):
    """Helper function to get +ve numbers"""

    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number")
        except:
            print("Please enter a valid number")


def main():
    """main program loop"""
    inv = InventoryManger()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice  == "1":
            # Add perishable item
            name = input("Enter item name:")
            qty = get_pInt("Enter quantity:")
            exp = input("Enter exp date (YYYY-MM-DD):")
            inv.add_item(PerishableItem(name,qty,exp))
        
        elif choice == "2":
            # Add Digital item
            name = input("Enter item name:")
            qty = get_pInt("Enter quantity:")
            inv.add_item(DigitalItem(name,qty))

        elif choice =="3":
            #Remove item
            name = input ("Enter item name:")
            # qty = get_pInt("Enter quantity:")
            inv.remove_item(name)

        elif choice =="4":
            #sell item
            name = input ("Enter item name:")
            qty = get_pInt("Enter quantity:")
            inv.sell_item(name,qty)
        elif choice == "5":
            #view inventory
            inv.view_inv()
        elif choice == "6":
            # view sales
            inv.view_sold_items()
        elif choice == "7":
            # print stock
            inv.print_curr_stock()
        elif choice == "8":
            #Exit program
            print("Thank you bye!")
            break
        else:
            print("Invalid choice. Please enter a number 1- 8")

if __name__ == "__main__":
    main()





