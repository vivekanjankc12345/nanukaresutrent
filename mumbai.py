

data = []

def adddata():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    snack_price = float(input("Enter snack price: "))
    snack_availability = input("Is the snack available? (yes/no): ")
    snack = {
        "id": snack_id,
        "name": snack_name,
        "price": snack_price,
        "availability": snack_availability.lower() == "yes"
    }
    data.append(snack)
    print("Snack added successfully.")

def removedata():
    snack_id = input("Enter snack ID to remove: ")
    for snack in data:
        if snack["id"] == snack_id:
            data.remove(snack)
            print("Snack removed successfully.")
            return
    print("Snack not found.")

def updatedata():
    snack_id = input("Enter snack ID to update availability: ")
    for snack in data:
        if snack["id"] == snack_id:
            snack_availability = input("Is the snack available? (yes/no): ")
            snack["availability"] = snack_availability.lower() == "yes"
            print("Snack updated successfully.")
            return
    print("Snack not found.")

def displaydata():
    print("Snack Inventory:")
    
    for snack in data:
        print(f"ID: {snack['id']}")
        print(f"Name: {snack['name']}")
        print(f"Price: {snack['price']}")
        print(f"Availability: {'Yes' if snack['availability'] else 'No'}")
      

def recordsaledata():
    snack_id = input("Enter snack ID sold: ")
    for snack in data:
        if snack["id"] == snack_id:
            if snack["availability"]:
                snack["availability"] = False
                print("Sale recorded successfully.")
                return
            else:
                print("Snack is already sold.")
                return
    print("Snack not found.")

def displaysalesrecorddata():
    print("Sales Record:")
   
    for snack in data:
        if not snack["availability"]:
            print(f"ID: {snack['id']}")
            print(f"Name: {snack['name']}")
            print(f"Price: {snack['price']}")
          

def main():
    while True:
        print("\n Snack Inventory Management")
        print("1. Add a snack to inventory")
        print("2. Remove a snack from inventory")
        print("3. Update snack availability")
        print("4. Display snack inventory")
        print("5. Record a snack sale")
        print("6. Display sales record")
        print("7. Exit")

        choice = input("Enter your choice from 1 to 7 ")

        if choice == "1":
            adddata()
        elif choice == "2":
            removedata()
        elif choice == "3":
            updatedata()
        elif choice == "4":
            displaydata()
        elif choice == "5":
            recordsaledata()
        elif choice == "6":
            displaysalesrecorddata()
        elif choice == "7":
            print("Thank you for order visit again")
            break
        else:
            print("Wrong data. Please try again.")

if __name__ == "__main__":
    main()
