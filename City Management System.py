class Vehicle:
    def __init__(self, reg_num, owner):
        self.registration_number = reg_num
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display(self):
        print(f"{self.registration_number}, {self.owner}")

vehicles = {}

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles
        print(f"Updated vehicle {reg_num}")
    else:
        print("Not found")

def add_owner(reg_num, owner):
    vehicles[reg_num] = Vehicle(reg_num, owner)

def display_vehicles():
    for vehicle in vehicles.values():
        vehicle.display()


while True:
    choice = input("Would you like to 'update', 'add', 'display', or 'exit'? ")

    try:
        if choice == "update":
            reg_num = input("Enter registration number: ")
            new_owner = input("Enter new owner: ")
            update_vehicle_owner(reg_num, new_owner)
        elif choice == "add":
            reg_num = input("Enter registration number: ")
            owner = input("Enter owner: ")
            add_owner(reg_num, owner)
        elif choice == "display":
            display_vehicles()
        elif choice == "exit":
            break
        else:
            print("Please choose 'update', 'add', 'display', or 'exit'")
    except:
        print("An error occurred")

