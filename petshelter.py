pet_list=[]

# functions
def add_pet(name, type, status):
    while True:
        name = input("Name of pet: ")
        type = input("Type of pet: ")
        status = input("Available / Adopted: ")

        if name and type and status != "":
            pet_list.append({"name": name, "type": type, "status": status})
            print("Added successfully!")
            break
        elif name or type or status == "":
            print("All questions should be answered!")

def view_pets():
    for item in pet_list:
        print(item)

def count_available_adopted(status):
    for item in pet_list:
        if status == "Available":    
            print(item)

def find_pet(name, type, status):
    pass

def display_menu():
    print(f"=== Pet Adoption Records ===")
    print("1. Add a pet\n2. View all pets\n3. Count available vs adopted\n4. Find a pet by name\n5. Exit")
    choice = input("Choose an option [1-5]:")

    if choice == 1:
        add_pet()
    elif choice == 2:
        view_pets()
    elif choice == 3:
        count_available_adopted
    elif choice == 4:
        find_pet()
    elif choice == 5:
        return

# main starts here
while True:
    display_menu()