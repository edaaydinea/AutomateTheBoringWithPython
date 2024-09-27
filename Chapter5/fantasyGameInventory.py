# inventory.py
stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    
    for item, count in inventory.items():  # Loop through inventory items
        print(f"{count} {item}")  # Display item count and name
        item_total += count  # Add to total count
    
    print("Total number of items: " + str(item_total))  # Print total items

# Call the function to display the inventory
displayInventory(stuff)
