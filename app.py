from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database
menu_items = []

# Route to get all menu items
@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu_items)

# Route to add a new menu item
@app.route('/menu', methods=['POST'])
def add_menu():
    data = request.json
    menu_items.append(data)
    return jsonify({"message": "Item added successfully", "item": data}), 201

# Route to delete a menu item by ID
@app.route('/menu/<int:item_id>', methods=['DELETE'])
def delete_menu(item_id):
    global menu_items
    menu_items = [item for item in menu_items if item.get("id") != item_id]
    return jsonify({"message": f"Item with ID {item_id} deleted"})

if __name__ == '__main__':
    app.run(debug=True)
