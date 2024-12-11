from flask import Flask, request, jsonify, render_template
from Inventory_Management import InventoryManager

app = Flask(__name__)
INVENTORY_FILE_PATH = './data/inventory.json'
inventory_manager = InventoryManager(INVENTORY_FILE_PATH)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        try:
            item_name = request.form.get('name')
            quantity = int(request.form.get('quantity'))
            price = float(request.form.get('price'))

            inventory_manager.add_item(item_name, quantity, price)
            return render_template('add_item.html', inventory=inventory_manager.inventory)

        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return render_template('add_item.html')

@app.route('/remove_item', methods=['GET', 'POST'])
def remove_item():
    if request.method == 'POST':
        try:
            item_name = request.form.get('name')
            if inventory_manager.remove_item(item_name):
                return render_template('remove_item.html', inventory=inventory_manager.inventory, message=f'Item "{item_name}" removed successfully.')
            else:
                return render_template('remove_item.html', inventory=inventory_manager.inventory, message=f'Item "{item_name}" not found in inventory.')

        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return render_template('remove_item.html', inventory=inventory_manager.inventory)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return render_template('inventory.html', inventory=inventory_manager.inventory)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)