items = {
    "keys": "Bedroom table",
    "wallet": "Study desk",
    "headphones": "Laptop bag",
    "charger": "Near the bed",
    "watch": "Drawer"
}

print("====== LOST ITEM FINDER ======")

search = input("Enter the item you lost: ").lower()

if search in items:
    print("\nItem found!")
    print("Location:", items[search])
else:
    print("\nSorry, item not found.")

print("\nAvailable items:")
for item in items:
    print("-", item)