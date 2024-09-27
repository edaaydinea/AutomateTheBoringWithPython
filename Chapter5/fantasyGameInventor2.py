# inventory.py

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    
    for item, count in inventory.items():  # Loop through inventory items
        print(f"{count} {item}")  # Display item count and name
        item_total += count  # Add to total count
    
    print("Total number of items: " + str(item_total))  # Print total items

def addToInventory(inventory, addedItems):
    for item in addedItems:  # Loop through each item in the added items
        if item in inventory:  # Check if the item is already in the inventory
            inventory[item] += 1  # Increment the count of the existing item
        else:
            inventory[item] = 1  # Add the new item with count 1
    return inventory  # Return the updated inventory

# Initial inventory
inv = {'gold coin': 42, 'rope': 1}

# Items to add
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Update inventory
inv = addToInventory(inv, dragonLoot)

# Display updated inventory
displayInventory(inv)
