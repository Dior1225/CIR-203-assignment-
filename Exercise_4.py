# ==============================================
# **EXERCISE 4: PYTHON DICTIONARIES (E-COMMERCE SECTOR)**
# ==============================================

print("EXERCISE 4: PYTHON DICTIONARIES (E-COMMERCE SECTOR)")
inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Headphones": 20,
    "Monitor": 5,
    "Keyboard": 12
}
print("Initial inventory:", inventory)

inventory["Mouse"] = 18
inventory["Phone"] = 10
print("Updated inventory:", inventory)

def low_stock(inv):
    return {product: qty for product, qty in inv.items() if qty < 10}

print("Low stock items:", low_stock(inventory))

del inventory["Monitor"]
print("Inventory after deletion:", inventory)

print("Final inventory listing:")
for product, qty in inventory.items():
    print(product, ":", qty)
