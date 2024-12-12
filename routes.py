from flask import jsonify, request, render_template
from app_instance import app
from InventoryManagement import Inventory_Manager

INVENTORY_FILE_PATH = './data/inventory.json'
inventory_manager = Inventory_Manager(INVENTORY_FILE_PATH)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form.get('name')
        quantity = int(request.form.get('quantity'))
        price = float(request.form.get('price'))
        inventory_manager.add_item(item_name, quantity, price)
        return render_template('add_item.html', inventory=inventory_manager.inventory)
    return render_template('add_item.html')

@app.route('/remove_item', methods=['GET', 'POST'])
def remove_item():
    if request.method == 'POST':
        item_name = request.form.get('name')
        if inventory_manager.remove_item(item_name):
            message = f'Item "{item_name}" removed successfully.'
        else:
            message = f'Item "{item_name}" not found in inventory.'
        return render_template('remove_item.html', inventory=inventory_manager.inventory, message=message)
    return render_template('remove_item.html', inventory=inventory_manager.inventory)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return render_template('inventory.html', inventory=inventory_manager.inventory)

@app.route('/')
def index():
    return render_template('index.html')