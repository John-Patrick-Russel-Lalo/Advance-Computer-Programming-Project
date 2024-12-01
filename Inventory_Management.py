import json
import os

class InventoryManager:
    def __init__(self, inventory_file_path):
        self.inventory_file_path = inventory_file_path
        self.inventory = self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.inventory_file_path):
            with open(self.inventory_file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_inventory(self):
        with open(self.inventory_file_path, 'w') as f:
            json.dump(self.inventory, f)

    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['price'] = price  # Update price if necessary
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
        self.save_inventory()

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            self.save_inventory()
            return True
        return False